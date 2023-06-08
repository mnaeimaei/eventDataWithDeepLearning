import os
from google.cloud import bigquery

symPath = '../gcKey/SNOMED_CT_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

###################################
################################### Go to SQL \ Query 10_SCT
###################################
# Perform a query.
query1 = f'''            

CREATE TABLE  `snomed-ct-377221.SCT_3.PaperD`   AS 
SELECT distinct
a.s0 as conceptId,
b.termA,
b.termB,
b.Semanti_tags,
b.ConceptType
FROM `snomed-ct-377221.SCT_3.PaperC` a
left join `snomed-ct-377221.SCT_2.B_3` b
on
a.s0=b.conceptId


'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
