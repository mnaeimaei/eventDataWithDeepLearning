import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            


            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set interpretation_Syn=0
            where interpretation="no interpretation";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set interpretation_Syn=1
            where interpretation="S";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set interpretation_Syn=2
            where interpretation="I";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set interpretation_Syn=3
            where interpretation="R";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set interpretation_Syn=8
            where interpretation="no need interpretation";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set interpretation_Syn=4
            where interpretation="P";

'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
