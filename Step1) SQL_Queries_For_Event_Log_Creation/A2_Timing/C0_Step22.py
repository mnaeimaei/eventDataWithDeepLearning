import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

#######################################################

update `mimic-four-377221.R_TimeH.H_SHIT` 
set stay_id=99
where stay_id is null;

#######################################################

CREATE TABLE `mimic-four-377221.R_TimeH.H_SHIT_part2`  AS
SELECT * FROM `mimic-four-377221.R_TimeG.G_ST` ;

#######################################################

alter table `mimic-four-377221.R_TimeH.H_SHIT_part2` 
add column hadm_id integer;

alter table `mimic-four-377221.R_TimeH.H_SHIT_part2` 
add column stay_id integer;

#######################################################

update `mimic-four-377221.R_TimeH.H_SHIT_part2` 
set hadm_id =0
where hadm_id is null;



update `mimic-four-377221.R_TimeH.H_SHIT_part2` 
set stay_id =99
where stay_id is null;

#######################################################

CREATE TABLE `mimic-four-377221.R_TimeH.H_SHIT_part3`  AS
SELECT 
subject_id, hadm_id, stay_id, transfer_id, min_T, max_T
 FROM `mimic-four-377221.R_TimeH.H_SHIT` 

 union all

 SELECT 
subject_id, hadm_id, stay_id, transfer_id, min, max
 FROM `mimic-four-377221.R_TimeH.H_SHIT_part2` ;

#######################################################

drop table `mimic-four-377221.R_TimeH.H_SHIT` ;
drop table `mimic-four-377221.R_TimeH.H_SHIT_part2` ;

#######################################################

CREATE TABLE `mimic-four-377221.R_TimeH.H_SHIT`  AS
SELECT * FROM `mimic-four-377221.R_TimeH.H_SHIT_part3` ;

#######################################################

drop table `mimic-four-377221.R_TimeH.H_SHIT_part3` ;

#######################################################
'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
