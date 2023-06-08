import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            


        ALTER TABLE `mimic-four-377221.D0_Potential.PE` 
ADD column  ER STRING ;


UPDATE `mimic-four-377221.D0_Potential.PE` 
SET ER ="A"
WHERE ER is null ;

        CREATE TABLE  `mimic-four-377221.D0_Potential.Potential_Entity`   AS

Select 
Row_number() over (partition by ER) as ER, rowNum, subject_id,
hadm_id,
icd_code,
icd_code_syn,
Entity1_Origin,
Entity1_ID,
Entity2_Origin,
Entity2_ID
from `mimic-four-377221.D0_Potential.PE` ;



drop table `mimic-four-377221.D0_Potential.PE` ;


'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
