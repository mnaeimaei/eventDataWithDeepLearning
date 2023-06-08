import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
#print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

create table `mimic-four-377221.S_labEvents.2_Chemistry` as

SELECT 

subject_id	,
hadm_id	,
labevent_id	,
specimen_id	,
itemid	,
order_provider_id	,
charttime	,
storetime	,
value	,
valuenum	,
valueuom	,
ref_range_lower	,
ref_range_upper	,
flag	,
priority	,
comments	,
label	,
fluid	,

FROM `mimic-four-377221.S_labEvents.1_labEvents` 
where category="Chemistry"

'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
