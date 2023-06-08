import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            


        CREATE TABLE  `mimic-four-377221.D0_Potential.Potential_Entity`   AS
        SELECT
        a.rowNum, a.subject_id, a.hadm_id, a.icd_code, a.icd_code_syn,
        b.Entity1_Origin, b.Entity1_ID,
        From `mimic-four-377221.D0_Potential.Event_Pot1`   as a
        LEFT JOIN `mimic-four-377221.C0_EventLog.AEL5`   as b
        ON
        a.subject_id=b.subject_id 
        ;




'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
