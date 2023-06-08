import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

alter table `mimic-four-377221.C0_EventLog.AEL_final` 
add column Event string;

update `mimic-four-377221.C0_EventLog.AEL_final` 
set Event="e"
where Event is null;


create table  `mimic-four-377221.C0_EventLog.AEL_output` as
Select 
concat(Event,Row_number() over (partition by Event order by Entity1_ID, Timestamp)) as Event
, Timestamp, Entity1_Origin, Entity1_ID, Entity2_Origin, Entity2_ID, Activity, Activity_Synonym, Activity_Origin, Activity_Value_ID
from `mimic-four-377221.C0_EventLog.AEL_final` ;





alter table `mimic-four-377221.C0_EventLog.EL_final` 
add column Event string;

update `mimic-four-377221.C0_EventLog.EL_final` 
set Event="e"
where Event is null;


create table  `mimic-four-377221.C0_EventLog.EL_output` as
Select 
concat(Event,Row_number() over (partition by Event order by Entity1_ID, Timestamp)) as Event
, Timestamp, Entity1_Origin, Entity1_ID, Entity2_Origin, Entity2_ID, Activity, Activity_Synonym, Activity_Origin, Activity_Value_ID
from `mimic-four-377221.C0_EventLog.EL_final` ;

drop table `mimic-four-377221.C0_EventLog.EL_final` ;


drop table `mimic-four-377221.C0_EventLog.AEL_final` ;



'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
