import os
from google.cloud import bigquery

symPath = '../gcKey/SNOMED_CT_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            
        CREATE TABLE  `snomed-ct-377221.SCT_2.A_Description`   AS
        (SELECT conceptId, Max(term) AS term from
        
        (SELECT distinct conceptId,term  FROM `snomed-ct-377221.SCT.Terminology_Description` 
        where typeId=900000000000003001         and term like "%)"
        order by conceptId )
        GROUP BY conceptId)
'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
