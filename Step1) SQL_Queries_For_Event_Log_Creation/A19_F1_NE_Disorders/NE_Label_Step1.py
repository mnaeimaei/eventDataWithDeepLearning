import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

create schema `mimic-four-377221.F1_NE_Disorders` ;

create table `mimic-four-377221.F1_NE_Disorders.S1` as

SELECT hadm_id, count(icd_code) as icd_num

 FROM `mimic-four-377221.P_NonEvents.icdCM1` 
 group by hadm_id
 



'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
