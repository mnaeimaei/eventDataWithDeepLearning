import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

create table `mimic-four-377221.C0_Activity_Event.BondAll` as
SELECT 
a.Activity,
a.Activity_Synonym,
a.Activity_Origin,
a.Activity_Value_ID,
b.OTC

FROM `mimic-four-377221.C0_Activity_Event.BondAll_2` a
left join `mimic-four-377221.C0_Activity_OTC.A1` b
on
a.Activity=b.Activity and
a.Activity_Synonym=b.Activity_Synonym and
a.Activity_Origin=b.Activity_Origin;

drop table `mimic-four-377221.C0_Activity_Event.BondAll_2` ;


'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
