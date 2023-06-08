import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            




create table `mimic-four-377221.P_NonEvents.K1` as
SELECT distinct icd_code,
long_title
 FROM `mimic-four-377221.P_NonEvents.icdCM1` 

where subject_id=13313474 or 
 subject_id=17905563 or
 subject_id=18030855

 order by icd_code

'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
