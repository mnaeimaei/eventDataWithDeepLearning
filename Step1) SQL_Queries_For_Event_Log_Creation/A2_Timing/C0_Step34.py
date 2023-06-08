import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            


################################################

CREATE TABLE  `mimic-four-377221.R_TimeJ.b1`   AS


select subject_id, hadm_id, stay_id, transfer_id, min(min_Time) as min_Time, max_Time
from

(SELECT 
subject_id, hadm_id, stay_id, transfer_id, min_Time, max(max_Time) as max_Time

 FROM `mimic-four-377221.R_TimeJ.a1` 
 group by subject_id, hadm_id, stay_id, transfer_id, min_Time)


 group by subject_id, hadm_id, stay_id, transfer_id, max_Time;


################################################

CREATE TABLE  `mimic-four-377221.R_TimeJ.b2`   AS


select subject_id, hadm_id, stay_id, transfer_id, min(min_Time) as min_Time, max_Time
from

(SELECT 
subject_id, hadm_id, stay_id, transfer_id, min_Time, max(max_Time) as max_Time

 FROM `mimic-four-377221.R_TimeJ.a2` 
 group by subject_id, hadm_id, stay_id, transfer_id, min_Time)


 group by subject_id, hadm_id, stay_id, transfer_id, max_Time;

################################################
'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
