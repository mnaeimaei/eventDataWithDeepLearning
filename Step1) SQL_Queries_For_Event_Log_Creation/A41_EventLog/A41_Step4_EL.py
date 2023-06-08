import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

alter table `mimic-four-377221.C0_EventLog.AEL1` 
add column Entity1_Origin string;


alter table `mimic-four-377221.C0_EventLog.EL1` 
add column Entity1_Origin string;

##############################################################

alter table `mimic-four-377221.C0_EventLog.AEL1` 
add column Entity2_Origin string;


alter table `mimic-four-377221.C0_EventLog.EL1` 
add column Entity2_Origin string;

##############################################################

alter table `mimic-four-377221.C0_EventLog.AEL1` 
add column Entity1_ID int;


alter table `mimic-four-377221.C0_EventLog.EL1` 
add column Entity1_ID int;

##############################################################

alter table `mimic-four-377221.C0_EventLog.AEL1` 
add column Entity2_ID int;


alter table `mimic-four-377221.C0_EventLog.EL1` 
add column Entity2_ID int;

##############################################################


update `mimic-four-377221.C0_EventLog.AEL1` 
set Entity1_Origin="Patient"
where Entity1_Origin is null;


update `mimic-four-377221.C0_EventLog.AEL1` 
set Entity2_Origin="Admission"
where Entity2_Origin is null;

##############################################################


update `mimic-four-377221.C0_EventLog.EL1` 
set Entity1_Origin="Patient"
where Entity1_Origin is null;


update `mimic-four-377221.C0_EventLog.EL1` 
set Entity2_Origin="Admission"
where Entity2_Origin is null;




'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
