import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

CREATE TABLE  `mimic-four-377221.C0_EventLog.AEL6`   AS
select distinct * from

(SELECT 
a.rowNum, 
a.Timestamp,
a.subject_id,
a.Entity1_Origin,
a.Entity1_ID,
a.hadm_id,
a.Entity2_Origin,
a.Entity2_ID,
a.Activity,
a.Activity_Synonym,
a.Activity_Origin,
a.Activity_Value_ID,
b.Disorders

FROM `mimic-four-377221.C0_EventLog.AEL5` a
left join  `mimic-four-377221.P_NonEvents.K8` b
on
a.subject_id=b.subject_id
and
a.hadm_id=b.hadm_id);

#####################################################################3

CREATE TABLE  `mimic-four-377221.C0_EventLog.EL6`   AS
select distinct * from

(SELECT 
a.rowNum, 
a.Timestamp,
a.subject_id,
a.Entity1_Origin,
a.Entity1_ID,
a.hadm_id,
a.Entity2_Origin,
a.Entity2_ID,
a.Activity,
a.Activity_Synonym,
a.Activity_Origin,
a.Activity_Value_ID,
b.Disorders

FROM `mimic-four-377221.C0_EventLog.EL5` a
left join  `mimic-four-377221.P_NonEvents.K8` b
on
a.subject_id=b.subject_id
and
a.hadm_id=b.hadm_id);

####################################################################

drop table `mimic-four-377221.C0_EventLog.AEL5` ;
drop table `mimic-four-377221.C0_EventLog.EL5` ;  

'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
