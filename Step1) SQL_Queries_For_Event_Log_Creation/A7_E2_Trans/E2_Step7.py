import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

create table `mimic-four-377221.E2_Trans.TabF` as

SELECT
subject_id, hadm_id, transfer_id, Timestamp, act1 as Activity

, act11 as Activity_Synonym
, careunit as into_careunit
, careunit2 as out_of_careunit
, a1, a2, Property_Str, Proprty_int, Type


  FROM `mimic-four-377221.E2_Trans.Trans4`;

#########################################################################

drop table `mimic-four-377221.E2_Trans.Trans2` ;
drop table `mimic-four-377221.E2_Trans.Trans3` ;
drop table `mimic-four-377221.E2_Trans.Trans4` ;



'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
