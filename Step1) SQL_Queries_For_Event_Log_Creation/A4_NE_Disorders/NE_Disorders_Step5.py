import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

        UPDATE  `mimic-four-377221.P_NonEvents.K2`   
        set icd_code="03812"
        where icd_code="3812";

        UPDATE  `mimic-four-377221.P_NonEvents.K2`   
        set icd_code="0389"
        where icd_code="389";

        UPDATE  `mimic-four-377221.P_NonEvents.K2`   
        set icd_code="04111"
        where icd_code="4111";

        UPDATE  `mimic-four-377221.P_NonEvents.K2`   
        set icd_code="07999"
        where icd_code="7999";


'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
