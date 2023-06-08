import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

create table `mimic-four-377221.E6_BloodGas.bgB11_C3` as
SELECT distinct
rowNum,Item31
FROM `mimic-four-377221.E6_BloodGas.bgA7` ;


create table `mimic-four-377221.E6_BloodGas.bgB11_C2` as
SELECT distinct
rowNum,
Item3,Item5,Item22,Item25,Item27,
FROM `mimic-four-377221.E6_BloodGas.bgA7` ;


create table `mimic-four-377221.E6_BloodGas.bgB11_C1` as
SELECT distinct
rowNum,
Item7,Item10,Item11,Item12,Item13,Item15,Item28,Item30
FROM `mimic-four-377221.E6_BloodGas.bgA7` ;


create table `mimic-four-377221.E6_BloodGas.bgB11_C0` as
SELECT distinct
rowNum,
Item1,Item2,Item4,Item6,Item8,Item9,Item14,Item16,Item17,Item18,Item19,Item20,
Item21,Item23,Item24,Item26,Item29,Item32,Item33,Item34,Item35,Item36,Item37,
FROM `mimic-four-377221.E6_BloodGas.bgA7` ;


'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
