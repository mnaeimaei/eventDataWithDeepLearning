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

create table `mimic-four-377221.R_TimeA.Time_Table01` as
SELECT subject_id, hadm_id, edregtime as Timestamp
FROM `mimic-four-377221.S_Admission.2_Admissions` ;

alter table `mimic-four-377221.R_TimeA.Time_Table01` 
add column Title String;

update `mimic-four-377221.R_TimeA.Time_Table01` 
set Title="Admissions_edregtime"
where Title is null;

######################################################

create table `mimic-four-377221.R_TimeA.Time_Table02` as
SELECT subject_id, hadm_id, admittime as Timestamp
FROM `mimic-four-377221.S_Admission.2_Admissions` ;

alter table `mimic-four-377221.R_TimeA.Time_Table02` 
add column Title String;

update `mimic-four-377221.R_TimeA.Time_Table02` 
set Title="Admissions_admittime"
where Title is null;


######################################################

create table `mimic-four-377221.R_TimeA.Time_Table03` as
SELECT subject_id, hadm_id, edouttime as Timestamp
FROM `mimic-four-377221.S_Admission.2_Admissions` ;

alter table `mimic-four-377221.R_TimeA.Time_Table03` 
add column Title String;

update `mimic-four-377221.R_TimeA.Time_Table03` 
set Title="Admissions_edouttime"
where Title is null;

######################################################

create table `mimic-four-377221.R_TimeA.Time_Table04` as
SELECT subject_id, hadm_id, dischtime as Timestamp
FROM `mimic-four-377221.S_Admission.2_Admissions` ;

alter table `mimic-four-377221.R_TimeA.Time_Table04` 
add column Title String;

update `mimic-four-377221.R_TimeA.Time_Table04` 
set Title="Admissions_dischtime"
where Title is null;

######################################################

create table `mimic-four-377221.R_TimeA.Time_Table05` as
SELECT subject_id, hadm_id, deathtime as Timestamp
FROM `mimic-four-377221.S_Admission.2_Admissions` ;

alter table `mimic-four-377221.R_TimeA.Time_Table05` 
add column Title String;

update `mimic-four-377221.R_TimeA.Time_Table05` 
set Title="Admissions_deathtime"
where Title is null;

######################################################

create table `mimic-four-377221.R_TimeA.Time_Table06` as
SELECT subject_id, hadm_id, charttime as Timestamp
FROM `mimic-four-377221.S_Microbiology.1_Microbiology` ;

alter table `mimic-four-377221.R_TimeA.Time_Table06` 
add column Title String;

update `mimic-four-377221.R_TimeA.Time_Table06` 
set Title="Microbiology_charttime"
where Title is null;



######################################################

create table `mimic-four-377221.R_TimeA.Time_Table07` as
SELECT subject_id, hadm_id, storetime as Timestamp
FROM `mimic-four-377221.S_Microbiology.1_Microbiology` ;

alter table `mimic-four-377221.R_TimeA.Time_Table07` 
add column Title String;

update `mimic-four-377221.R_TimeA.Time_Table07` 
set Title="Microbiology_storetime"
where Title is null;


######################################################

create table `mimic-four-377221.R_TimeA.Time_Table08` as
SELECT subject_id, hadm_id, transfertime as Timestamp
FROM `mimic-four-377221.S_Services.1_Service` ;

alter table `mimic-four-377221.R_TimeA.Time_Table08` 
add column Title String;

update `mimic-four-377221.R_TimeA.Time_Table08` 
set Title="Service_transfertime"
where Title is null;


######################################################

create table `mimic-four-377221.R_TimeA.Time_Table09` as
SELECT subject_id, hadm_id, transfer_id, intime as Timestamp 
FROM `mimic-four-377221.S_Transfers.1_Transfer` ;

alter table `mimic-four-377221.R_TimeA.Time_Table09` 
add column Title String;

update `mimic-four-377221.R_TimeA.Time_Table09` 
set Title="Transfer_intime"
where Title is null;


