import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            


        CREATE TABLE  `mimic-four-377221.E4_Micro.Micro_B92`   AS 
        select * from
(SELECT distinct

a.rowNum,
b.subject_id, b.hadm_id, b.Activity, b.Activity_Synonym, b.Timestamp,  b.ActivityValueID, b.TYPE as Type



FROM `mimic-four-377221.E4_Micro.Micro_B8` a
left join  `mimic-four-377221.E4_Micro.Micro_B71` b
on a.rowNum=b.rowNum)
where subject_id is not null
;


'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
