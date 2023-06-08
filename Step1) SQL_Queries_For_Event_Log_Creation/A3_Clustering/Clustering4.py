import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

CREATE TABLE `mimic-four-377221.Q_ClusA.Q4_Admissions`  AS

SELECT 
subject_id, hadm_id, insurance, `language`, marital_status, race


 FROM `mimic-four-377221.Q_ClusA.Q3_Admissions` ;


'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
