import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            




        CREATE   TABLE `mimic-four-377221.D8_Specimen.Feature_Specimen`  AS
        SELECT * FROM `mimic-four-377221.E6_BloodGas.bgB14_E3_Specimen` 

         ;



'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
