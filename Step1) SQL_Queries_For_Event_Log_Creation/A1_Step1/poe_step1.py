import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
#print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            


create schema `mimic-four-377221.S_poe` ;

        CREATE TABLE  `mimic-four-377221.S_poe.1_POE`   AS
        SELECT
        a.subject_id, a.hadm_id, a.ordertime, a.poe_id, a.poe_seq, b.field_name, b.field_value, a.order_type, a.order_subtype, a.transaction_type, a.discontinue_of_poe_id, a.discontinued_by_poe_id, a.order_provider_id, a.order_status,
        
        From `mimic-four-377221.x_mimiciv_hosp.poe`   as a
        LEFT JOIN `mimic-four-377221.x_mimiciv_hosp.poe_detail`   as b
        ON
        a.poe_id=b.poe_id 
        ;




'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
