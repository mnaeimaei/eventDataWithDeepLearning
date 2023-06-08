import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            


create table  `mimic-four-377221.F1_NE_Disorders.S6` as
Select 
Row_number() over (partition by row_str order by icd_code) as num, icd_code
from   `mimic-four-377221.F1_NE_Disorders.S5`

;

ALTER TABLE  `mimic-four-377221.F1_NE_Disorders.S6`
ADD column  row_str STRING ;

UPDATE  `mimic-four-377221.F1_NE_Disorders.S6`
SET row_str ="D"
WHERE row_str is null ;

ALTER TABLE  `mimic-four-377221.F1_NE_Disorders.S6`
ADD column  Final STRING ;

update  `mimic-four-377221.F1_NE_Disorders.S6`
set Final =concat(row_str,num)
where num<10;


update  `mimic-four-377221.P_NonEvents.S6`
set Final =concat(row_str,num)
where num<100;


update  `mimic-four-377221.P_NonEvents.S6`
set Final =concat(row_str,num)
where num<1000;



update  `mimic-four-377221.P_NonEvents.S6`
set Final =concat(row_str,num)
where num<10000;



update  `mimic-four-377221.P_NonEvents.S6`
set Final =concat(row_str,num)
where num>=10000;



'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
