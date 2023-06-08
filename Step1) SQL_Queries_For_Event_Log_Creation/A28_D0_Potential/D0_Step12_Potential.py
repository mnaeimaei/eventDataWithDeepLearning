import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

alter table `mimic-four-377221.D0_Potential.Nodes` 
add column potential string;

update `mimic-four-377221.D0_Potential.Nodes` 
set potential="pt"
where potential is null;


create table  `mimic-four-377221.D0_Potential.Nodes_output` as
Select 
concat(potential,Row_number() over (partition by potential order by icd_code_syn)) as potential
, icd_code, icd_version, long_title, icd_code_syn, Icd9_Code_Short, potentialEntity
from `mimic-four-377221.D0_Potential.Nodes` ;

drop table `mimic-four-377221.D0_Potential.Nodes` ;

'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
