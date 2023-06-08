import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

        ALTER   TABLE `mimic-four-377221.E6_BloodGas.bgB13_C0`  
        ADD    COLUMN  Type STRING ;

        UPDATE `mimic-four-377221.E6_BloodGas.bgB13_C0`  
        SET  Type  = "Respiratory_Therapy"
        WHERE Type is null ;




        ################################################################################

                ALTER   TABLE `mimic-four-377221.E6_BloodGas.bgB13_C1`  
        ADD    COLUMN  Type STRING ;

        UPDATE `mimic-four-377221.E6_BloodGas.bgB13_C1`  
        SET  Type  = "CMP"
        WHERE Type is null ;




        ##############################################################################


        ALTER   TABLE `mimic-four-377221.E6_BloodGas.bgB13_C2`  
        ADD    COLUMN  Type STRING ;

        UPDATE `mimic-four-377221.E6_BloodGas.bgB13_C2`  
        SET  Type  = "ABG"
        WHERE Type is null ;




        #############################################################################

        ALTER   TABLE `mimic-four-377221.E6_BloodGas.bgB13_C3`  
        ADD    COLUMN  Type STRING ;

        UPDATE `mimic-four-377221.E6_BloodGas.bgB13_C3`  
        SET  Type  = "ABG_specimen_type"
        WHERE Type is null ;





'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
