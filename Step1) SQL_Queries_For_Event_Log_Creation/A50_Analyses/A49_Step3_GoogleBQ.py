import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

create table  `mimic-four-377221.C0_EventLog.AEL_final_Disorders2`  as
select distinct * from(
SELECT 
a.Type,
a.ActivityValueID,
a.Disorders,
b.Disorders as Disorders_ML


 FROM `mimic-four-377221.C0_EventLog.AEL_final_Disorders` a
 left join `mimic-four-377221.C0_EventLog.ML` b

on
a.ActivityValueID=b.rowNum
and
a.Type=b.Activity_Origin);

create table  `mimic-four-377221.C0_EventLog.EL_final_Disorders2`  as
select distinct * from(
SELECT 
a.Type,
a.ActivityValueID,
a.Disorders,
b.Disorders as Disorders_ML


 FROM `mimic-four-377221.C0_EventLog.EL_final_Disorders` a
 left join `mimic-four-377221.C0_EventLog.ML` b

on
a.ActivityValueID=b.rowNum
and
a.Type=b.Activity_Origin);




'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
