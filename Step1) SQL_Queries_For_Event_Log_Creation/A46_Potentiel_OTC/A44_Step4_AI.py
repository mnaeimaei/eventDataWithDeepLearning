import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=266096002  where icd_code_syn="D01";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=91302008  where icd_code_syn="D02";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=127331000119101  where icd_code_syn="D03";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=34014006  where icd_code_syn="D04";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=1085006  where icd_code_syn="D05";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=188154003  where icd_code_syn="D06";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=94181007  where icd_code_syn="D07";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=44054006  where icd_code_syn="D08";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=277547006  where icd_code_syn="D09";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=21420006  where icd_code_syn="D10";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=414916001  where icd_code_syn="D11";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=238136002  where icd_code_syn="D12";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=87522002  where icd_code_syn="D13";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=735452003  where icd_code_syn="D14";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=234347009  where icd_code_syn="D15";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=13746004  where icd_code_syn="D16";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=94921000119107  where icd_code_syn="D17";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=20010003  where icd_code_syn="D18";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=398057008  where icd_code_syn="D19";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=47505003  where icd_code_syn="D20";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=35489007  where icd_code_syn="D21";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=78275009  where icd_code_syn="D22";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=32914008  where icd_code_syn="D23";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=59621000  where icd_code_syn="D24";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=441746000  where icd_code_syn="D25";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=195029002  where icd_code_syn="D26";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=111293003  where icd_code_syn="D27";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=10692761000119107  where icd_code_syn="D28";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=195967001  where icd_code_syn="D29";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=196033004  where icd_code_syn="D30";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=65710008  where icd_code_syn="D31";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=249496004  where icd_code_syn="D32";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=81060008  where icd_code_syn="D33";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=68566005  where icd_code_syn="D34";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=200645004  where icd_code_syn="D35";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=40275004  where icd_code_syn="D36";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=9014002  where icd_code_syn="D37";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=1156409003  where icd_code_syn="D38";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=29689003  where icd_code_syn="D39";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=26517000  where icd_code_syn="D40";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=76571007  where icd_code_syn="D41";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=59021001  where icd_code_syn="D42";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=236667007  where icd_code_syn="D43";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=11792671000119105  where icd_code_syn="D44";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=125649002  where icd_code_syn="D45";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=449084002  where icd_code_syn="D46";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=473092007  where icd_code_syn="D47";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=429271009  where icd_code_syn="D48";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=736152001  where icd_code_syn="D49";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=43752006  where icd_code_syn="D50";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=372064008  where icd_code_syn="D51";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=303201005  where icd_code_syn="D52";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=94392001  where icd_code_syn="D53";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=94391008  where icd_code_syn="D54";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=93870000  where icd_code_syn="D55";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=94222008  where icd_code_syn="D56";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=25904003  where icd_code_syn="D57";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=267272006  where icd_code_syn="D58";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=40930008  where icd_code_syn="D59";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=238107002  where icd_code_syn="D60";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=414916001  where icd_code_syn="D61";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=87049008  where icd_code_syn="D62";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=34095006  where icd_code_syn="D63";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=267447008  where icd_code_syn="D64";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=24982008  where icd_code_syn="D65";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=59621000  where icd_code_syn="D66";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=72972005  where icd_code_syn="D67";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=441481004  where icd_code_syn="D68";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=195967001  where icd_code_syn="D69";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=59927004  where icd_code_syn="D70";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=19943007  where icd_code_syn="D71";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=235919008  where icd_code_syn="D72";
update `mimic-four-377221.C0_Potential_OCT.PO1`  set OTC=9014002  where icd_code_syn="D73";


'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
