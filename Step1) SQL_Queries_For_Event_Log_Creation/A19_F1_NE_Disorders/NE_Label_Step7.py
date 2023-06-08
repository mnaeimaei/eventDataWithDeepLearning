import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

create table  `mimic-four-377221.F1_NE_Disorders.S7` as
SELECT 

a.subject_id, a.hadm_id, a.icd_num, a.seq_max, a.seq_num, b.num as icd_code_int, b.Final as icd_code_str, a.icd_code, 
a.icd_version, a.long_title

FROM `mimic-four-377221.F1_NE_Disorders.S4` a
left join `mimic-four-377221.F1_NE_Disorders.S6` b
on
a.icd_code=b.icd_code



'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
