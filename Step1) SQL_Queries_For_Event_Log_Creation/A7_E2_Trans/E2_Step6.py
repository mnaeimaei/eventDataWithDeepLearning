import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

#################################################################


create table `mimic-four-377221.E2_Trans.Trans4` as
SELECT * FROM `mimic-four-377221.E2_Trans.Trans3` 
where Timestamp is not null;


#################################################################

update  `mimic-four-377221.E2_Trans.Trans4`
set careunit ="NULL"
where careunit is null;

update  `mimic-four-377221.E2_Trans.Trans4`
set careunit2 ="NULL"
where careunit2 is null;



#################################################################

alter table `mimic-four-377221.E2_Trans.Trans4` 
add column a1 INTEGER;

alter table `mimic-four-377221.E2_Trans.Trans4` 
add column a2 INTEGER;

#################################################################
    
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a1=1
            where careunit="PACU";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a1=2
            where careunit="Surgery";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a1=3
            where careunit="Med/Surg";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a1=4
            where careunit="Medicine";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a1=5
            where careunit="Vascular";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a1=6
            where careunit="Neurology";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a1=7
            where careunit="Cardiology";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a1=8
            where careunit="Psychiatry";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a1=9
            where careunit="Transplant";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a1=10
            where careunit="Observation";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a1=11
            where careunit="Med/Surg/GYN";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a1=12
            where careunit="Surgery/Trauma";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a1=13
            where careunit="Cardiac Surgery";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a1=14
            where careunit="Med/Surg/Trauma";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a1=15
            where careunit="Discharge Lounge";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a1=16
            where careunit="Labor & Delivery";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a1=17
            where careunit="Thoracic Surgery";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a1=18
            where careunit="Neuro Intermediate";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a1=19
            where careunit="Hematology/Oncology";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a1=20
            where careunit="Medicine/Cardiology";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a1=21
            where careunit="Trauma SICU (TSICU)";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a1=22
            where careunit="Obstetrics Antepartum";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a1=23
            where careunit="Coronary Care Unit (CCU)";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a1=24
            where careunit="Medical/Surgical (Gynecology)";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a1=25
            where careunit="Cardiology Surgery Intermediate";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a1=26
            where careunit="Emergency Department Observation";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a1=27
            where careunit="Hematology/Oncology Intermediate";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a1=28
            where careunit="Medicine/Cardiology Intermediate";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a1=29
            where careunit="Medical Intensive Care Unit (MICU)";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a1=30
            where careunit="Surgical Intensive Care Unit (SICU)";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a1=31
            where careunit="Surgery/Pancreatic/Biliary/Bariatric";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a1=32
            where careunit="Medical/Surgical Intensive Care Unit (MICU/SICU)";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a1=33
            where careunit="Neuro Stepdown";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a1=34
            where careunit="Obstetrics (Postpartum & Antepartum)";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a1=35
            where careunit="Cardiac Vascular Intensive Care Unit (CVICU)";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a1=36
            where careunit="Neuro Surgical Intensive Care Unit (Neuro SICU)";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a1=37
            where careunit="Obstetrics Postpartum";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a1=38
            where careunit="Unknown";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a1=39
            where careunit="Emergency Department";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a1=0
            where careunit="ND";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a1=99
            where careunit="NULL";
        
##################################################################################

            update `mimic-four-377221.E2_Trans.Trans4`  
            set a2=0
            where careunit2="ND";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a2=1
            where careunit2="PACU";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a2=2
            where careunit2="Surgery";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a2=3
            where careunit2="Med/Surg";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a2=4
            where careunit2="Medicine";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a2=5
            where careunit2="Vascular";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a2=6
            where careunit2="Neurology";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a2=7
            where careunit2="Cardiology";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a2=8
            where careunit2="Psychiatry";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a2=9
            where careunit2="Transplant";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a2=10
            where careunit2="Observation";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a2=11
            where careunit2="Med/Surg/GYN";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a2=12
            where careunit2="Neuro Stepdown";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a2=13
            where careunit2="Surgery/Trauma";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a2=14
            where careunit2="Cardiac Surgery";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a2=15
            where careunit2="Med/Surg/Trauma";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a2=16
            where careunit2="Discharge Lounge";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a2=17
            where careunit2="Labor & Delivery";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a2=18
            where careunit2="Neuro Intermediate";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a2=19
            where careunit2="Hematology/Oncology";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a2=20
            where careunit2="Medicine/Cardiology";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a2=21
            where careunit2="Trauma SICU (TSICU)";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a2=22
            where careunit2="Coronary Care Unit (CCU)";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a2=23
            where careunit2="Medical/Surgical (Gynecology)";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a2=24
            where careunit2="Cardiology Surgery Intermediate";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a2=25
            where careunit2="Emergency Department Observation";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a2=26
            where careunit2="Hematology/Oncology Intermediate";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a2=27
            where careunit2="Medicine/Cardiology Intermediate";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a2=28
            where careunit2="Medical Intensive Care Unit (MICU)";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a2=29
            where careunit2="Surgical Intensive Care Unit (SICU)";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a2=30
            where careunit2="Obstetrics (Postpartum & Antepartum)";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a2=31
            where careunit2="Surgery/Pancreatic/Biliary/Bariatric";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a2=32
            where careunit2="Cardiac Vascular Intensive Care Unit (CVICU)";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a2=33
            where careunit2="Neuro Surgical Intensive Care Unit (Neuro SICU)";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a2=34
            where careunit2="Medical/Surgical Intensive Care Unit (MICU/SICU)";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a2=35
            where careunit2="Thoracic Surgery";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a2=36
            where careunit2="Obstetrics Antepartum";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a2=37
            where careunit2="Unknown";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a2=38
            where careunit2="Obstetrics Postpartum";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a2=39
            where careunit2="Emergency Department";
        
            update `mimic-four-377221.E2_Trans.Trans4`  
            set a2=99
            where careunit2="NULL";

#################################################################


alter table `mimic-four-377221.E2_Trans.Trans4` 
add column Property_Str string;

############################################################

alter table `mimic-four-377221.E2_Trans.Trans4` 
add column Proprty_int string;

############################################################

update `mimic-four-377221.E2_Trans.Trans4` 
set Property_Str=concat("[",careunit,",",careunit2,"]")
where Property_Str is null;

############################################################

update `mimic-four-377221.E2_Trans.Trans4` 
set Proprty_int=concat("[",a1,",",a2,"]")
where Proprty_int is null;
############################################################


alter table `mimic-four-377221.E2_Trans.Trans4` 
add column Type string;

############################################################

update `mimic-four-377221.E2_Trans.Trans4` 
set Type="Transfer"
where Type is null;

#################################################################



'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
