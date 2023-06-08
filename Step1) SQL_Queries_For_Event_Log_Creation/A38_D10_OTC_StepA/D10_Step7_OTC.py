import os
from google.cloud import bigquery

symPath = '../gcKey/SNOMED_CT_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            
        CREATE TABLE  `snomed-ct-377221.SCT_2.B_1`   AS
        SELECT distinct
a.conceptId,
a.term,
a.TLC,
b.term as termB
FROM `snomed-ct-377221.SCT_2.A_Description2` a
left join `snomed-ct-377221.SCT_2.A_Definition` b
on 
a.conceptId=b.conceptId
        
        
'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
