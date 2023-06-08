import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            


        CREATE TABLE  `mimic-four-377221.Q_ClusA.Q5_AdmissionPatient`   AS
        SELECT
        a.subject_id, a.insurance, a.language, a.marital_status, a.race,
        b.gender, b.anchor_age, b.anchor_year, b.anchor_year_group, b.dod,
        From `mimic-four-377221.Q_ClusA.Q4_Admissions`   as a
        LEFT JOIN `mimic-four-377221.Q_ClusA.Q1_Patient`   as b
        ON
        a.subject_id=b.subject_id 
        ;



'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