######################################################

create table `mimic-four-377221.R_TimeA.Time_Table10` as
SELECT subject_id, hadm_id, transfer_id, outtime as Timestamp 
FROM `mimic-four-377221.S_Transfers.1_Transfer` ;

alter table `mimic-four-377221.R_TimeA.Time_Table10` 
add column Title String;

update `mimic-four-377221.R_TimeA.Time_Table10` 
set Title="Transfer_outtime"
where Title is null;

######################################################

create table `mimic-four-377221.R_TimeA.Time_Table11` as
SELECT subject_id, hadm_id, stay_id, charttime as Timestamp 
FROM `mimic-four-377221.S_chartEvents.1_chartEvent` ;

alter table `mimic-four-377221.R_TimeA.Time_Table11` 
add column Title String;

update `mimic-four-377221.R_TimeA.Time_Table11` 
set Title="chartEvent_charttime"
where Title is null;


######################################################################


create table `mimic-four-377221.R_TimeA.Time_Table12` as
SELECT subject_id, hadm_id, stay_id, storetime as Timestamp 
FROM `mimic-four-377221.S_chartEvents.1_chartEvent` ;

alter table `mimic-four-377221.R_TimeA.Time_Table12` 
add column Title String;

update `mimic-four-377221.R_TimeA.Time_Table12` 
set Title="chartEvent_storetime"
where Title is null;


######################################################

create table `mimic-four-377221.R_TimeA.Time_Table13` as
SELECT subject_id, hadm_id, stay_id, charttime as Timestamp 
FROM `mimic-four-377221.S_datetimeEvents.1_datetimeEvent` ;

alter table `mimic-four-377221.R_TimeA.Time_Table13` 
add column Title String;

update `mimic-four-377221.R_TimeA.Time_Table13` 
set Title="datetimeEvent_charttime"
where Title is null;

######################################################################



create table `mimic-four-377221.R_TimeA.Time_Table14` as
SELECT subject_id, hadm_id, stay_id, storetime as Timestamp 
FROM `mimic-four-377221.S_datetimeEvents.1_datetimeEvent` ;

alter table `mimic-four-377221.R_TimeA.Time_Table14` 
add column Title String;

update `mimic-four-377221.R_TimeA.Time_Table14` 
set Title="datetimeEvent_storetime"
where Title is null;

######################################################################


create table `mimic-four-377221.R_TimeA.Time_Table15` as
SELECT subject_id, hadm_id, stay_id, value as Timestamp 
FROM `mimic-four-377221.S_datetimeEvents.1_datetimeEvent` 
where valueuom="Date and Time";

alter table `mimic-four-377221.R_TimeA.Time_Table15` 
add column Title String;

update `mimic-four-377221.R_TimeA.Time_Table15` 
set Title="datetimeEvent_value"
where Title is null;

######################################################################




create table `mimic-four-377221.R_TimeA.Time_Table16` as
SELECT subject_id, hadm_id, charttime as Timestamp 
FROM `mimic-four-377221.S_eMAR.1_eMAR` ;


alter table `mimic-four-377221.R_TimeA.Time_Table16` 
add column Title String;

update `mimic-four-377221.R_TimeA.Time_Table16` 
set Title="eMAR_charttime"
where Title is null;

######################################################################

create table `mimic-four-377221.R_TimeA.Time_Table17` as
SELECT subject_id, hadm_id, scheduletime as Timestamp 
FROM `mimic-four-377221.S_eMAR.1_eMAR` ;


alter table `mimic-four-377221.R_TimeA.Time_Table17` 
add column Title String;

update `mimic-four-377221.R_TimeA.Time_Table17` 
set Title="eMAR_scheduletime"
where Title is null;


######################################################################

create table `mimic-four-377221.R_TimeA.Time_Table18` as
SELECT subject_id, hadm_id, storetime as Timestamp 
FROM `mimic-four-377221.S_eMAR.1_eMAR` ;


alter table `mimic-four-377221.R_TimeA.Time_Table18` 
add column Title String;

