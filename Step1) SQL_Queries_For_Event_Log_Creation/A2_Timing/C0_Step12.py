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

update `mimic-four-377221.R_TimeE.E_S` 
set min=mini_Time
where mini_Date is null;

update `mimic-four-377221.R_TimeE.E_S` 
set max=maxi_Time
where maxi_Date is null;


update `mimic-four-377221.R_TimeE.E_S` 
set min=mini_Date
where mini_Date is not null and mini_Date<mini_Time;

update `mimic-four-377221.R_TimeE.E_S` 
set max=maxi_Date
where maxi_Date is not null and maxi_Date>maxi_Time;


update `mimic-four-377221.R_TimeE.E_S` 
set min=mini_Time
where mini_Date is not null and mini_Date>=mini_Time;


update `mimic-four-377221.R_TimeE.E_S` 
set max=maxi_Time
where maxi_Date is not null and maxi_Date<=maxi_Time;

#######################################################

update `mimic-four-377221.R_TimeE.E_SH` 
set min=mini_Time
where mini_Date is null;

update `mimic-four-377221.R_TimeE.E_SH` 
set max=maxi_Time
where maxi_Date is null;


update `mimic-four-377221.R_TimeE.E_SH` 
set min=mini_Date
where mini_Date is not null and mini_Date<mini_Time;

update `mimic-four-377221.R_TimeE.E_SH` 
set max=maxi_Date
where maxi_Date is not null and maxi_Date>maxi_Time;


update `mimic-four-377221.R_TimeE.E_SH` 
set min=mini_Time
where mini_Date is not null and mini_Date>=mini_Time;


update `mimic-four-377221.R_TimeE.E_SH` 
set max=maxi_Time
where maxi_Date is not null and maxi_Date<=maxi_Time;

#######################################################

update `mimic-four-377221.R_TimeE.E_SHI` 
set min=mini_Time
where mini_Date is null;

update `mimic-four-377221.R_TimeE.E_SHI` 
set max=maxi_Time
where maxi_Date is null;


update `mimic-four-377221.R_TimeE.E_SHI` 
set min=mini_Date
where mini_Date is not null and mini_Date<mini_Time;

update `mimic-four-377221.R_TimeE.E_SHI` 
set max=maxi_Date
where maxi_Date is not null and maxi_Date>maxi_Time;


update `mimic-four-377221.R_TimeE.E_SHI` 
set min=mini_Time
where mini_Date is not null and mini_Date>=mini_Time;


update `mimic-four-377221.R_TimeE.E_SHI` 
set max=maxi_Time
where maxi_Date is not null and maxi_Date<=maxi_Time;


#######################################################


'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
