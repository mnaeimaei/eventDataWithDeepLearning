import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
#print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            


create schema `mimic-four-377221.S_icd_diagnoses` ;

create table `mimic-four-377221.S_icd_diagnoses.1_icdCM` as


select
           A.subject_id,
           A.hadm_id,
           A.seq_num,
           A.icd_code,
           A.icd_version,
           B.long_title


from  `mimic-four-377221.x_mimiciv_hosp.diagnoses_icd` A
LEFT JOIN  `mimic-four-377221.x_mimiciv_hosp.d_icd_diagnoses` B
ON A.icd_code=B.icd_code


####################

'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