update `mimic-four-377221.R_TimeA.Time_Table18` 
set Title="eMAR_storetime"
where Title is null;


######################################################

create table `mimic-four-377221.R_TimeA.Time_Table19` as
SELECT subject_id, hadm_id,stay_id, intime as Timestamp 
FROM `mimic-four-377221.S_icuStays.1_icuStays` ;


alter table `mimic-four-377221.R_TimeA.Time_Table19` 
add column Title String;

update `mimic-four-377221.R_TimeA.Time_Table19` 
set Title="icuStays_intime"
where Title is null;


######################################################
create table `mimic-four-377221.R_TimeA.Time_Table20` as
SELECT subject_id, hadm_id,stay_id, outtime as Timestamp 
FROM `mimic-four-377221.S_icuStays.1_icuStays` ;


alter table `mimic-four-377221.R_TimeA.Time_Table20` 
add column Title String;

update `mimic-four-377221.R_TimeA.Time_Table20` 
set Title="icuStays_outtime"
where Title is null;

######################################################

create table `mimic-four-377221.R_TimeA.Time_Table21` as
SELECT subject_id, hadm_id,stay_id, starttime as Timestamp 
FROM `mimic-four-377221.S_ingredientEvents.1_ingredientEvent` ;


alter table `mimic-four-377221.R_TimeA.Time_Table21` 
add column Title String;

update `mimic-four-377221.R_TimeA.Time_Table21` 
set Title="ingredientEvent_starttime"
where Title is null;

########################################################

create table `mimic-four-377221.R_TimeA.Time_Table22` as
SELECT subject_id, hadm_id,stay_id, endtime as Timestamp 
FROM `mimic-four-377221.S_ingredientEvents.1_ingredientEvent` ;


alter table `mimic-four-377221.R_TimeA.Time_Table22` 
add column Title String;

update `mimic-four-377221.R_TimeA.Time_Table22` 
set Title="ingredientEvent_endtime"
where Title is null;

########################################################


create table `mimic-four-377221.R_TimeA.Time_Table23` as
SELECT subject_id, hadm_id,stay_id, storetime as Timestamp 
FROM `mimic-four-377221.S_ingredientEvents.1_ingredientEvent` ;


alter table `mimic-four-377221.R_TimeA.Time_Table23` 
add column Title String;

update `mimic-four-377221.R_TimeA.Time_Table23` 
set Title="ingredientEvent_storetime"
where Title is null;

########################################################

create table `mimic-four-377221.R_TimeA.Time_Table24` as
SELECT subject_id, hadm_id,stay_id, starttime as Timestamp 
FROM `mimic-four-377221.S_inputEvents.1_inputEvent` ;


alter table `mimic-four-377221.R_TimeA.Time_Table24` 
add column Title String;

update `mimic-four-377221.R_TimeA.Time_Table24` 
set Title="inputEvent_starttime"
where Title is null;

########################################################

create table `mimic-four-377221.R_TimeA.Time_Table25` as
SELECT subject_id, hadm_id,stay_id, endtime as Timestamp 
FROM `mimic-four-377221.S_inputEvents.1_inputEvent` ;


alter table `mimic-four-377221.R_TimeA.Time_Table25` 
add column Title String;

update `mimic-four-377221.R_TimeA.Time_Table25` 
set Title="inputEvent_endtime"
where Title is null;

########################################################


create table `mimic-four-377221.R_TimeA.Time_Table26` as
SELECT subject_id, hadm_id,stay_id, storetime as Timestamp 
FROM `mimic-four-377221.S_inputEvents.1_inputEvent` ;


alter table `mimic-four-377221.R_TimeA.Time_Table26` 
add column Title String;

update `mimic-four-377221.R_TimeA.Time_Table26` 
set Title="inputEvent_storetime"
where Title is null;

########################################################

create table `mimic-four-377221.R_TimeA.Time_Table27` as
SELECT subject_id, hadm_id, charttime as Timestamp 
FROM `mimic-four-377221.S_labEvents.2_Blood_Gas` ;


