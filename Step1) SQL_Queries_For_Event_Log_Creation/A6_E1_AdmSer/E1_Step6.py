import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

update `mimic-four-377221.E1_AdmSer.TabF` 
set admission_location="ND"
where admission_location is null;


update `mimic-four-377221.E1_AdmSer.TabF` 
set admission_type="ND"
where admission_type is null;


update `mimic-four-377221.E1_AdmSer.TabF` 
set discharge_location	="ND"
where discharge_location	 is null;

update `mimic-four-377221.E1_AdmSer.TabF` 
set discharge_location	="ND"
where discharge_location	 is null;

update `mimic-four-377221.E1_AdmSer.TabF` 
set prev_service	="ND"
where prev_service	 is null;

update `mimic-four-377221.E1_AdmSer.TabF` 
set curr_service	="ND"
where curr_service	 is null;




'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
