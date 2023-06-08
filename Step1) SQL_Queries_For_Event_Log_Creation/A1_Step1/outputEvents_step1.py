import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            


create schema `mimic-four-377221.S_outputEvents` ;

create table `mimic-four-377221.S_outputEvents.1_outputEvent` as


SELECT
        a.subject_id, 
        a.hadm_id, 
        a.stay_id,
        a.caregiver_id, 
        a.charttime, 
        a.storetime, 
        a.value, 
        a.valueuom,
        
        b.itemid, 
        b.label, 
        b.abbreviation, 
        b.category, 
        b.unitname, 
        b.param_type, 
        b.lownormalvalue, 
        b.highnormalvalue,
        
        From `mimic-four-377221.x_mimiciv_icu.outputevents`   as a
        LEFT JOIN `mimic-four-377221.x_mimiciv_icu.d_items`   as b
        ON
        a.itemid=b.itemid 
        ;
        
        





'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
