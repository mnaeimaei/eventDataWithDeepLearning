import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

###########################################################################

alter table `mimic-four-377221.R_TimeE.E_S` 
add column min DATETIME;

alter table `mimic-four-377221.R_TimeE.E_S` 
add column max DATETIME;


#######################################################


alter table `mimic-four-377221.R_TimeE.E_SH` 
add column min DATETIME;

alter table `mimic-four-377221.R_TimeE.E_SH` 
add column max DATETIME;


#######################################################



alter table `mimic-four-377221.R_TimeE.E_SHI` 
add column min DATETIME;

alter table `mimic-four-377221.R_TimeE.E_SHI` 
add column max DATETIME;





		

'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
