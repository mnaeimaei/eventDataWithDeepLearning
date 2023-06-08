import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

        CREATE TABLE  `mimic-four-377221.D0_Potential.Potential_Entity_all`   AS
        SELECT 
        ER, Entity1_Origin, Entity1_ID, Entity2_Origin, Entity2_ID, icd_code, icd_code_syn
        FROM `mimic-four-377221.D0_Potential.Potential_Entity` ;

'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
