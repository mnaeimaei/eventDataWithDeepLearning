import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            


        CREATE TABLE  `mimic-four-377221.E6_BloodGas.bgB14_D1K`   AS
        SELECT * FROM 
        (SELECT
        b.rowNum, b.Item7, b.Item10, b.Item11, b.Item12, b.Item13, b.Item15, b.Item28, b.Item30,
        a.D01, a.D02, a.D03, a.D04, a.D05, a.D06, a.D07, a.D08, a.D09, a.D10, a.D11, a.D12, a.D13, a.D14, a.D15, a.D16, a.D17, a.D18, a.D19, a.D20, a.D21, a.D22, a.D23, a.D24, a.D25, a.D26, a.D27, a.D28, a.D29, a.D30, a.D31, a.D32, a.D33, a.D34, a.D35, a.D36, a.D37, a.D38, a.D39, a.D40, a.D41, a.D42, a.D43, a.D44, a.D45, a.D46, a.D47, a.D48, a.D49, a.D50, a.D51, a.D52, a.D53, a.D54, a.D55, a.D56, a.D57, a.D58, a.D59, a.D60, a.D61, a.D62, a.D63, a.D64, a.D65, a.D66, a.D67, a.D68, a.D69, a.D70, a.D71, a.D72, a.D73,
        From `mimic-four-377221.P_NonEvents.K7`   as a
        LEFT JOIN `mimic-four-377221.E6_BloodGas.bgB14_C1`   as b
        ON
        a.HADM_ID=b.HADM_ID )
        WHERE Item7 is not null
        ;




'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
