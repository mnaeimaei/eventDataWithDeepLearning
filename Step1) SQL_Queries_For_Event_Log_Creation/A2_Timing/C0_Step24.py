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

create table  `mimic-four-377221.R_TimeI.I_All_part1` as
(SELECT 

a.subject_id,
a.hadm_id,
a.stay_id,
a.transfer_id,
a.min_T,
a.max_T,



FROM `mimic-four-377221.R_TimeH.H_SHIT` a
left join `mimic-four-377221.R_TimeH.H_SH` b
on 
a.subject_id=b.subject_id
and
a.hadm_id=b.hadm_id
where b.hadm_id is null
);




#######################################################

create table  `mimic-four-377221.R_TimeI.I_All_part2` as
(SELECT 

a.subject_id,
a.hadm_id,

b.stay_id,
b.transfer_id,

a.min_S,
a.max_S,

b.min_T,
b.max_T,

FROM `mimic-four-377221.R_TimeH.H_SH` a
left join `mimic-four-377221.R_TimeH.H_SHIT` b
on 
a.subject_id=b.subject_id
and
a.hadm_id=b.hadm_id
)

;
#######################################################

alter table `mimic-four-377221.R_TimeI.I_All_part1` 
add column min_S Datetime;

alter table `mimic-four-377221.R_TimeI.I_All_part1` 
add column max_S Datetime;


#######################################################

create table  `mimic-four-377221.R_TimeI.I_All` as
SELECT 
subject_id, hadm_id, stay_id, transfer_id, min_S, max_S, min_T, max_T

FROM `mimic-four-377221.R_TimeI.I_All_part2` 


union all
SELECT 
subject_id, hadm_id, stay_id, transfer_id, min_S, max_S, min_T, max_T

FROM `mimic-four-377221.R_TimeI.I_All_part1` ;



#######################################################



drop table `mimic-four-377221.R_TimeI.I_All_part2` ;
drop table `mimic-four-377221.R_TimeI.I_All_part1` ;

#######################################################
'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
