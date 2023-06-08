#Should be done in Google BQ

#STEP1
#Create Two Database


query1 = f'''            

create schema `mimic-four-377221.x_mimiciv_hosp` ;
create schema `mimic-four-377221.x_mimiciv_icu` ;

'''

#Step2
#Using These Query
query2 = f'''            

create table  `mimic-four-377221.x_mimiciv_hosp.admissions` as	SELECT * FROM `physionet-data.mimiciv_hosp.admissions` 				;
create table  `mimic-four-377221.x_mimiciv_hosp.d_hcpcs` as	SELECT * FROM `physionet-data.mimiciv_hosp.d_hcpcs` 				;
create table  `mimic-four-377221.x_mimiciv_hosp.d_icd_diagnoses` as	SELECT * FROM `physionet-data.mimiciv_hosp.d_icd_diagnoses` 				;
create table  `mimic-four-377221.x_mimiciv_hosp.d_icd_procedures` as	SELECT * FROM `physionet-data.mimiciv_hosp.d_icd_procedures` 				;
create table  `mimic-four-377221.x_mimiciv_hosp.d_labitems` as	SELECT * FROM `physionet-data.mimiciv_hosp.d_labitems` 				;
create table  `mimic-four-377221.x_mimiciv_hosp.diagnoses_icd` as	SELECT * FROM `physionet-data.mimiciv_hosp.diagnoses_icd` 				;
create table  `mimic-four-377221.x_mimiciv_hosp.drgcodes` as	SELECT * FROM `physionet-data.mimiciv_hosp.drgcodes` 				;
create table  `mimic-four-377221.x_mimiciv_hosp.emar` as	SELECT * FROM `physionet-data.mimiciv_hosp.emar` 				;
create table  `mimic-four-377221.x_mimiciv_hosp.emar_detail` as	SELECT * FROM `physionet-data.mimiciv_hosp.emar_detail` 				;
create table  `mimic-four-377221.x_mimiciv_hosp.hcpcsevents` as	SELECT * FROM `physionet-data.mimiciv_hosp.hcpcsevents` 				;
create table  `mimic-four-377221.x_mimiciv_hosp.labevents` as	SELECT * FROM `physionet-data.mimiciv_hosp.labevents` 				;
create table  `mimic-four-377221.x_mimiciv_hosp.microbiologyevents` as	SELECT * FROM `physionet-data.mimiciv_hosp.microbiologyevents` 				;
create table  `mimic-four-377221.x_mimiciv_hosp.omr` as	SELECT * FROM `physionet-data.mimiciv_hosp.omr` 				;
create table  `mimic-four-377221.x_mimiciv_hosp.patients` as	SELECT * FROM `physionet-data.mimiciv_hosp.patients` 				;
create table  `mimic-four-377221.x_mimiciv_hosp.pharmacy` as	SELECT * FROM `physionet-data.mimiciv_hosp.pharmacy` 				;
create table  `mimic-four-377221.x_mimiciv_hosp.poe` as	SELECT * FROM `physionet-data.mimiciv_hosp.poe` 				;
create table  `mimic-four-377221.x_mimiciv_hosp.poe_detail` as	SELECT * FROM `physionet-data.mimiciv_hosp.poe_detail` 				;
create table  `mimic-four-377221.x_mimiciv_hosp.prescriptions` as	SELECT * FROM `physionet-data.mimiciv_hosp.prescriptions` 				;
create table  `mimic-four-377221.x_mimiciv_hosp.procedures_icd` as	SELECT * FROM `physionet-data.mimiciv_hosp.procedures_icd` 				;
create table  `mimic-four-377221.x_mimiciv_hosp.provider` as	SELECT * FROM `physionet-data.mimiciv_hosp.provider` 				;
create table  `mimic-four-377221.x_mimiciv_hosp.services` as	SELECT * FROM `physionet-data.mimiciv_hosp.services` 				;
create table  `mimic-four-377221.x_mimiciv_hosp.transfers` as	SELECT * FROM `physionet-data.mimiciv_hosp.transfers` 				;
					
create table  `mimic-four-377221.x_mimiciv_icu.caregiver` as	SELECT * FROM `physionet-data.mimiciv_icu.caregiver` 				;
create table  `mimic-four-377221.x_mimiciv_icu.chartevents` as	SELECT * FROM `physionet-data.mimiciv_icu.chartevents` 				;
create table  `mimic-four-377221.x_mimiciv_icu.d_items` as	SELECT * FROM `physionet-data.mimiciv_icu.d_items` 				;
create table  `mimic-four-377221.x_mimiciv_icu.datetimeevents` as	SELECT * FROM `physionet-data.mimiciv_icu.datetimeevents` 				;
create table  `mimic-four-377221.x_mimiciv_icu.icustays` as	SELECT * FROM `physionet-data.mimiciv_icu.icustays` 				;
create table  `mimic-four-377221.x_mimiciv_icu.ingredientevents` as	SELECT * FROM `physionet-data.mimiciv_icu.ingredientevents` 				;
create table  `mimic-four-377221.x_mimiciv_icu.inputevents` as	SELECT * FROM `physionet-data.mimiciv_icu.inputevents` 				;
create table  `mimic-four-377221.x_mimiciv_icu.outputevents` as	SELECT * FROM `physionet-data.mimiciv_icu.outputevents` 				;
create table  `mimic-four-377221.x_mimiciv_icu.procedureevents` as	SELECT * FROM `physionet-data.mimiciv_icu.procedureevents` 				;

'''