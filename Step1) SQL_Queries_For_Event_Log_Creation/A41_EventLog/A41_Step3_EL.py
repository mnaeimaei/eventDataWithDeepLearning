import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            


create table `mimic-four-377221.C0_EventLog.AEL1` as
SELECT 
rowNum, subject_id, hadm_id, Timestamp, Activity, Activity_Synonym,  Type as Activity_Origin, ActivityValueID as Activity_Value_ID
FROM `mimic-four-377221.D1_AdmSer.eLogA_AdmSer` 

union all

SELECT 
rowNum, subject_id, hadm_id, Timestamp, Activity, Activity_Synonym,  Type as ActivityOrigin, ActivityValue_ID as Activity_Value_ID
FROM `mimic-four-377221.D2_Transfer.eLogA_Transfer` 

union all

SELECT 
rowNum, subject_id, hadm_id, Timestamp, Activity, Activity_Synonym,  Type as ActivityOrigin, ActivityValueID as Activity_Value_ID
FROM `mimic-four-377221.D3_MicroA.eLogA_MicroA` 

union all

SELECT 
rowNum, subject_id, hadm_id, Timestamp, Activity, Activity_Synonym,  Type as ActivityOrigin, ActivityValue_ID as Activity_Value_ID
FROM `mimic-four-377221.D4_MicroB.eLogA_MicroB` 

union all

SELECT 
rowNum, subject_id, hadm_id, Timestamp, Activity, Activity_Synonym,  Type as ActivityOrigin, ActivityValue_ID as Activity_Value_ID
FROM `mimic-four-377221.D5_RT.eLogA_RT` 


union all

SELECT 
rowNum, subject_id, hadm_id, Timestamp, Activity, Activity_Synonym,  Type as ActivityOrigin, ActivityValue_ID as Activity_Value_ID
FROM `mimic-four-377221.D6_CMP.eLogA_CMP` 


union all

SELECT 
rowNum, subject_id, hadm_id, Timestamp, Activity, Activity_Synonym,  Type as ActivityOrigin, ActivityValue_ID as Activity_Value_ID
FROM `mimic-four-377221.D7_ABG.eLogA_ABG` 


union all

SELECT 
rowNum, subject_id, hadm_id, Timestamp, Activity, Activity_Synonym,  Type as ActivityOrigin, ActivityValue_ID as Activity_Value_ID
FROM `mimic-four-377221.D8_Specimen.eLogA_Specimen` 



'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
