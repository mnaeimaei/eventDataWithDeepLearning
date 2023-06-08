import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

create table `mimic-four-377221.C0_OCT.OCT_Nodes` as
SELECT * FROM `snomed-ct-377221.SCT_3.PaperD` ;

create table `mimic-four-377221.C0_OCT.OCT_Rel` as
SELECT * FROM `snomed-ct-377221.SCT_3.PaperB` ;


'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
