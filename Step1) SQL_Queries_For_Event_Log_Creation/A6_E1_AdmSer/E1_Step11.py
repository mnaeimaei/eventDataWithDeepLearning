import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            
############################################################

alter table `mimic-four-377221.E1_AdmSer.TabF` 
add column Type string;

############################################################

update `mimic-four-377221.E1_AdmSer.TabF` 
set Type="Logistic"
where Type is null;



'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
