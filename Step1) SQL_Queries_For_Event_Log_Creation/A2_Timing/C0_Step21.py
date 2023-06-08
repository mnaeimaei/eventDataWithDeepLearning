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

create table  `mimic-four-377221.R_TimeH.H_SHTI_part1` as

SELECT * FROM `mimic-four-377221.R_TimeG.G_SHTI` 
where stay_id is null;


#######################################################

create table  `mimic-four-377221.R_TimeH.H_SHTI_part2` as

SELECT * FROM `mimic-four-377221.R_TimeG.G_SHTI` 
where stay_id is not null;


#######################################################

        CREATE TABLE `mimic-four-377221.R_TimeH.H_SHTI_part22`  AS
        
        SELECT
        a.subject_id, a.hadm_id, a.stay_id, 
        
        a.transfer_id, 
        b.RankN as RankN_A,
        a.min_T, a.max_T, a.min_I, a.max_I
        FROM `mimic-four-377221.R_TimeH.H_SHTI_part2`  a
        LEFT   JOIN (
        SELECT  
        subject_id, hadm_id, stay_id, min_T,
        Row_number() over (partition by  subject_id order by min_T) as RankN
        FROM
        
        (SELECT   DISTINCT subject_id, hadm_id, stay_id, min_T  FROM `mimic-four-377221.R_TimeH.H_SHTI_part2`  )  ) b
        ON
        a.subject_id = b.subject_id AND a.hadm_id = b.hadm_id AND a.stay_id = b.stay_id AND a.min_T = b.min_T
;
#######################################################

        CREATE TABLE `mimic-four-377221.R_TimeH.H_SHTI_part23`  AS
        
        SELECT
        a.subject_id, a.hadm_id, a.stay_id, 
        a.transfer_id,
        a.RankN_A, b.RankN as RankN_B, a.min_T, a.max_T, a.min_I, a.max_I
        FROM `mimic-four-377221.R_TimeH.H_SHTI_part22`  a
        LEFT   JOIN (
        SELECT  
        subject_id, hadm_id, stay_id, max_T,
        Row_number() over (partition by  subject_id order by max_T desc) as RankN
        FROM
        
        (SELECT   DISTINCT subject_id, hadm_id, stay_id, max_T  FROM `mimic-four-377221.R_TimeH.H_SHTI_part22`  )  ) b
        ON
        a.subject_id = b.subject_id AND a.hadm_id = b.hadm_id AND a.stay_id = b.stay_id AND a.max_T = b.max_T
        ;

#######################################################

update `mimic-four-377221.R_TimeH.H_SHTI_part23` 
set min_T=min_I
where RankN_A=1 and min_T>min_I;


update `mimic-four-377221.R_TimeH.H_SHTI_part23` 
set max_T=max_I
where RankN_B=1 and max_T<max_I;

#######################################################

        CREATE TABLE `mimic-four-377221.R_TimeH.H_SHIT`  AS
(SELECT subject_id, hadm_id, stay_id, transfer_id, min_T, max_T  FROM `mimic-four-377221.R_TimeH.H_SHTI_part1` 
union all
SELECT subject_id, hadm_id, stay_id, transfer_id, min_T, max_T  FROM `mimic-four-377221.R_TimeH.H_SHTI_part23` );
#######################################################

drop table `mimic-four-377221.R_TimeH.H_SHTI_part1` ;
drop table `mimic-four-377221.R_TimeH.H_SHTI_part2` ;
drop table `mimic-four-377221.R_TimeH.H_SHTI_part22` ;
drop table `mimic-four-377221.R_TimeH.H_SHTI_part23` ;

#######################################################
'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
