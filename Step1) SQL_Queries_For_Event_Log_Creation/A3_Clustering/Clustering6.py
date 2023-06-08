import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            



        ALTER TABLE  `mimic-four-377221.Q_ClusA.Q5_AdmissionPatient`   
        ADD COLUMN Died INTEGER;
        
        UPDATE  `mimic-four-377221.Q_ClusA.Q5_AdmissionPatient`   
        set Died=0
        where dod is not null;
        
        UPDATE   `mimic-four-377221.Q_ClusA.Q5_AdmissionPatient`   
        set Died=1
        where dod is null;
        
        ###############################################################
        
        ALTER TABLE  `mimic-four-377221.Q_ClusA.Q5_AdmissionPatient`   
        ADD COLUMN gender_Int INTEGER;
        
        UPDATE  `mimic-four-377221.Q_ClusA.Q5_AdmissionPatient`   
        set gender_Int=0
        where gender="F";
        
        UPDATE   `mimic-four-377221.Q_ClusA.Q5_AdmissionPatient`   
        set gender_Int=1
        where gender="M" ;


'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
