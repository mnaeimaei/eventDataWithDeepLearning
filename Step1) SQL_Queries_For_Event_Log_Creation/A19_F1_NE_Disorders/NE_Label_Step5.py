import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

create table `mimic-four-377221.F1_NE_Disorders.S5` as
SELECT distinct icd_code  FROM `mimic-four-377221.F1_NE_Disorders.S4` 
order by icd_code;


ALTER TABLE  `mimic-four-377221.F1_NE_Disorders.S5`
ADD column  row_str STRING ;

UPDATE  `mimic-four-377221.F1_NE_Disorders.S5`
SET row_str ="A"
WHERE row_str is null ;



'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
