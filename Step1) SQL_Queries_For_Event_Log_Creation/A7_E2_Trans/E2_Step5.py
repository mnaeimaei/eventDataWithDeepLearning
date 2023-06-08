import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

#################################################################

create table `mimic-four-377221.E2_Trans.Trans3` as
SELECT 
subject_id, hadm_id, transfer_id, intime as Timestamp,
act1,act11, careunit, careunit2
FROM `mimic-four-377221.E2_Trans.Trans2` 

union all

SELECT 
subject_id, hadm_id, transfer_id, outtime as Timestamp,
act2,act22, careunit2, careunit
FROM `mimic-four-377221.E2_Trans.Trans2` ;

#################################################################




#################################################################
'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
