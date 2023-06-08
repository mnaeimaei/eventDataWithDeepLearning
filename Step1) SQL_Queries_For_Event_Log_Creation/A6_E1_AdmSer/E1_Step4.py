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

alter table `mimic-four-377221.E1_AdmSer.Tab1` 
add column admission_location string;

alter table `mimic-four-377221.E1_AdmSer.Tab1` 
add column admission_type string;

alter table `mimic-four-377221.E1_AdmSer.Tab1` 
add column discharge_location string;

alter table `mimic-four-377221.E1_AdmSer.Tab1` 
add column prev_service string;

alter table `mimic-four-377221.E1_AdmSer.Tab1` 
add column curr_service string;

##################################################################


alter table `mimic-four-377221.E1_AdmSer.Tab2` 
add column discharge_location string;

alter table `mimic-four-377221.E1_AdmSer.Tab2` 
add column prev_service string;

alter table `mimic-four-377221.E1_AdmSer.Tab2` 
add column curr_service string;

##################################################################


alter table `mimic-four-377221.E1_AdmSer.Tab3` 
add column admission_location string;

alter table `mimic-four-377221.E1_AdmSer.Tab3` 
add column admission_type string;

alter table `mimic-four-377221.E1_AdmSer.Tab3` 
add column discharge_location string;

alter table `mimic-four-377221.E1_AdmSer.Tab3` 
add column prev_service string;

alter table `mimic-four-377221.E1_AdmSer.Tab3` 
add column curr_service string;

##################################################################



alter table `mimic-four-377221.E1_AdmSer.Tab4` 
add column admission_location string;

alter table `mimic-four-377221.E1_AdmSer.Tab4` 
add column admission_type string;

alter table `mimic-four-377221.E1_AdmSer.Tab4` 
add column prev_service string;

alter table `mimic-four-377221.E1_AdmSer.Tab4` 
add column curr_service string;

##################################################################


alter table `mimic-four-377221.E1_AdmSer.Tab5` 
add column admission_location string;

alter table `mimic-four-377221.E1_AdmSer.Tab5` 
add column admission_type string;

alter table `mimic-four-377221.E1_AdmSer.Tab5` 
add column prev_service string;

alter table `mimic-four-377221.E1_AdmSer.Tab5` 
add column curr_service string;

##################################################################


alter table `mimic-four-377221.E1_AdmSer.Tab6` 
add column admission_location string;

alter table `mimic-four-377221.E1_AdmSer.Tab6` 
add column admission_type string;

alter table `mimic-four-377221.E1_AdmSer.Tab6` 
add column discharge_location string;


##################################################################



'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
