import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

        CREATE TABLE  `mimic-four-377221.Q_ClusA.Q2_Timing`   AS
        SELECT subject_id, COUNT (hadm_id) as hadm_id_num
        FROM  `mimic-four-377221.Q_ClusA.Q1_Timing`     
        GROUP BY subject_id

'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
