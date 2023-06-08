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
	create table `mimic-four-377221.R_TimeB.S_Time` as	
select distinct * from		
(	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table01`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table02`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table03`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table04`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table05`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table06`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table07`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table08`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table09`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table10`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table11`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table12`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table13`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table14`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table15`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table16`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table17`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table18`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table19`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table20`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table21`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table22`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table23`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table24`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table25`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table26`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table27`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table28`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table29`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table30`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table31`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table32`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table33`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table34`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table35`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table36`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table37`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table38`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table39`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table40`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table41`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table42`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table43`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table44`
)		
where Timestamp is not null	;	
		
		
###########################################################################		
	create table `mimic-four-377221.R_TimeB.S_Date` as	
select distinct * from		
(	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Date_Table01`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Date_Table02`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Date_Table03`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Date_Table04`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Date_Table05`
union all	SELECT subject_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Date_Table06`
)		
where Timestamp is not null	;	
		
###########################################################################		
	create table `mimic-four-377221.R_TimeB.SH_Time` as	
select distinct * from		
(	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table01`
union all	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table02`
union all	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table03`
union all	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table04`
union all	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table05`
union all	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table06`
union all	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table07`
union all	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table08`
union all	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table09`
union all	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table10`
union all	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table11`
union all	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table12`
union all	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table13`
union all	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table14`
union all	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table15`
union all	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table16`
union all	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table17`
union all	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table18`
union all	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table19`
union all	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table20`
union all	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table21`
union all	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table22`
union all	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table23`
union all	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table24`
union all	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table25`
union all	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table26`
union all	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table27`
union all	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table28`
union all	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table29`
union all	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table30`
union all	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table31`
union all	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table32`
union all	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table33`
union all	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table34`
union all	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table35`
union all	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table36`
union all	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table37`
union all	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table38`
union all	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table39`
union all	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table40`
union all	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table41`
union all	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table42`
union all	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table43`
union all	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table44`
)		
where Timestamp is not null	and hadm_id is not null;	
		
###########################################################################		
	create table `mimic-four-377221.R_TimeB.SH_Date` as	
select distinct * from		
(	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Date_Table01`
union all	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Date_Table02`
union all	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Date_Table04`
union all	SELECT subject_id, hadm_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Date_Table06`
)		
where Timestamp is not null	and hadm_id is not null;	
		
###########################################################################		
	create table `mimic-four-377221.R_TimeB.SHI_Time` as	
select distinct * from		
(	SELECT subject_id, hadm_id, stay_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table11`
union all	SELECT subject_id, hadm_id, stay_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table12`
union all	SELECT subject_id, hadm_id, stay_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table13`
union all	SELECT subject_id, hadm_id, stay_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table14`
union all	SELECT subject_id, hadm_id, stay_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table15`
union all	SELECT subject_id, hadm_id, stay_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table19`
union all	SELECT subject_id, hadm_id, stay_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table20`
union all	SELECT subject_id, hadm_id, stay_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table21`
union all	SELECT subject_id, hadm_id, stay_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table22`
union all	SELECT subject_id, hadm_id, stay_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table23`
union all	SELECT subject_id, hadm_id, stay_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table24`
union all	SELECT subject_id, hadm_id, stay_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table25`
union all	SELECT subject_id, hadm_id, stay_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table26`
union all	SELECT subject_id, hadm_id, stay_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table33`
union all	SELECT subject_id, hadm_id, stay_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table34`
union all	SELECT subject_id, hadm_id, stay_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table42`
union all	SELECT subject_id, hadm_id, stay_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table43`
union all	SELECT subject_id, hadm_id, stay_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table44`
)		
where Timestamp is not null	;	
		
###########################################################################		
	create table `mimic-four-377221.R_TimeB.SHI_Date` as	
select distinct * from		
(	SELECT subject_id, hadm_id, stay_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Date_Table05`
)		
where Timestamp is not null	;	
		
###########################################################################		
	create table `mimic-four-377221.R_TimeB.SHT_Time` as	
select distinct * from		
(	SELECT subject_id, hadm_id, transfer_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table09`
where Timestamp is not null and hadm_id is not null	
union all	SELECT subject_id, hadm_id, transfer_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table10`
where Timestamp is not null and hadm_id is not null	
)		;
	
		
###########################################################################		
	create table `mimic-four-377221.R_TimeB.ST_Time` as	
select distinct * from		
(	SELECT subject_id, transfer_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table09`
where Timestamp is not null and hadm_id is null	
union all	SELECT subject_id, transfer_id, Timestamp, Title FROM	`mimic-four-377221.R_TimeA.Time_Table10`
where Timestamp is not null and hadm_id is null	
)		;	


'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
