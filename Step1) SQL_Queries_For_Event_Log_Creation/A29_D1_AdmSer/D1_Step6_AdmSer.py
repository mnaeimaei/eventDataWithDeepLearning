import os
import pandas as pd
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

############################################################################################################
############################################################################################################
############################################################################################################
# Perform a query.
query1 = f'''            

SELECT * FROM `mimic-four-377221.D1_AdmSer.Feature_AdmSer` 

'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)


df = query_job.to_dataframe()
symPath2='../File_OtherFiles/Feature_AdmSer.csv'
Realpath2 = os.path.realpath(symPath2)
df2=df.to_csv(Realpath2,index=False)




############################################################################################################
############################################################################################################
############################################################################################################
# Perform a query.
query1 = f'''            

SELECT * FROM `mimic-four-377221.D1_AdmSer.eLogFeatureClass_AdmSer` 

'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)


df = query_job.to_dataframe()
symPath2='../File_TrainingData/0DownloadedFiles/eLogFeatureClass_AdmSer.csv'
Realpath2 = os.path.realpath(symPath2)
df2=df.to_csv(Realpath2,index=False)

#############################################################################################################