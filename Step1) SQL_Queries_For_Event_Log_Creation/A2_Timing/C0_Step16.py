import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

###############################################################

create table  `mimic-four-377221.R_TimeG.G_SH` as
SELECT 
a.subject_id,
b.hadm_id,
a.min as min_S, 
a.max as max_S,
b.min as min_H, 
b.max as max_H

FROM `mimic-four-377221.R_TimeF.F_S` a
left join  `mimic-four-377221.R_TimeF.F_SH` b
on
a.subject_id=b.subject_id;

            

###############################################################


create table  `mimic-four-377221.R_TimeG.G_SHTI` as
SELECT 
a.subject_id,
a.hadm_id,
a.transfer_id,
b.stay_id,
a.min as min_T, 
a.max as max_T,
b.min as min_I, 
b.max as max_I

FROM `mimic-four-377221.R_TimeF.F_SHT` a
left join  `mimic-four-377221.R_TimeF.F_SHI` b
on
a.subject_id=b.subject_id
and
a.hadm_id=b.hadm_id;


            

###############################################################


create table  `mimic-four-377221.R_TimeG.G_ST` as


SELECT * FROM `mimic-four-377221.R_TimeF.F_ST` ;
            

###############################################################




'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
