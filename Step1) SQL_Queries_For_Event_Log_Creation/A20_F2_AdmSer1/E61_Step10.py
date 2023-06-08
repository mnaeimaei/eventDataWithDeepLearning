import os
import pandas as pd
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

SELECT 
rowNum, hadm_id, a1, a2, a3, a4, a5
FROM `mimic-four-377221.E1_AdmSer1.A0` 

'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)


df = query_job.to_dataframe()
symPath2='../gcKey/AdmSer_std.csv'
Realpath2 = os.path.realpath(symPath2)
df2=df.to_csv(Realpath2,index=False)
