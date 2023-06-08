import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

create schema `mimic-four-377221.F5_BloodGasC` ;

CREATE TABLE  `mimic-four-377221.F5_BloodGasC.A1`   AS
SELECT * FROM `mimic-four-377221.E6_BloodGas.bgB14_C2` 

'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
