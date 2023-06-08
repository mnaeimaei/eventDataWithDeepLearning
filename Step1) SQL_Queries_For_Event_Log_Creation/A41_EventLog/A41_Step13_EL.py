import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

update `mimic-four-377221.C0_EventLog.sub2` 
set RRR=null
where RRR=1;


update `mimic-four-377221.C0_EventLog.sub2` 
set RRR=null
where RRR=2;


update `mimic-four-377221.C0_EventLog.sub2` 
set RRR=null
where RRR=3;


update `mimic-four-377221.C0_EventLog.sub2` 
set RRR=null
where subject_id=13313474;

update `mimic-four-377221.C0_EventLog.sub2` 
set RRR=null
where subject_id=17905563;


update `mimic-four-377221.C0_EventLog.sub2` 
set RRR=null
where subject_id=18030855;



#########################################################################################

update `mimic-four-377221.C0_EventLog.sub2` 
set RRR=97846
where subject_id=10000032;


update `mimic-four-377221.C0_EventLog.sub2` 
set RRR=96300
where subject_id=10000280;


update `mimic-four-377221.C0_EventLog.sub2` 
set RRR=40197
where subject_id=10000635;

#########################################################################################

update `mimic-four-377221.C0_EventLog.sub2` 
set RRR=1
where subject_id=13313474;

update `mimic-four-377221.C0_EventLog.sub2` 
set RRR=2
where subject_id=17905563;


update `mimic-four-377221.C0_EventLog.sub2` 
set RRR=3
where subject_id=18030855;


'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
