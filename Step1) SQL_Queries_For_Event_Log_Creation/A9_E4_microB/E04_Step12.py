import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

        CREATE TABLE  `mimic-four-377221.E4_MicroB.Micro_C6`   AS
        SELECT
        a.rowNum, a.subject_id, a.hadm_id, a.Timestamp, a.test_name_Syn, a.org_name_Syn,
        b.ab_99, b.ab_00, b.ab_01, b.ab_02, b.ab_03, b.ab_04, b.ab_05, b.ab_06, b.ab_07, b.ab_08, b.ab_09, b.ab_10, b.ab_11, b.ab_12, b.ab_13, b.ab_14, b.ab_15, b.ab_16, b.ab_17, b.ab_18, b.ab_19, b.ab_20, b.ab_21, b.ab_22, b.ab_23, b.ab_24, b.ab_25, b.ab_26, b.ab_27,
        From `mimic-four-377221.E4_MicroB.Micro_C4`   as a
        LEFT JOIN `mimic-four-377221.E4_MicroB.Micro_C5`   as b
        ON
        a.rowNum=b.rowNum 
        ;


'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
