import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

        CREATE TABLE  `mimic-four-377221.Q_ClusA.Q7_AdmPatTime`   AS
        SELECT
        a.subject_id, b.hadm_id_num, a.gender, a.anchor_age, a.dod
        
        From `mimic-four-377221.Q_ClusA.Q6_AdmissionPatient`   as a
        LEFT JOIN `mimic-four-377221.Q_ClusA.Q2_Timing`   as b
        ON
        a.subject_id=b.subject_id 
        ;

'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
