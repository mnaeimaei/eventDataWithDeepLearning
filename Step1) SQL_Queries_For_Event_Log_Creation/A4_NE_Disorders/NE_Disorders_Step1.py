import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            


create schema `mimic-four-377221.P_NonEvents` ;



create table `mimic-four-377221.P_NonEvents.DRG1` as
SELECT * FROM `mimic-four-377221.S_DRG.1_DRG` ;


create table `mimic-four-377221.P_NonEvents.Provider1` as
SELECT * FROM `mimic-four-377221.S_Providers.1_Provider`; 

create table `mimic-four-377221.P_NonEvents.icdCM1` as
SELECT * FROM `mimic-four-377221.S_icd_diagnoses.1_icdCM`; 


create table `mimic-four-377221.P_NonEvents.icdPCM1` as
SELECT * FROM `mimic-four-377221.S_icd_procedures.1_icdPCM`; 

create table `mimic-four-377221.P_NonEvents.Caregiver1` as
SELECT * FROM `mimic-four-377221.S_Caregivers.1_Caregiver` ;

create table `mimic-four-377221.P_NonEvents.cptEvents1` as
SELECT * FROM `mimic-four-377221.S_cptEvent.1_cptEvents`  ;

'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
