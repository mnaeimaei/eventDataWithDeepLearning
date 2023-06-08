import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            



create schema `mimic-four-377221.E4_Micro` ;


create table `mimic-four-377221.E4_Micro.Micro_A` as
SELECT * FROM `mimic-four-377221.S_Microbiology.1_Microbiology` ;




'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
