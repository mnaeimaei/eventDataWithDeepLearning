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

SELECT * FROM `mimic-four-377221.C0_EventLog.AEL_output` ;

'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)


df = query_job.to_dataframe()
symPath2='../File_OtherFiles/EventLogAll.csv'
Realpath2 = os.path.realpath(symPath2)
df2=df.to_csv(Realpath2,index=False)




############################################################################################################
############################################################################################################
############################################################################################################
# Perform a query.
query1 = f'''            

SELECT * FROM `mimic-four-377221.C0_EventLog.EL_output` ;


'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

df = query_job.to_dataframe()
symPath2='../File_OtherFiles/EventLog.csv'
Realpath2 = os.path.realpath(symPath2)
df2=df.to_csv(Realpath2,index=False)


#############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
# Perform a query.
query1 = f'''            

SELECT * FROM `mimic-four-377221.C0_EventLog.AEL_final_Disorders` ;

'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

df = query_job.to_dataframe()
symPath2='../File_OtherFiles/EventLogAll_Disorders.csv'
Realpath2 = os.path.realpath(symPath2)
df2=df.to_csv(Realpath2,index=False)


#############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
# Perform a query.
query1 = f'''            


SELECT * FROM `mimic-four-377221.C0_EventLog.EL_final_Disorders` ;

'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

df = query_job.to_dataframe()
symPath2='../File_OtherFiles/EventLog_Disorders.csv'
Realpath2 = os.path.realpath(symPath2)
df2=df.to_csv(Realpath2,index=False)


#############################################################################################################



############################################################################################################
############################################################################################################
############################################################################################################