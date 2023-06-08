import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

        CREATE TABLE `mimic-four-377221.C0_EventLog.Timing2`  AS

        SELECT * FROM 
        (SELECT
        a.subject_id, a.hadm_id,
        
        a.maxTime, b.RankN
        FROM `mimic-four-377221.C0_EventLog.Timing`  a
        LEFT   JOIN (
        SELECT  
        subject_id, hadm_id,
        Row_number() over (partition by  subject_id order by maxTime asc) as RankN
        FROM
        
        (SELECT   DISTINCT subject_id, hadm_id, maxTime  FROM `mimic-four-377221.C0_EventLog.Timing`  )  ) b
        ON
        a.subject_id = b.subject_id AND a.hadm_id = b.hadm_id)
        order by subject_id, hadm_id, maxTime;
        
        drop table `mimic-four-377221.C0_EventLog.Timing` ;

'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
