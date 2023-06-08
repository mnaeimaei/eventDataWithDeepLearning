import os
from google.cloud import bigquery

symPath = '../gcKey/SNOMED_CT_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''          

CREATE TABLE  `snomed-ct-377221.SCT_2.B_3`   AS
SELECT distinct
a.conceptId,
a.term as termA,
a.TLC as Semanti_tags,
a.termB,
b.ConceptType
FROM `snomed-ct-377221.SCT_2.B_1` a
left join `snomed-ct-377221.SCT_2.B_2` b
on 
a.conceptId=b.conceptId




'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
