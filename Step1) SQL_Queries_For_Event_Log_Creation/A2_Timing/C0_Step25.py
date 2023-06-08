import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

#######################################################

create table  `mimic-four-377221.R_TimeI.I_All_p1` as
SELECT * FROM `mimic-four-377221.R_TimeI.I_All` 
where hadm_id=0 and stay_id is  null and transfer_id is  null;



#######################################################

create table  `mimic-four-377221.R_TimeI.I_All_p2` as
SELECT * FROM `mimic-four-377221.R_TimeI.I_All` 
where hadm_id<>0 

;
#######################################################
update `mimic-four-377221.R_TimeI.I_All_p1` 
set stay_id=0
where stay_id is null;

update `mimic-four-377221.R_TimeI.I_All_p1` 
set transfer_id=0
where transfer_id is null;

#######################################################


'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
