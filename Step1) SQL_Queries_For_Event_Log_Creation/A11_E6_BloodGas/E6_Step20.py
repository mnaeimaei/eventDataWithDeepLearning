
#Based On Best Clustring and Domain Knowledge

import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

        ALTER   TABLE `mimic-four-377221.E6_BloodGas.bgB10`  
        ADD    COLUMN  Activity STRING ;

        UPDATE `mimic-four-377221.E6_BloodGas.bgB10`  
        SET  Activity  = "Respiratory_Therapy"
        WHERE Cluster4=0 ;

        UPDATE `mimic-four-377221.E6_BloodGas.bgB10`  
        SET  Activity  = "CMP_Test"
        WHERE Cluster4=1 ;

        UPDATE `mimic-four-377221.E6_BloodGas.bgB10`  
        SET  Activity  = "ABG_Test"
        WHERE Cluster4=2 ;

        UPDATE `mimic-four-377221.E6_BloodGas.bgB10`  
        SET  Activity  = "SpecimenType"
        WHERE Cluster4=3 ;




'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
