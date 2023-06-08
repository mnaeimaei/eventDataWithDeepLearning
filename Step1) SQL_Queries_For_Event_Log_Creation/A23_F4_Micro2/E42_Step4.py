import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath
client = bigquery.Client()

# Perform a query.
query1 = f'''            

create table `mimic-four-377221.F4_Micro2.T2` as

SELECT 
a.subject_id,
a.hadm_id,
a.icd_num,
a.seq_max,
a.seq_num,
a.icd_code_int,
a.icd_code_str,
a.icd_code,
a.icd_version,
a.long_title



from
(SELECT distinct *FROM `mimic-four-377221.F1_NE_Disorders.S7` 
where icd_num=2 and seq_max=2) a
left join (SELECT distinct icd_code  FROM `mimic-four-377221.F1_NE_Disorders.T1` )b
on a.icd_code=b.icd_code;

##############


create table `mimic-four-377221.F4_Micro2.T2_1` as

SELECT 

a.subject_id,
a.hadm_id,
a.icd_num,
a.seq_max,
a.seq_num,
a.icd_code_int,
a.icd_code_str,
a.icd_code,
a.icd_version,
a.long_title

from `mimic-four-377221.F1_NE_Disorders.T2` a
left join  `mimic-four-377221.F1_NE_Disorders.T1` b
on a.icd_code=b.icd_code
WHERE b.icd_code IS NULL 

'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
