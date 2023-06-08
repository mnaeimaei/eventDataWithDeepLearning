import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            


######################################################################


create table `mimic-four-377221.E1_AdmSer.Tab1` as
SELECT subject_id, hadm_id, edregtime as Timestamp
FROM `mimic-four-377221.E1_AdmSer.AdmSer1` ;


alter table `mimic-four-377221.E1_AdmSer.Tab1` 
add column Activity string;

alter table `mimic-four-377221.E1_AdmSer.Tab1` 
add column Activity_Synonym string;

update  `mimic-four-377221.E1_AdmSer.Tab1` 
set Activity="Reg_from_ED"
where Activity is null;

update  `mimic-four-377221.E1_AdmSer.Tab1` 
set Activity_Synonym="RFE"
where Activity_Synonym is null;


######################################################################

create table `mimic-four-377221.E1_AdmSer.Tab2` as
SELECT subject_id, hadm_id, admittime as Timestamp, admission_location, admission_type
FROM `mimic-four-377221.E1_AdmSer.AdmSer1` ;


alter table `mimic-four-377221.E1_AdmSer.Tab2` 
add column Activity string;

alter table `mimic-four-377221.E1_AdmSer.Tab2` 
add column Activity_Synonym string;

update  `mimic-four-377221.E1_AdmSer.Tab2` 
set Activity="Hospital_Admission"
where Activity is null;

update  `mimic-four-377221.E1_AdmSer.Tab2` 
set Activity_Synonym="HA"
where Activity_Synonym is null;


######################################################################
create table `mimic-four-377221.E1_AdmSer.Tab3` as
SELECT subject_id, hadm_id, edouttime as Timestamp
FROM `mimic-four-377221.E1_AdmSer.AdmSer1` ;


alter table `mimic-four-377221.E1_AdmSer.Tab3` 
add column Activity string;

alter table `mimic-four-377221.E1_AdmSer.Tab3` 
add column Activity_Synonym string;

update  `mimic-four-377221.E1_AdmSer.Tab3` 
set Activity="Discharging_from_ED"
where Activity is null;

update  `mimic-four-377221.E1_AdmSer.Tab3` 
set Activity_Synonym="DFE"
where Activity_Synonym is null;


######################################################################
create table `mimic-four-377221.E1_AdmSer.Tab4` as
SELECT subject_id, hadm_id, dischtime  as Timestamp, discharge_location
FROM `mimic-four-377221.E1_AdmSer.AdmSer1` 
where hospital_expire_flag=0;

alter table `mimic-four-377221.E1_AdmSer.Tab4` 
add column Activity string;

alter table `mimic-four-377221.E1_AdmSer.Tab4` 
add column Activity_Synonym string;

update  `mimic-four-377221.E1_AdmSer.Tab4` 
set Activity="Discharging_from_Hospital"
where Activity is null;

update  `mimic-four-377221.E1_AdmSer.Tab4` 
set Activity_Synonym="DFH"
where Activity_Synonym is null;


######################################################################
create table `mimic-four-377221.E1_AdmSer.Tab5` as
SELECT subject_id, hadm_id, deathtime  as Timestamp, discharge_location
FROM `mimic-four-377221.E1_AdmSer.AdmSer1` 
where hospital_expire_flag=1;


alter table `mimic-four-377221.E1_AdmSer.Tab5` 
add column Activity string;

alter table `mimic-four-377221.E1_AdmSer.Tab5` 
add column Activity_Synonym string;

update  `mimic-four-377221.E1_AdmSer.Tab5` 
set Activity="Dying_in_hospital"
where Activity is null;

update  `mimic-four-377221.E1_AdmSer.Tab5` 
set Activity_Synonym="DIH"
where Activity_Synonym is null;


######################################################################
create table `mimic-four-377221.E1_AdmSer.Tab6` as
SELECT subject_id, hadm_id, transfertime  as Timestamp, prev_service, curr_service
FROM `mimic-four-377221.E1_AdmSer.AdmSer2` ;


alter table `mimic-four-377221.E1_AdmSer.Tab6` 
add column Activity string;

alter table `mimic-four-377221.E1_AdmSer.Tab6` 
add column Activity_Synonym string;

update  `mimic-four-377221.E1_AdmSer.Tab6` 
set Activity="Transfering_btw_services"
where Activity is null;

update  `mimic-four-377221.E1_AdmSer.Tab6` 
set Activity_Synonym="TBS"
where Activity_Synonym is null;


######################################################################






'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
