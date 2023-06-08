import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            


ALTER TABLE  `mimic-four-377221.C0_EventLog.sub` 
ADD column  col STRING ;

UPDATE  `mimic-four-377221.C0_EventLog.sub` 
SET col ="A"
WHERE col is null ;


CREATE TABLE  `mimic-four-377221.C0_EventLog.sub2`   AS
Select 
Row_number() over (partition by col order by subject_id) as RRR, subject_id
from  `mimic-four-377221.C0_EventLog.sub` ;

drop table `mimic-four-377221.C0_EventLog.sub` ;


'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
