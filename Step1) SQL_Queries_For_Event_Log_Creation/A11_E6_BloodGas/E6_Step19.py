import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

create table `mimic-four-377221.E6_BloodGas.bgB10` as

SELECT
e.Label,
e.Label_Syn,
b.Cluster as Cluster4
from

FROM `mimic-four-377221.E6_BloodGas.bgA9` a
left join `mimic-four-377221.E6_BloodGas.bgA9_K4`b
on a.Label_Syn=b.Items

'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
