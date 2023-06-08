import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            


        ALTER   TABLE `mimic-four-377221.E4_Micro.Micro_B7`  
        ADD    COLUMN  Activity STRING ;

        UPDATE `mimic-four-377221.E4_Micro.Micro_B7`  
        SET  Activity  = "Mirobiology_Blood_Sample"
        WHERE Activity is null ;

        ############################################################


        ALTER   TABLE `mimic-four-377221.E4_Micro.Micro_B7`  
        ADD    COLUMN  Activity_Synonym STRING ;

        UPDATE `mimic-four-377221.E4_Micro.Micro_B7`  
        SET  Activity_Synonym  = "MBS"
        WHERE Activity_Synonym is null ;

        ############################################################


        ALTER   TABLE `mimic-four-377221.E4_Micro.Micro_B7`  
        ADD    COLUMN  TYPE STRING ;

        UPDATE `mimic-four-377221.E4_Micro.Micro_B7`  
        SET  TYPE  = "Mirobiology_Sample"
        WHERE TYPE is null ;




'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
