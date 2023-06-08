import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

create schema `mimic-four-377221.R_TimeJ` ;
################################################

CREATE TABLE  `mimic-four-377221.R_TimeJ.a1`   AS

SELECT subject_id, hadm_id, stay_id, transfer_id, min_S as min_Time, max_S as max_Time FROM `mimic-four-377221.R_TimeI.I_All_p1` ;

################################################

CREATE TABLE  `mimic-four-377221.R_TimeJ.a2`   AS

SELECT * FROM `mimic-four-377221.R_TimeI.I_All_p23` ;

################################################

'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
