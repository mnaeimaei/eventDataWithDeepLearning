import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

        CREATE TABLE  `mimic-four-377221.E4_Micro.Micro_B91`   AS
SELECT 
rowNum as ActivityValueID,
test_name,
spec_type_desc


FROM `mimic-four-377221.E4_Micro.Micro_B2` 
order by rowNum


'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
