import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            
create table `mimic-four-377221.E2_Trans.Trans2` as
SELECT * FROM `mimic-four-377221.E2_Trans.Trans1` ;


alter table `mimic-four-377221.E2_Trans.Trans2` 
add column act1 string;

alter table `mimic-four-377221.E2_Trans.Trans2` 
add column act11 string;

alter table `mimic-four-377221.E2_Trans.Trans2` 
add column act2 string;


alter table `mimic-four-377221.E2_Trans.Trans2` 
add column act22 string;



'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
