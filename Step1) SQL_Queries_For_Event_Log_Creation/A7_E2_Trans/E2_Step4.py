import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            


alter table `mimic-four-377221.E2_Trans.Trans2` 
add column careunit2 string;

update `mimic-four-377221.E2_Trans.Trans2` 
set careunit2 ="ND"
where careunit2 is null	;




'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
