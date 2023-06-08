import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            


        CREATE   TABLE `mimic-four-377221.E4_MicroB.Micro_C4`  AS

SELECT 

rowNum, subject_id, hadm_id, Timestamp, test_name, test_name_Syn, org_name, org_name_Syn, ab_name, ab_name_Syn, interpretation, interpretation_Syn
 FROM `mimic-four-377221.E4_MicroB.Micro_C3` 
where Timestamp is not null

'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
