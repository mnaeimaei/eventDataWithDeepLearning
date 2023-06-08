import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            


################################################

CREATE TABLE  `mimic-four-377221.R_TimeJ.c1`   AS
select distinct * from
(SELECT * FROM `mimic-four-377221.R_TimeJ.b1` 
union all
SELECT * FROM `mimic-four-377221.R_TimeJ.b2` );

################################################

'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
