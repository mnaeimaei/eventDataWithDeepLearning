import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
#print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            
create schema `mimic-four-377221.S_Admission` ;

create table `mimic-four-377221.S_Admission.1_Admissions` as
select
           subject_id,
           hadm_id,
           insurance,
           language,
           marital_status,
           race
from  `mimic-four-377221.x_mimiciv_hosp.admissions` 
'''


QUERY = (query1)


query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)

















