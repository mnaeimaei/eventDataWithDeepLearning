import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

CREATE TABLE  `mimic-four-377221.E6_BloodGas.bgB14_E2_ABG`   AS

SELECT distinct

rowNum,
Label2,
Value


FROM `mimic-four-377221.E6_BloodGas.bgA6`
where   Label_Syn="Item3"
or   Label_Syn="Item5"
or   Label_Syn="Item22"
or   Label_Syn="Item25"
or   Label_Syn="Item27"






'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
