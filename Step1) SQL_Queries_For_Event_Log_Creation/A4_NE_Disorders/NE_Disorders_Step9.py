import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

  ALTER   TABLE `mimic-four-377221.P_NonEvents.K5`  
        ADD    COLUMN  icd_code_syn STRING ;

UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D01"	where icd_code="03812"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D02"	where icd_code="0389"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D03"	where icd_code="04111"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D04"	where icd_code="07999"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D05"	where icd_code="1121"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D06"	where icd_code="1744"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D07"	where icd_code="1963"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D08"	where icd_code="25000"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D09"	where icd_code="2761"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D10"	where icd_code="2763"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D11"	where icd_code="27800"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D12"	where icd_code="27801"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D13"	where icd_code="2809"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D14"	where icd_code="2811"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D15"	where icd_code="28529"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D16"	where icd_code="29680"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D17"	where icd_code="29690"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D18"	where icd_code="30183"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D19"	where icd_code="30781"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D20"	where icd_code="30981"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D21"	where icd_code="311"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D22"	where icd_code="32723"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D23"	where icd_code="33394"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D24"	where icd_code="4019"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D25"	where icd_code="41519"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D26"	where icd_code="4259"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D27"	where icd_code="4538"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D28"	where icd_code="49320"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D29"	where icd_code="49390"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D30"	where icd_code="5070"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D31"	where icd_code="51881"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D32"	where icd_code="53081"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D33"	where icd_code="5609"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D34"	where icd_code="5990"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D35"	where icd_code="6820"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D36"	where icd_code="6929"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D37"	where icd_code="6961"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D38"	where icd_code="7197"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D39"	where icd_code="7280"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D40"	where icd_code="73620"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D41"	where icd_code="78552"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D42"	where icd_code="78659"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D43"	where icd_code="78830"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D44"	where icd_code="83400"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D45"	where icd_code="88100"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D46"	where icd_code="99592"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D47"	where icd_code="99664"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D48"	where icd_code="99731"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D49"	where icd_code="99931"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D50"	where icd_code="A047"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D51"	where icd_code="C50912"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D52"	where icd_code="C778"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D53"	where icd_code="C779"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D54"	where icd_code="C7800"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D55"	where icd_code="C787"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D56"	where icd_code="C7951"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D57"	where icd_code="D684"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D58"	where icd_code="D688"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D59"	where icd_code="E039"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D60"	where icd_code="E46"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D61"	where icd_code="E669"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D62"	where icd_code="E8339"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D63"	where icd_code="E860"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D64"	where icd_code="E871"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D65"	where icd_code="H532"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D66"	where icd_code="I10"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D67"	where icd_code="I427"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D68"	where icd_code="I5022"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D69"	where icd_code="J45909"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D70"	where icd_code="K7290"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D71"	where icd_code="K7469"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D72"	where icd_code="K8020"	;
UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set icd_code_syn="D73"	where icd_code="L409"	;

          ALTER   TABLE `mimic-four-377221.P_NonEvents.K5`  
        ADD    COLUMN  Value INTEGER ;

UPDATE  `mimic-four-377221.P_NonEvents.K5` 	set Value=1	where Value  is NULL 	;

'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
