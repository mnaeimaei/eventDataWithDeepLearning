import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

        CREATE TABLE  `mimic-four-377221.D0_Potential.PE`   AS
        SELECT DISTINCT * FROM  `mimic-four-377221.D0_Potential.Potential_Entity_3`  ;

        drop table `mimic-four-377221.D0_Potential.Potential_Entity` ;
        drop table `mimic-four-377221.D0_Potential.Potential_Entity_2` ;
        drop table `mimic-four-377221.D0_Potential.Potential_Entity_3` ;



'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
