import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
#print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

create schema `mimic-four-377221.S_cptEvent` ;

create table `mimic-four-377221.S_cptEvent.1_cptEvents` as

select
           A.subject_id,
           A.hadm_id,
           A.chartdate,
           A.seq_num,
           A.hcpcs_cd,
           A.short_description,
           B.long_description,
           B.category,


from  `mimic-four-377221.x_mimiciv_hosp.hcpcsevents` A
LEFT JOIN  `mimic-four-377221.x_mimiciv_hosp.d_hcpcs` B
ON A.hcpcs_cd=B.code


####################

'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
