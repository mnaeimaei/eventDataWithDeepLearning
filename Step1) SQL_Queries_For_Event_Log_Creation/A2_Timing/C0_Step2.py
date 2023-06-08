import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            


######################################################

create table `mimic-four-377221.R_TimeA.Date_Table01` as
SELECT subject_id, hadm_id, chartdate as Timestamp
FROM `mimic-four-377221.S_Microbiology.1_Microbiology` 
where charttime is null;

alter table `mimic-four-377221.R_TimeA.Date_Table01` 
add column Title String;

update `mimic-four-377221.R_TimeA.Date_Table01` 
set Title="Microbiology_chartdate"
where Title is null;

######################################################

create table `mimic-four-377221.R_TimeA.Date_Table02` as
SELECT subject_id, hadm_id, storedate as Timestamp
FROM `mimic-four-377221.S_Microbiology.1_Microbiology` 
where storetime is null;


alter table `mimic-four-377221.R_TimeA.Date_Table02` 
add column Title String;

update `mimic-four-377221.R_TimeA.Date_Table02` 
set Title="Microbiology_storedate"
where Title is null;

######################################################

create table `mimic-four-377221.R_TimeA.Date_Table03` as
SELECT subject_id, CAST(chartdate AS datetime) as Timestamp
FROM `mimic-four-377221.S_OMR.1_OMR` ;

alter table `mimic-four-377221.R_TimeA.Date_Table03` 
add column Title String;

update `mimic-four-377221.R_TimeA.Date_Table03` 
set Title="OMR"
where Title is null;

######################################################


create table `mimic-four-377221.R_TimeA.Date_Table04` as
SELECT subject_id, hadm_id, CAST(chartdate AS datetime) as Timestamp 
FROM `mimic-four-377221.S_cptEvent.1_cptEvents` ;

alter table `mimic-four-377221.R_TimeA.Date_Table04` 
add column Title String;

update `mimic-four-377221.R_TimeA.Date_Table04` 
set Title="cptEvent_chartdate"
where Title is null;

######################################################

create table `mimic-four-377221.R_TimeA.Date_Table05` as
SELECT subject_id, hadm_id, stay_id, value as Timestamp 
FROM `mimic-four-377221.S_datetimeEvents.1_datetimeEvent` 
where valueuom="Date";

alter table `mimic-four-377221.R_TimeA.Date_Table05` 
add column Title String;

update `mimic-four-377221.R_TimeA.Date_Table05` 
set Title="datetimeEvent_value"
where Title is null;

######################################################

create table `mimic-four-377221.R_TimeA.Date_Table06` as
SELECT subject_id, hadm_id, CAST(chartdate AS datetime) as Timestamp 
FROM `mimic-four-377221.S_icd_procedures.1_icdPCM` ;

alter table `mimic-four-377221.R_TimeA.Date_Table06` 
add column Title String;

update `mimic-four-377221.R_TimeA.Date_Table06` 
set Title="icdPCM_chartdate"
where Title is null;


######################################################


'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
