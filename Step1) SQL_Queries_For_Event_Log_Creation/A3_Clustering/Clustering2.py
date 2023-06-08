import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            



      CREATE TABLE `mimic-four-377221.Q_ClusA.Q2_Admissions`  AS
        
        SELECT
        a.subject_id, a.hadm_id,
        
        a.insurance, a.language, a.marital_status, a.race, b.RankN
        FROM `mimic-four-377221.Q_ClusA.Q1_Admissions`  a
        LEFT   JOIN (
        SELECT  
        subject_id, hadm_id,
        Row_number() over (partition by  subject_id order by hadm_id asc) as RankN
        FROM
        
        (SELECT   DISTINCT subject_id, hadm_id  FROM `mimic-four-377221.Q_ClusA.Q1_Admissions`  )  ) b
        ON
        a.subject_id = b.subject_id AND a.hadm_id = b.hadm_id;
        



'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
