import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            





################################################

CREATE TABLE  `mimic-four-377221.R_TimeI.I_All_p23`   AS

select distinct * from
(select 
s1 as subject_id
, h1 as hadm_id
, i1 as stay_id
, t1 as transfer_id
, min1 as min_Time
, max1 as max_Time
from  `mimic-four-377221.R_TimeI.I_All_p22` 
where s1 is not null


union all


select 
s2 as subject_id
, h2 as hadm_id
, i2 as stay_id
, t2 as transfer_id
, min2 as min_Time
, max2 
from  `mimic-four-377221.R_TimeI.I_All_p22` 
where s2 is not null


union all



select 
s3 as subject_id
, h3 as hadm_id
, i3 as stay_id
, t3 as transfer_id
, min3 as min_Time
, max3  as max_Time
from  `mimic-four-377221.R_TimeI.I_All_p22` 
where s3 is not null);





################################################

'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
