import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

create table `mimic-four-377221.F1_NE_Disorders.S2` as
SELECT 
a.subject_id,
a.hadm_id,
b.icd_num,
a.seq_num,
a.icd_code,
a.icd_version,
a.long_title
FROM `mimic-four-377221.P_NonEvents.icdCM1` a
left join  `mimic-four-377221.F1_NE_Disorders.S1` b
on
a.hadm_id=b.hadm_id


'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
