import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

CREATE TABLE  `mimic-four-377221.E6_BloodGas.bgB14_E0_RT`   AS
SELECT distinct

rowNum,
Label2,
Value


FROM `mimic-four-377221.E6_BloodGas.bgA6`
where   Label_Syn="Item1"
or   Label_Syn="Item2"
or   Label_Syn="Item4"
or   Label_Syn="Item6"
or   Label_Syn="Item8"
or   Label_Syn="Item9"
or   Label_Syn="Item14"
or   Label_Syn="Item16"
or   Label_Syn="Item17"
or   Label_Syn="Item18"
or   Label_Syn="Item19"
or   Label_Syn="Item20"
or   Label_Syn="Item21"
or   Label_Syn="Item23"
or   Label_Syn="Item24"
or   Label_Syn="Item26"
or   Label_Syn="Item29"
or   Label_Syn="Item32"
or   Label_Syn="Item33"
or   Label_Syn="Item34"
or   Label_Syn="Item35"
or   Label_Syn="Item36"
or   Label_Syn="Item37"



'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
