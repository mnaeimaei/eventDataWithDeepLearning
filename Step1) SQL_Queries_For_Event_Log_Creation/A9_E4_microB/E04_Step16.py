import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            


create table `mimic-four-377221.E4_MicroB.Micro_C8`    as

SELECT 

rowNum, subject_id, hadm_id, Timestamp, Activity, Activity_Synonym, TYPE, Property, 

test_name_Syn, org_name_Syn, ab_99, ab_00, ab_01, ab_02, ab_03, ab_04, ab_05, ab_06, ab_07, ab_08, ab_09, ab_10, ab_11, ab_12, ab_13, ab_14, ab_15, ab_16, ab_17, ab_18, ab_19, ab_20, ab_21, ab_22, ab_23, ab_24, ab_25, ab_26, ab_27
FROM `mimic-four-377221.E4_MicroB.Micro_C7` 


'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
