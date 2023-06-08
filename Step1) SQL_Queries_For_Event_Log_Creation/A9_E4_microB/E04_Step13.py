import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

        CREATE TABLE  `mimic-four-377221.E4_MicroB.Micro_C7`   AS
        SELECT distinct   * FROM  `mimic-four-377221.E4_MicroB.Micro_C6`

  order by subject_id, Timestamp
        ;


'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
