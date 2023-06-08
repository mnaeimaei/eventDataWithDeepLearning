import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

        CREATE TABLE  `mimic-four-377221.C0_EventLog.AEL_final`   AS
        SELECT
        rowNum, Timestamp, Entity1_Origin, Entity1_ID, Entity2_Origin, Entity2_ID, Activity, Activity_Synonym, Activity_Origin, Activity_Value_ID,
        From `mimic-four-377221.C0_EventLog.AEL6`          ;


        CREATE TABLE  `mimic-four-377221.C0_EventLog.EL_final`   AS
        SELECT
        rowNum, Timestamp,Entity1_Origin, Entity1_ID, Entity2_Origin, Entity2_ID, Activity, Activity_Synonym, Activity_Origin, Activity_Value_ID,
        From `mimic-four-377221.C0_EventLog.EL6`      ;
        
        CREATE TABLE  `mimic-four-377221.C0_EventLog.AEL_final_Disorders`   AS
        SELECT
        Activity_Origin as Type, Activity_Value_ID as ActivityValueID, Disorders
        From `mimic-four-377221.C0_EventLog.AEL6`          ;


        CREATE TABLE  `mimic-four-377221.C0_EventLog.EL_final_Disorders`   AS
        SELECT
        Activity_Origin as Type, Activity_Value_ID as ActivityValueID, Disorders
        From `mimic-four-377221.C0_EventLog.EL6`      ;


'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
