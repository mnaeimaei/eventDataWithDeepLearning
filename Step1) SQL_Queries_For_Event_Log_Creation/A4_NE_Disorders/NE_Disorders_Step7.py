import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

create table `mimic-four-377221.P_NonEvents.K4` as
SELECT * FROM `mimic-four-377221.P_NonEvents.icdCM1` 
Where icd_code= "78552" or
icd_code= "88100" or
icd_code= "7197" or
icd_code= "6820" or
icd_code= "30183" or
icd_code= "2809" or
icd_code= "53081" or
icd_code= "311" or
icd_code= "78830" or
icd_code= "83400" or
icd_code= "28529" or
icd_code= "41519" or
icd_code= "25000" or
icd_code= "03812" or
icd_code= "5990" or
icd_code= "29680" or
icd_code= "2763" or
icd_code= "1121" or
icd_code= "99731" or
icd_code= "99931" or
icd_code= "2761" or
icd_code= "2811" or
icd_code= "5609" or
icd_code= "27801" or
icd_code= "04111" or
icd_code= "78659" or
icd_code= "4259" or
icd_code= "49320" or
icd_code= "4538" or
icd_code= "30781" or
icd_code= "99664" or
icd_code= "73620" or
icd_code= "27800" or
icd_code= "29690" or
icd_code= "7280" or
icd_code= "33394" or
icd_code= "51881" or
icd_code= "1744" or
icd_code= "5070" or
icd_code= "6929" or
icd_code= "32723" or
icd_code= "1963" or
icd_code= "30981" or
icd_code= "4019" or
icd_code= "0389" or
icd_code= "99592" or
icd_code= "6961" or
icd_code= "49390" or
icd_code= "07999" or
icd_code= "A047" or
icd_code= "C779" or
icd_code= "C787" or
icd_code= "C7951" or
icd_code= "C7800" or
icd_code= "C50912" or
icd_code= "C778" or
icd_code= "D684" or
icd_code= "D688" or
icd_code= "E871" or
icd_code= "E8339" or
icd_code= "E46" or
icd_code= "E669" or
icd_code= "E860" or
icd_code= "E039" or
icd_code= "H532" or
icd_code= "I5022" or
icd_code= "I10" or
icd_code= "I427" or
icd_code= "J45909" or
icd_code= "K7469" or
icd_code= "K8020" or
icd_code= "K7290" or
icd_code= "L409"

'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
