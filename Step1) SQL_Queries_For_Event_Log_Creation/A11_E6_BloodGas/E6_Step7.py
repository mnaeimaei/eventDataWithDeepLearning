import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            


create table `mimic-four-377221.E6_BloodGas.bgA5` as

SELECT distinct 
subject_id, hadm_id, ACT, Timstamp, Label, Value
 FROM `mimic-four-377221.E6_BloodGas.bgA4` 

#################################################################

        alter table `mimic-four-377221.E6_BloodGas.bgA5`
        ADD COLUMN Value_Int INTEGER  ;
        
#####################################################################

'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
