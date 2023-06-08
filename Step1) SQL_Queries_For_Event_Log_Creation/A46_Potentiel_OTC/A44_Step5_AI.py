import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            
create table `mimic-four-377221.C0_Potential_OCT.PO2` as
SELECT distinct *  FROM `mimic-four-377221.C0_Potential_OCT.PO1` 

drop table `mimic-four-377221.C0_Potential_OCT.PO1` ;

'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
