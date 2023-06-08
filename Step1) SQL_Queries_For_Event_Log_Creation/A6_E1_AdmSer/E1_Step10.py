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
add column Property_Str string;

############################################################

alter table `mimic-four-377221.E1_AdmSer.TabF` 
add column Proprty_int string;

############################################################

update `mimic-four-377221.E1_AdmSer.TabF` 
set Property_Str=concat("[",admission_location,",",admission_type,",",discharge_location,",",prev_service,",",curr_service,"]")
where Property_Str is null;

############################################################

update `mimic-four-377221.E1_AdmSer.TabF` 
set Proprty_int=concat("[",a1,",",a2,",",a3,",",a4,",",a5,"]")
where Proprty_int is null;
############################################################

'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
