import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            


        CREATE TABLE  `mimic-four-377221.E4_Micro.Micro_B93`   AS 
        SELECT * FROM `mimic-four-377221.E4_Micro.Micro_B92` 
where subject_id=13313474 or
subject_id=17905563 or
subject_id=18030855

        


'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
