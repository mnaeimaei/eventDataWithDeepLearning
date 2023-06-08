import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

create schema `mimic-four-377221.Q_ClusA` ;



create table `mimic-four-377221.Q_ClusA.Q1_Admissions` as
SELECT * FROM `mimic-four-377221.S_Admission.1_Admissions` ;



create table `mimic-four-377221.Q_ClusA.Q1_Patient` as
SELECT * FROM `mimic-four-377221.S_Patients.1_Patient` ;


create table `mimic-four-377221.Q_ClusA.Q1_OMR` as
SELECT * FROM `mimic-four-377221.S_OMR.1_OMR` ;


create table `mimic-four-377221.Q_ClusA.Q1_Timing` as
SELECT distinct  subject_id, hadm_id  FROM `mimic-four-377221.R_TimeT.Timing_Final` ;



'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
