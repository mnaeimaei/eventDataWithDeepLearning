import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            



#######################################################

alter table `mimic-four-377221.R_TimeI.I_All_p2` 
add column min2 DATETIME;


alter table `mimic-four-377221.R_TimeI.I_All_p2` 
add column max2 DATETIME;



alter table `mimic-four-377221.R_TimeI.I_All_p2` 
add column s3 INTEGER;

alter table `mimic-four-377221.R_TimeI.I_All_p2` 
add column h3 INTEGER;

alter table `mimic-four-377221.R_TimeI.I_All_p2` 
add column i3 INTEGER;

################################################






'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
