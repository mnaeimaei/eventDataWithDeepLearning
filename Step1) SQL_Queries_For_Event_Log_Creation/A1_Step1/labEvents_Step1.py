import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
#print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            


create schema `mimic-four-377221.S_labEvents` ;

create table `mimic-four-377221.S_labEvents.1_labEvents` as

        SELECT
        a.subject_id, 
        a.hadm_id, 
        a.labevent_id, 
        a.specimen_id,
        a.itemid, 
        a.order_provider_id, 
        a.charttime, 
        a.storetime,
        a.value, 
        a.valuenum, 
        a.valueuom, 
        a.ref_range_lower, 
        a.ref_range_upper,
        a.flag, 
        a.priority, 
        a.comments,

        b.label,
        b.fluid, 
        b.category,
        From `mimic-four-377221.x_mimiciv_hosp.labevents`   as a
        LEFT JOIN `mimic-four-377221.x_mimiciv_hosp.d_labitems`   as b
        ON        a.itemid=b.itemid         ;



'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
