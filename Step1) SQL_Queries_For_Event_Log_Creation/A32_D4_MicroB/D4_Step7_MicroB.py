import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            


 
         CREATE   TABLE `mimic-four-377221.D4_MicroB.Disorders_MicroB`  AS
        SELECT distinct
a.subject_id, a.hadm_id, a.Type, a.ActivityValue_ID as ActivityValueID, b.Disorders

FROM `mimic-four-377221.D4_MicroB.eLogA_MicroB` a
left join  `mimic-four-377221.P_NonEvents.K8` b
on
a.subject_id=b.subject_id
and
a.hadm_id=b.hadm_id
 
 

'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
