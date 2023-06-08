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

SELECT * FROM `mimic-four-377221.C0_EventLog.AEL_output` 

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

SELECT * FROM `mimic-four-377221.C0_EventLog.EL_output` 


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

SELECT * FROM `mimic-four-377221.D0_Potential.Nodes_output` 


'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

df = query_job.to_dataframe()
symPath2='../File_OtherFiles/Potential_Node.csv'
Realpath2 = os.path.realpath(symPath2)
df2=df.to_csv(Realpath2,index=False)


#############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
# Perform a query.
query1 = f'''            

SELECT * FROM `mimic-four-377221.C0_OCT.OCT_Nodes` 


'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

df = query_job.to_dataframe()
symPath2='../File_OtherFiles/OCT_Node.csv'
Realpath2 = os.path.realpath(symPath2)
df2=df.to_csv(Realpath2,index=False)


#############################################################################################################



############################################################################################################
############################################################################################################
############################################################################################################
# Perform a query.
query1 = f'''            

SELECT * FROM `mimic-four-377221.C0_OCT.OCT_Rel` 


'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

df = query_job.to_dataframe()
symPath2='../File_OtherFiles/OCT_REL.csv'
Realpath2 = os.path.realpath(symPath2)
df2=df.to_csv(Realpath2,index=False)


#############################################################################################################



############################################################################################################
############################################################################################################
############################################################################################################
# Perform a query.
query1 = f'''            

SELECT * FROM `mimic-four-377221.D0_Potential.Potential_Entity_Aggr` 


'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

df = query_job.to_dataframe()
symPath2='../File_OtherFiles/Potential_Entity_Aggr.csv'
Realpath2 = os.path.realpath(symPath2)
df2=df.to_csv(Realpath2,index=False)


#############################################################################################################




############################################################################################################
############################################################################################################
############################################################################################################
# Perform a query.
query1 = f'''            

SELECT * FROM `mimic-four-377221.D0_Potential.Potential_Entity_Ind` 


'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

df = query_job.to_dataframe()
symPath2='../File_OtherFiles/Potential_Entity_Ind.csv'
Realpath2 = os.path.realpath(symPath2)
df2=df.to_csv(Realpath2,index=False)


#############################################################################################################



############################################################################################################
############################################################################################################
############################################################################################################
# Perform a query.
query1 = f'''            

SELECT * FROM `mimic-four-377221.C0_Potential_OCT.PO2` 


'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

df = query_job.to_dataframe()
symPath2='../File_OtherFiles/Potential_OCT.csv'
Realpath2 = os.path.realpath(symPath2)
df2=df.to_csv(Realpath2,index=False)


#############################################################################################################



############################################################################################################
############################################################################################################
############################################################################################################
# Perform a query.
query1 = f'''            

SELECT * FROM `mimic-four-377221.C0_Activity_OTC.A1` 


'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

df = query_job.to_dataframe()
symPath2='../File_OtherFiles/Activity_OCT.csv'
Realpath2 = os.path.realpath(symPath2)
df2=df.to_csv(Realpath2,index=False)


############################################################################################################
############################################################################################################
############################################################################################################
# Perform a query.
query1 = f'''            

SELECT * FROM `mimic-four-377221.C0_Activity_Event.BondAll_output` 


'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

df = query_job.to_dataframe()
symPath2='../File_OtherFiles/BondAll_output.csv'
Realpath2 = os.path.realpath(symPath2)
df2=df.to_csv(Realpath2,index=False)


############################################################################################################
############################################################################################################
############################################################################################################
# Perform a query.
query1 = f'''            


SELECT * FROM `mimic-four-377221.C0_Activity_Event.Bond_output` 

'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

df = query_job.to_dataframe()
symPath2='../File_OtherFiles/Bond_output.csv'
Realpath2 = os.path.realpath(symPath2)
df2=df.to_csv(Realpath2,index=False)


#############################################################################################################


