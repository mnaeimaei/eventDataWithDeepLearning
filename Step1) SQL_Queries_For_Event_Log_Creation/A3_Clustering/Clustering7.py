import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

        CREATE TABLE  `mimic-four-377221.Q_ClusA.Q6_AdmissionPatient`   AS
        SELECT 
        distinct subject_id, gender_Int as gender, anchor_age , Died as dod
        FROM `mimic-four-377221.Q_ClusA.Q5_AdmissionPatient` 

'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
