import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            




##################################################################

create table `mimic-four-377221.E1_AdmSer.TabF` as

SELECT 
subject_id, hadm_id, Activity, Activity_Synonym, Timestamp, admission_location, admission_type, discharge_location ,  prev_service, curr_service
FROM `mimic-four-377221.E1_AdmSer.Tab1` 

union distinct

SELECT 
subject_id, hadm_id, Activity, Activity_Synonym, Timestamp, admission_location, admission_type, discharge_location ,  prev_service, curr_service
FROM `mimic-four-377221.E1_AdmSer.Tab2` 

union distinct

SELECT 
subject_id, hadm_id, Activity, Activity_Synonym, Timestamp, admission_location, admission_type, discharge_location ,  prev_service, curr_service
FROM `mimic-four-377221.E1_AdmSer.Tab3` 

union distinct

SELECT 
subject_id, hadm_id, Activity, Activity_Synonym, Timestamp, admission_location, admission_type, discharge_location ,  prev_service, curr_service
FROM `mimic-four-377221.E1_AdmSer.Tab4` 

union distinct

SELECT 
subject_id, hadm_id, Activity, Activity_Synonym, Timestamp, admission_location, admission_type, discharge_location ,  prev_service, curr_service
FROM `mimic-four-377221.E1_AdmSer.Tab5` 

union distinct

SELECT 
subject_id, hadm_id, Activity, Activity_Synonym, Timestamp, admission_location, admission_type, discharge_location ,  prev_service, curr_service
FROM `mimic-four-377221.E1_AdmSer.Tab6` ;

##################################################################

drop table `mimic-four-377221.E1_AdmSer.Tab1` ;
drop table `mimic-four-377221.E1_AdmSer.Tab2` ;
drop table `mimic-four-377221.E1_AdmSer.Tab3` ;
drop table `mimic-four-377221.E1_AdmSer.Tab4` ;
drop table `mimic-four-377221.E1_AdmSer.Tab5` ;
drop table `mimic-four-377221.E1_AdmSer.Tab6` ;

##################################################################




'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
