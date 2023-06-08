import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

###########################################################################

create table  `mimic-four-377221.R_TimeF.F_S` as

SELECT distinct
subject_id, min, max
FROM `mimic-four-377221.R_TimeE.E_S` ;


###########################################################################

create table  `mimic-four-377221.R_TimeF.F_SH` as

SELECT distinct
subject_id, hadm_id, min, max
FROM `mimic-four-377221.R_TimeE.E_SH` ;

###########################################################################

create table  `mimic-four-377221.R_TimeF.F_SHI` as

SELECT distinct
subject_id, hadm_id, stay_id, min, max
FROM `mimic-four-377221.R_TimeE.E_SHI` ;

###########################################################################

create table  `mimic-four-377221.R_TimeF.F_SHT` as

SELECT distinct
subject_id, hadm_id, transfer_id, mini as min, maxi as max
FROM `mimic-four-377221.R_TimeE.E_SHT` ;

###########################################################################

create table  `mimic-four-377221.R_TimeF.F_ST` as

SELECT distinct
subject_id, transfer_id, mini as min, maxi as max
FROM `mimic-four-377221.R_TimeE.E_ST` ;

###########################################################################




'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
