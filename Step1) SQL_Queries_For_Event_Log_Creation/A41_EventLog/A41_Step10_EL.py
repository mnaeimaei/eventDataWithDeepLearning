import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            


update `mimic-four-377221.C0_EventLog.EL3` 
set Entity2_ID=RankN
where Entity2_ID is null;

update `mimic-four-377221.C0_EventLog.AEL3` 
set Entity2_ID=RankN
where Entity2_ID is null;



'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
