import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

create table `mimic-four-377221.E6_BloodGas.bgA4` as

SELECT distinct 
subject_id, hadm_id, ACT, Timstamp, Label, Value_N as Value,
 flag
 FROM `mimic-four-377221.E6_BloodGas.bgA3` 
 where Timstamp is not null;


###############################################################






'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
