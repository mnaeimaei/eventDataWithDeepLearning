import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

alter table `mimic-four-377221.D0_Potential.Potential_Entity_all` 
add column Enpo string;

update `mimic-four-377221.D0_Potential.Potential_Entity_all` 
set Enpo="ep"
where Enpo is null;


create table  `mimic-four-377221.D0_Potential.Potential_Entity_Aggr` as
Select 
concat(Enpo,Row_number() over (partition by Enpo order by icd_code_syn)) as EnpoID
, Entity1_Origin, Entity1_ID, Entity2_Origin, Entity2_ID, icd_code, icd_code_syn
from `mimic-four-377221.D0_Potential.Potential_Entity_all` ;

drop table `mimic-four-377221.D0_Potential.Potential_Entity_all` ;
'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
