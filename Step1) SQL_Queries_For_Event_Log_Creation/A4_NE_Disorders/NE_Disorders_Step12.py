import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

        CREATE TABLE  `mimic-four-377221.P_NonEvents.K8`   AS
        SELECT 
        subject_id, hadm_id, STRING_AGG(icd_code_syn ORDER BY icd_code_syn) as Disorders
        FROM `mimic-four-377221.P_NonEvents.K5` 
        GROUP BY subject_id, hadm_id;
        
        update `mimic-four-377221.P_NonEvents.K8` 
        set Disorders=REPLACE(Disorders,"D0","")
        where Disorders is not null;
        
        update `mimic-four-377221.P_NonEvents.K8` 
        set Disorders=REPLACE(Disorders,"D","")
        where Disorders is not null;



'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
