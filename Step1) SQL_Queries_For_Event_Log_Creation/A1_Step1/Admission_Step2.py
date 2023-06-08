import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
#print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            


create table `mimic-four-377221.S_Admission.2_Admissions` as
    select
           subject_id,
           hadm_id,
           edregtime,
           admission_location,
           admission_type,
           admit_provider_id,
           admittime,
           edouttime,
           hospital_expire_flag,
           dischtime,
           deathtime,         
           discharge_location

from  `mimic-four-377221.x_mimiciv_hosp.admissions` 


'''


QUERY = (query1)


query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)

















