import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            
        create schema `mimic-four-377221.C0_Disorders` ;

create table `mimic-four-377221.C0_Disorders.D1` as
SELECT * FROM `mimic-four-377221.D7_ABG.Disorders_ABG` 
union all
SELECT * FROM `mimic-four-377221.D6_CMP.Disorders_CMP` 
union all
SELECT * FROM `mimic-four-377221.D8_Specimen.Disorders_Specimen` 
union all
SELECT * FROM `mimic-four-377221.D5_RT.Disorders_RT` 
union all
SELECT * FROM `mimic-four-377221.D4_MicroB.Disorders_MicroB`
union all
SELECT * FROM `mimic-four-377221.D3_MicroA.Disorders_MicroA`
union all
SELECT * FROM  `mimic-four-377221.D2_Transfer.Disorders_Transfer` 
union all
SELECT * FROM  `mimic-four-377221.D1_AdmSer.Disorders_AdmSer`



'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
