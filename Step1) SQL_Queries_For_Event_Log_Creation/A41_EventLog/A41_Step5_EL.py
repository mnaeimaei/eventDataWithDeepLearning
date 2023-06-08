import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

create table `mimic-four-377221.C0_EventLog.EL2` as
SELECT 
rowNum, Timestamp, 
subject_id, Entity1_Origin, Entity1_ID,
hadm_id, Entity2_Origin, Entity2_ID,
Activity, Activity_Synonym,  Activity_Origin, Activity_Value_ID
FROM `mimic-four-377221.C0_EventLog.EL1` ;

create table `mimic-four-377221.C0_EventLog.AEL2` as
SELECT 
rowNum, Timestamp, 
subject_id, Entity1_Origin, Entity1_ID,
hadm_id, Entity2_Origin, Entity2_ID,
Activity, Activity_Synonym,  Activity_Origin, Activity_Value_ID
FROM `mimic-four-377221.C0_EventLog.AEL1` ;

drop table `mimic-four-377221.C0_EventLog.EL1` ;

drop table `mimic-four-377221.C0_EventLog.AEL1` ;



'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
