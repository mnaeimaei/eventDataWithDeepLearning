import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

update `mimic-four-377221.D0_Potential.Nodes` 
set long_title="Other disorders of phosphorus metabolism"
where icd_code_syn="D62";

update `mimic-four-377221.D0_Potential.Event_Pot1` 
set long_title="Other disorders of phosphorus metabolism"
where icd_code_syn="D62";


'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
