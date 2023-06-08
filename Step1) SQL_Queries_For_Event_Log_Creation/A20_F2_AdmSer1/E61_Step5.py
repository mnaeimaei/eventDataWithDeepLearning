import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            
        CREATE TABLE  `mimic-four-377221.F2_AdmSer1.A1_Training`   AS
        select * from
        (SELECT
        a.rowNum, 
        a.a1, a.a2, a.a3, a.a4, a.a5,
        b.icd_code_int as disorder
        From `mimic-four-377221.F2_AdmSer1.A0`   as a
        LEFT JOIN `mimic-four-377221.F2_AdmSer1.T1`   as b
        ON
        a.hadm_id=b.hadm_id )
        where disorder is not null
        ;


'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