alter table `mimic-four-377221.R_TimeA.Time_Table27` 
add column Title String;

update `mimic-four-377221.R_TimeA.Time_Table27` 
set Title="Blood_Gas_charttime"
where Title is null;

########################################################

create table `mimic-four-377221.R_TimeA.Time_Table28` as
SELECT subject_id, hadm_id, storetime as Timestamp 
FROM `mimic-four-377221.S_labEvents.2_Blood_Gas` ;


alter table `mimic-four-377221.R_TimeA.Time_Table28` 
add column Title String;

update `mimic-four-377221.R_TimeA.Time_Table28` 
set Title="Blood_Gas_storetime"
where Title is null;

########################################################

create table `mimic-four-377221.R_TimeA.Time_Table29` as
SELECT subject_id, hadm_id, charttime as Timestamp 
FROM `mimic-four-377221.S_labEvents.2_Chemistry` ;


alter table `mimic-four-377221.R_TimeA.Time_Table29` 
add column Title String;

update `mimic-four-377221.R_TimeA.Time_Table29` 
set Title="Chemistry_charttime"
where Title is null;

########################################################

create table `mimic-four-377221.R_TimeA.Time_Table30` as
SELECT subject_id, hadm_id, storetime as Timestamp 
FROM `mimic-four-377221.S_labEvents.2_Chemistry` ;


alter table `mimic-four-377221.R_TimeA.Time_Table30` 
add column Title String;

update `mimic-four-377221.R_TimeA.Time_Table30` 
set Title="Chemistry_storetime"
where Title is null;

########################################################



create table `mimic-four-377221.R_TimeA.Time_Table31` as
SELECT subject_id, hadm_id, charttime as Timestamp 
FROM `mimic-four-377221.S_labEvents.2_Hematology` ;


alter table `mimic-four-377221.R_TimeA.Time_Table31` 
add column Title String;

update `mimic-four-377221.R_TimeA.Time_Table31` 
set Title="Hematology_charttime"
where Title is null;

########################################################

create table `mimic-four-377221.R_TimeA.Time_Table32` as
SELECT subject_id, hadm_id, storetime as Timestamp 
FROM `mimic-four-377221.S_labEvents.2_Hematology` ;


alter table `mimic-four-377221.R_TimeA.Time_Table32` 
add column Title String;

update `mimic-four-377221.R_TimeA.Time_Table32` 
set Title="Hematology_storetime"
where Title is null;

########################################################

create table `mimic-four-377221.R_TimeA.Time_Table33` as
SELECT subject_id, hadm_id, stay_id, charttime as Timestamp 
FROM `mimic-four-377221.S_outputEvents.1_outputEvent` ;


alter table `mimic-four-377221.R_TimeA.Time_Table33` 
add column Title String;

update `mimic-four-377221.R_TimeA.Time_Table33` 
set Title="outputEvent_charttime"
where Title is null;

######################################################################################


create table `mimic-four-377221.R_TimeA.Time_Table34` as
SELECT subject_id, hadm_id, stay_id, storetime as Timestamp 
FROM `mimic-four-377221.S_outputEvents.1_outputEvent` ;


alter table `mimic-four-377221.R_TimeA.Time_Table34` 
add column Title String;

update `mimic-four-377221.R_TimeA.Time_Table34` 
set Title="outputEvent_storetime"
where Title is null;


######################################################

create table `mimic-four-377221.R_TimeA.Time_Table35` as
SELECT subject_id, hadm_id, starttime as Timestamp 
FROM `mimic-four-377221.S_pharmacy.1_pharmacy` ;


alter table `mimic-four-377221.R_TimeA.Time_Table35` 
add column Title String;

update `mimic-four-377221.R_TimeA.Time_Table35` 
set Title="pharmacy_starttime"
where Title is null;

######################################################################################

