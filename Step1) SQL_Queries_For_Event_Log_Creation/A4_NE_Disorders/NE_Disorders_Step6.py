import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

create table `mimic-four-377221.P_NonEvents.K3` as
SELECT * FROM `mimic-four-377221.P_NonEvents.K2` 
where num="0"
or num="A"
or num="C"
or num="D"
or num="E"
or num="H"
or num="I"
or num="J"
or num="K"
or num="L"

'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
