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
create table  `mimic-four-377221.R_TimeH.H_SH_Partly` as

     SELECT
        a.subject_id,
        b.RankN,
        a.min_H,
        
        a.max_H
        FROM `mimic-four-377221.R_TimeH.H_SH_Part3`  a
        LEFT   JOIN (
        SELECT  
        subject_id, min_H,
        Row_number() over (partition by  subject_id order by min_H) as RankN
        FROM
        
        (SELECT   DISTINCT subject_id, min_H  FROM `mimic-four-377221.R_TimeH.H_SH_Part3`  )  ) b
        ON
        a.subject_id = b.subject_id AND a.min_H = b.min_H;
        
        

#######################################################

update `mimic-four-377221.R_TimeH.H_SH_Partly` 
set min_H=DATETIME_ADD(min_H, INTERVAL -1 SECOND) 
where min_H is not null;

update `mimic-four-377221.R_TimeH.H_SH_Partly` 
set max_H=DATETIME_ADD(max_H, INTERVAL 1 SECOND) 
where max_H is not null;

#######################################################
create table  `mimic-four-377221.R_TimeH.H_SH_Part4` as

(SELECT * FROM
(select 
a.subject_id,
a.max_H as min_H,
b.min_H as max_H,
from `mimic-four-377221.R_TimeH.H_SH_Partly` a
left join `mimic-four-377221.R_TimeH.H_SH_Partly` b
on
a.subject_id=b.subject_id
and
a.RankN=b.RankN-1)
where  max_H is not null and min_H is not null and min_H<max_H
);

#######################################################
alter table `mimic-four-377221.R_TimeH.H_SH_Part4` 
add column hadm_id integer;
#######################################################

drop table `mimic-four-377221.R_TimeH.H_SH_Partly` ;


'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
