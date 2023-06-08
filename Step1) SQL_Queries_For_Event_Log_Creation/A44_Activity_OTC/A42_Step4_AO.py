import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

update `mimic-four-377221.C0_Activity_OTC.A1` 
set OTC=60170009
where Activity_Synonym="ABG";

update `mimic-four-377221.C0_Activity_OTC.A1` 
set OTC=371361000119107
where Activity_Synonym="CMP";

update `mimic-four-377221.C0_Activity_OTC.A1` 
set OTC=32485007
where Activity_Synonym="HA";

update `mimic-four-377221.C0_Activity_OTC.A1` 
set OTC=183676005
where Activity_Synonym="DIH";

update `mimic-four-377221.C0_Activity_OTC.A1` 
set OTC=308283009
where Activity_Synonym="DFH";

update `mimic-four-377221.C0_Activity_OTC.A1` 
set OTC=4525004
where Activity_Synonym="RFE";

update `mimic-four-377221.C0_Activity_OTC.A1` 
set OTC=306563004
where Activity_Synonym="DFE";

update `mimic-four-377221.C0_Activity_OTC.A1` 
set OTC=37729005
where Activity_Synonym="TBS";

update `mimic-four-377221.C0_Activity_OTC.A1` 
set OTC=225746001
where Activity_Synonym="SOO";

update `mimic-four-377221.C0_Activity_OTC.A1` 
set OTC=225746001
where Activity_Synonym="DOO";

update `mimic-four-377221.C0_Activity_OTC.A1` 
set OTC=225746001
where Activity_Synonym="AIN";

update `mimic-four-377221.C0_Activity_OTC.A1` 
set OTC=225746001
where Activity_Synonym="TIN";

update `mimic-four-377221.C0_Activity_OTC.A1` 
set OTC=225746001
where Activity_Synonym="TOO";

update `mimic-four-377221.C0_Activity_OTC.A1` 
set OTC=225746001
where Activity_Synonym="DIN";


update `mimic-four-377221.C0_Activity_OTC.A1` 
set OTC=225746001
where Activity_Synonym="AOO";

update `mimic-four-377221.C0_Activity_OTC.A1` 
set OTC=225746001
where Activity_Synonym="SIN";

update `mimic-four-377221.C0_Activity_OTC.A1` 
set OTC=119297000
where Activity_Synonym="ST";

update `mimic-four-377221.C0_Activity_OTC.A1` 
set OTC=165337006
where Activity_Synonym="MBS";

update `mimic-four-377221.C0_Activity_OTC.A1` 
set OTC=19851009
where Activity_Synonym="MTR";

update `mimic-four-377221.C0_Activity_OTC.A1` 
set OTC=53950000
where Activity_Synonym="RT";



'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
