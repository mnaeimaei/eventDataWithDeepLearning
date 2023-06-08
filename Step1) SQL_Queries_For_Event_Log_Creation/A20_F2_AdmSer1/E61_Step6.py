import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

        CREATE TABLE  `mimic-four-377221.F2_AdmSer1.A1_Prediction`   AS
        select distinct * from
        (SELECT
        a.rowNum, 
        a.a1, a.a2, a.a3, a.a4, a.a5
        From `mimic-four-377221.F2_AdmSer1.A0`   as a
        LEFT JOIN `mimic-four-377221.F2_AdmSer1.T2`   as b
        ON
        a.hadm_id=b.hadm_id )
        ;


'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
