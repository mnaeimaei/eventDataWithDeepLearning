import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

alter table `mimic-four-377221.C0_Activity_Event.Bond` 
add column dkID string;

update `mimic-four-377221.C0_Activity_Event.Bond` 
set dkID="dk"
where dkID is null;


create table  `mimic-four-377221.C0_Activity_Event.Bond_output` as
Select 
concat(dkID,Row_number() over (partition by dkID order by Activity_Origin)) as dkID
, Activity, Activity_Synonym, Activity_Origin, Activity_Value_ID, OTC
from `mimic-four-377221.C0_Activity_Event.Bond` ;

drop table `mimic-four-377221.C0_Activity_Event.Bond` ;


'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
