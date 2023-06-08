import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            
##################################################################
update `mimic-four-377221.E1_AdmSer.Tab2` 
set admission_location="NULL"
where admission_location is null;


update `mimic-four-377221.E1_AdmSer.Tab2` 
set admission_type="NULL"
where admission_type is null;


update `mimic-four-377221.E1_AdmSer.Tab4` 
set discharge_location	="NULL"
where discharge_location	 is null;

update `mimic-four-377221.E1_AdmSer.Tab5` 
set discharge_location	="NULL"
where discharge_location	 is null;

update `mimic-four-377221.E1_AdmSer.Tab6` 
set prev_service	="NULL"
where prev_service	 is null;

update `mimic-four-377221.E1_AdmSer.Tab6` 
set curr_service	="NULL"
where curr_service	 is null;

##################################################################
'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
