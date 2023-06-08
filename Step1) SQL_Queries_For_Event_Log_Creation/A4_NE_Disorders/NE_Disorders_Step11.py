import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

        CREATE TABLE  `mimic-four-377221.P_NonEvents.K7`   AS
        SELECT distinct
        a.rowNum, a.subject_id, a.hadm_id,
        b.D01, b.D02, b.D03, b.D04, b.D05, b.D06, b.D07, b.D08, b.D09, b.D10, b.D11, b.D12, b.D13, b.D14, b.D15, b.D16, b.D17, b.D18, b.D19, b.D20, b.D21, b.D22, b.D23, b.D24, b.D25, b.D26, b.D27, b.D28, b.D29, b.D30, b.D31, b.D32, b.D33, b.D34, b.D35, b.D36, b.D37, b.D38, b.D39, b.D40, b.D41, b.D42, b.D43, b.D44, b.D45, b.D46, b.D47, b.D48, b.D49, b.D50, b.D51, b.D52, b.D53, b.D54, b.D55, b.D56, b.D57, b.D58, b.D59, b.D60, b.D61, b.D62, b.D63, b.D64, b.D65, b.D66, b.D67, b.D68, b.D69, b.D70, b.D71, b.D72, b.D73,
        From `mimic-four-377221.P_NonEvents.K5`   as a
        LEFT JOIN `mimic-four-377221.P_NonEvents.K6`   as b
        ON
        a.rowNum=b.rowNum 
        ;


'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
