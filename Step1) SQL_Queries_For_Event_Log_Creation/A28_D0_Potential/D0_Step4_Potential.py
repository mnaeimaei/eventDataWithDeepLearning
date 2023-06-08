import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

alter table `mimic-four-377221.D0_Potential.Nodes` 
add column Icd9_Code_Short int;

alter table `mimic-four-377221.D0_Potential.Nodes` 
add column potentialEntity string;

update `mimic-four-377221.D0_Potential.Nodes` 
set potentialEntity="disorder"
where potentialEntity is null;

#########################################################################

update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=1
where icd_code_syn="D01";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=2
where icd_code_syn="D02";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=3
where icd_code_syn="D03";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=4
where icd_code_syn="D04";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=5
where icd_code_syn="D05";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=6
where icd_code_syn="D06";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=7
where icd_code_syn="D07";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=8
where icd_code_syn="D08";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=9
where icd_code_syn="D09";



update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=10
where icd_code_syn="D10";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=11
where icd_code_syn="D11";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=12
where icd_code_syn="D12";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=13
where icd_code_syn="D13";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=14
where icd_code_syn="D14";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=15
where icd_code_syn="D15";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=16
where icd_code_syn="D16";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=17
where icd_code_syn="D17";




update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=18
where icd_code_syn="D18";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=19
where icd_code_syn="D19";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=20
where icd_code_syn="D20";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=21
where icd_code_syn="D21";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=22
where icd_code_syn="D22";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=23
where icd_code_syn="D23";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=24
where icd_code_syn="D24";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=25
where icd_code_syn="D25";




update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=26
where icd_code_syn="D26";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=27
where icd_code_syn="D27";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=28
where icd_code_syn="D28";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=29
where icd_code_syn="D29";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=30
where icd_code_syn="D30";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=31
where icd_code_syn="D31";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=32
where icd_code_syn="D32";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=33
where icd_code_syn="D33";




update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=34
where icd_code_syn="D34";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=35
where icd_code_syn="D35";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=36
where icd_code_syn="D36";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=37
where icd_code_syn="D37";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=38
where icd_code_syn="D38";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=39
where icd_code_syn="D39";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=40
where icd_code_syn="D40";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=41
where icd_code_syn="D41";




update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=42
where icd_code_syn="D42";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=43
where icd_code_syn="D43";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=44
where icd_code_syn="D44";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=45
where icd_code_syn="D45";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=46
where icd_code_syn="D46";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=47
where icd_code_syn="D47";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=48
where icd_code_syn="D48";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=49
where icd_code_syn="D49";




update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=50
where icd_code_syn="D50";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=51
where icd_code_syn="D51";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=52
where icd_code_syn="D52";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=53
where icd_code_syn="D53";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=54
where icd_code_syn="D54";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=55
where icd_code_syn="D55";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=56
where icd_code_syn="D56";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=57
where icd_code_syn="D57";




update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=58
where icd_code_syn="D58";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=59
where icd_code_syn="D59";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=60
where icd_code_syn="D60";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=61
where icd_code_syn="D61";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=62
where icd_code_syn="D62";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=63
where icd_code_syn="D63";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=64
where icd_code_syn="D64";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=65
where icd_code_syn="D65";



update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=66
where icd_code_syn="D66";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=67
where icd_code_syn="D67";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=68
where icd_code_syn="D68";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=69
where icd_code_syn="D69";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=70
where icd_code_syn="D70";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=71
where icd_code_syn="D71";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=72
where icd_code_syn="D72";


update `mimic-four-377221.D0_Potential.Nodes` 
set Icd9_Code_Short=73
where icd_code_syn="D73";










'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
