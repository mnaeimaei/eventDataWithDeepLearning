import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            


create schema `mimic-four-377221.E2_Trans` ;

create table `mimic-four-377221.E2_Trans.Trans1` as
SELECT * FROM `mimic-four-377221.S_Transfers.1_Transfer` ;

update `mimic-four-377221.E2_Trans.Trans1`
set hadm_id=0
where hadm_id is null;




'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
