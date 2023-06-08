import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            


create schema `mimic-four-377221.E5_pharmacy` ;


create table `mimic-four-377221.E5_pharmacy.phar1` as
SELECT * FROM `mimic-four-377221.S_pharmacy.1_pharmacy` ;

create table `mimic-four-377221.E5_pharmacy.phar2` as
SELECT * FROM `mimic-four-377221.S_eMAR.1_eMAR` ;

create table `mimic-four-377221.E5_pharmacy.phar3` as
SELECT * FROM `mimic-four-377221.S_prescriptions.1_prescriptions` ;

'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
