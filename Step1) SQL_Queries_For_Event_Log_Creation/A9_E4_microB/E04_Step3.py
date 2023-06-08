import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            


        alter table `mimic-four-377221.E4_MicroB.Micro_C1`  
        ADD COLUMN test_name_Syn INTEGER  ;
        
        alter table `mimic-four-377221.E4_MicroB.Micro_C1`  
        ADD COLUMN org_name_Syn INTEGER  ;
        
        alter table `mimic-four-377221.E4_MicroB.Micro_C1`  
        ADD COLUMN ab_name_Syn STRING  ;
        
        alter table `mimic-four-377221.E4_MicroB.Micro_C1`  
        ADD COLUMN interpretation_Syn INTEGER  ;


'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
