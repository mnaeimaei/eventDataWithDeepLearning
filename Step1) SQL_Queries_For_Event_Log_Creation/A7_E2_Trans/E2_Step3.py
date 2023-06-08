import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

##################################################

update `mimic-four-377221.E2_Trans.Trans2` 
set act1 ="discharge_into"
where eventtype="discharge"	;

update `mimic-four-377221.E2_Trans.Trans2` 
set act11 ="DIN"
where eventtype="discharge"	;

update `mimic-four-377221.E2_Trans.Trans2` 
set act2 ="discharge_out_of"
where eventtype="discharge"	;

update `mimic-four-377221.E2_Trans.Trans2` 
set act22 ="DOO"
where eventtype="discharge"	;

##################################################


update `mimic-four-377221.E2_Trans.Trans2` 
set act1 ="transfer_into"
where eventtype="transfer"	;

update `mimic-four-377221.E2_Trans.Trans2` 
set act11 ="TIN"
where eventtype="transfer"	;

update `mimic-four-377221.E2_Trans.Trans2` 
set act2 ="transfer_out_of"
where eventtype="transfer"	;

update `mimic-four-377221.E2_Trans.Trans2` 
set act22 ="TOO"
where eventtype="transfer"	;

##################################################



update `mimic-four-377221.E2_Trans.Trans2` 
set act1 ="admit_into"
where eventtype="admit"	;

update `mimic-four-377221.E2_Trans.Trans2` 
set act11 ="AIN"
where eventtype="admit"	;

update `mimic-four-377221.E2_Trans.Trans2` 
set act2 ="admit_out_of"
where eventtype="admit"	;

update `mimic-four-377221.E2_Trans.Trans2` 
set act22 ="AOO"
where eventtype="admit"	;

##################################################




update `mimic-four-377221.E2_Trans.Trans2` 
set act1 ="staying_into"
where eventtype="ED"	;

update `mimic-four-377221.E2_Trans.Trans2` 
set act11 ="SIN"
where eventtype="ED"	;

update `mimic-four-377221.E2_Trans.Trans2` 
set act2 ="staying_out_of"
where eventtype="ED"	;

update `mimic-four-377221.E2_Trans.Trans2` 
set act22 ="SOO"
where eventtype="ED"	;

##################################################

'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
