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

create table  `mimic-four-377221.R_TimeH.H_SH` as
SELECT subject_id, hadm_id, min_S, max_S
FROM `mimic-four-377221.R_TimeH.H_SH_Part1` 

union all
SELECT subject_id, hadm_id, min_S, min_H
FROM `mimic-four-377221.R_TimeH.H_SH_Part2` 

union all
SELECT subject_id, hadm_id, min_H, max_H
FROM `mimic-four-377221.R_TimeH.H_SH_Part3` 

union all
SELECT subject_id, hadm_id, min_H, max_H
FROM `mimic-four-377221.R_TimeH.H_SH_Part4` ;

#######################################################

update `mimic-four-377221.R_TimeH.H_SH` 
set hadm_id=0
where hadm_id is null;


#######################################################

drop table `mimic-four-377221.R_TimeH.H_SH_Part1` ;
drop table `mimic-four-377221.R_TimeH.H_SH_Part2` ;
drop table `mimic-four-377221.R_TimeH.H_SH_Part3` ;
drop table `mimic-four-377221.R_TimeH.H_SH_Part4` ;


#######################################################



'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
