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
        ADD    COLUMN  Activity STRING ;

        UPDATE `mimic-four-377221.E6_BloodGas.bgB13_C0`  
        SET  Activity  = "Respiratory_Therapy"
        WHERE Activity is null ;


        ALTER   TABLE `mimic-four-377221.E6_BloodGas.bgB13_C0`  
        ADD    COLUMN  Activity_Synonym STRING ;

        UPDATE `mimic-four-377221.E6_BloodGas.bgB13_C0`  
        SET  Activity_Synonym  = "RT"
        WHERE Activity_Synonym is null ;

        ################################################################################

                ALTER   TABLE `mimic-four-377221.E6_BloodGas.bgB13_C1`  
        ADD    COLUMN  Activity STRING ;

        UPDATE `mimic-four-377221.E6_BloodGas.bgB13_C1`  
        SET  Activity  = "CMP_Test"
        WHERE Activity is null ;


        ALTER   TABLE `mimic-four-377221.E6_BloodGas.bgB13_C1`  
        ADD    COLUMN  Activity_Synonym STRING ;

        UPDATE `mimic-four-377221.E6_BloodGas.bgB13_C1`  
        SET  Activity_Synonym  = "CMP"
        WHERE Activity_Synonym is null ;

        ##############################################################################


        ALTER   TABLE `mimic-four-377221.E6_BloodGas.bgB13_C2`  
        ADD    COLUMN  Activity STRING ;

        UPDATE `mimic-four-377221.E6_BloodGas.bgB13_C2`  
        SET  Activity  = "ABG_Test"
        WHERE Activity is null ;


        ALTER   TABLE `mimic-four-377221.E6_BloodGas.bgB13_C2`  
        ADD    COLUMN  Activity_Synonym STRING ;

        UPDATE `mimic-four-377221.E6_BloodGas.bgB13_C2`  
        SET  Activity_Synonym  = "ABG"
        WHERE Activity_Synonym is null ;

        #############################################################################

        ALTER   TABLE `mimic-four-377221.E6_BloodGas.bgB13_C3`  
        ADD    COLUMN  Activity STRING ;

        UPDATE `mimic-four-377221.E6_BloodGas.bgB13_C3`  
        SET  Activity  = "Specimen_Taking"
        WHERE Activity is null ;


        ALTER   TABLE `mimic-four-377221.E6_BloodGas.bgB13_C3`  
        ADD    COLUMN  Activity_Synonym STRING ;

        UPDATE `mimic-four-377221.E6_BloodGas.bgB13_C3`  
        SET  Activity_Synonym  = "ST"
        WHERE Activity_Synonym is null ;




'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
