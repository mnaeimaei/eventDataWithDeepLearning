import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

        CREATE TABLE  `mimic-four-377221.C0_EventLog.AEL3`   AS
        SELECT
        a.rowNum, a.Timestamp, a.subject_id, a.Entity1_Origin, a.Entity1_ID, a.hadm_id, a.Entity2_Origin, a.Entity2_ID, a.Activity, a.Activity_Synonym, a.Activity_Origin, a.Activity_Value_ID,
        b.RankN,
        From `mimic-four-377221.C0_EventLog.AEL2`   as a
        LEFT JOIN `mimic-four-377221.C0_EventLog.Timing2`   as b
        ON
        a.subject_id=b.subject_id AND a.hadm_id=b.hadm_id 
        ;

'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