create table `mimic-four-377221.R_TimeA.Time_Table36` as
SELECT subject_id, hadm_id, stoptime as Timestamp 
FROM `mimic-four-377221.S_pharmacy.1_pharmacy` ;


alter table `mimic-four-377221.R_TimeA.Time_Table36` 
add column Title String;

update `mimic-four-377221.R_TimeA.Time_Table36` 
set Title="pharmacy_stoptime"
where Title is null;





######################################################################################


create table `mimic-four-377221.R_TimeA.Time_Table37` as
SELECT subject_id, hadm_id, entertime as Timestamp 
FROM `mimic-four-377221.S_pharmacy.1_pharmacy` ;


alter table `mimic-four-377221.R_TimeA.Time_Table37` 
add column Title String;

update `mimic-four-377221.R_TimeA.Time_Table37` 
set Title="pharmacy_entertime"
where Title is null;

######################################################################################

create table `mimic-four-377221.R_TimeA.Time_Table38` as
SELECT subject_id, hadm_id, verifiedtime as Timestamp 
FROM `mimic-four-377221.S_pharmacy.1_pharmacy` ;


alter table `mimic-four-377221.R_TimeA.Time_Table38` 
add column Title String;

update `mimic-four-377221.R_TimeA.Time_Table38` 
set Title="pharmacy_verifiedtime"
where Title is null;


######################################################################################
create table `mimic-four-377221.R_TimeA.Time_Table39` as
SELECT subject_id, hadm_id, ordertime as Timestamp 
FROM `mimic-four-377221.S_poe.1_POE` ;


alter table `mimic-four-377221.R_TimeA.Time_Table39` 
add column Title String;

update `mimic-four-377221.R_TimeA.Time_Table39` 
set Title="poe_ordertime"
where Title is null;


######################################################

create table `mimic-four-377221.R_TimeA.Time_Table40` as
SELECT subject_id, hadm_id, starttime as Timestamp 
FROM `mimic-four-377221.S_prescriptions.1_prescriptions` ;


alter table `mimic-four-377221.R_TimeA.Time_Table40` 
add column Title String;

update `mimic-four-377221.R_TimeA.Time_Table40` 
set Title="prescription_starttime"
where Title is null;

######################################################################################

create table `mimic-four-377221.R_TimeA.Time_Table41` as
SELECT subject_id, hadm_id, stoptime as Timestamp 
FROM `mimic-four-377221.S_prescriptions.1_prescriptions` ;


alter table `mimic-four-377221.R_TimeA.Time_Table41` 
add column Title String;

update `mimic-four-377221.R_TimeA.Time_Table41` 
set Title="prescription_stoptime"
where Title is null;

######################################################

create table `mimic-four-377221.R_TimeA.Time_Table42` as
SELECT subject_id, hadm_id,stay_id, starttime as Timestamp 
FROM `mimic-four-377221.S_procedureEvents.1_procedureEvent` ;


alter table `mimic-four-377221.R_TimeA.Time_Table42` 
add column Title String;

update `mimic-four-377221.R_TimeA.Time_Table42` 
set Title="procedureEvent_starttime"
where Title is null;

######################################################################################

create table `mimic-four-377221.R_TimeA.Time_Table43` as
SELECT subject_id, hadm_id,stay_id, endtime as Timestamp 
FROM `mimic-four-377221.S_procedureEvents.1_procedureEvent` ;


alter table `mimic-four-377221.R_TimeA.Time_Table43` 
add column Title String;

update `mimic-four-377221.R_TimeA.Time_Table43` 
set Title="procedureEvent_endtime"
where Title is null;



######################################################################################


create table `mimic-four-377221.R_TimeA.Time_Table44` as
SELECT subject_id, hadm_id,stay_id, storetime as Timestamp 
FROM `mimic-four-377221.S_procedureEvents.1_procedureEvent` ;


alter table `mimic-four-377221.R_TimeA.Time_Table44` 
add column Title String;

update `mimic-four-377221.R_TimeA.Time_Table44` 
set Title="procedureEvent_storetime"
where Title is null;

######################################################





'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
