import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

###########################################################################################
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a1=0
            where admission_location="ND";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a1=1
            where admission_location="PROCEDURE SITE";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a1=2
            where admission_location="TRANSFER FROM HOSPITAL";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a1=3
            where admission_location="PHYSICIAN REFERRAL";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a1=4
            where admission_location="INTERNAL TRANSFER TO OR FROM PSYCH";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a1=5
            where admission_location="WALK-IN/SELF REFERRAL";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a1=6
            where admission_location="TRANSFER FROM SKILLED NURSING FACILITY";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a1=7
            where admission_location="EMERGENCY ROOM";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a1=8
            where admission_location="CLINIC REFERRAL";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a1=9
            where admission_location="PACU";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a1=10
            where admission_location="INFORMATION NOT AVAILABLE";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a1=11
            where admission_location="AMBULATORY SURGERY TRANSFER";

###########################################################################################

    
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a2=0
            where admission_type="ND";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a2=1
            where admission_type="EW EMER.";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a2=2
            where admission_type="AMBULATORY OBSERVATION";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a2=3
            where admission_type="DIRECT OBSERVATION";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a2=4
            where admission_type="URGENT";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a2=5
            where admission_type="OBSERVATION ADMIT";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a2=6
            where admission_type="EU OBSERVATION";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a2=7
            where admission_type="DIRECT EMER.";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a2=8
            where admission_type="ELECTIVE";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a2=9
            where admission_type="SURGICAL SAME DAY ADMISSION";
        
########################################################################################

            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a3=0
            where discharge_location="ND";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a3=99
            where discharge_location="NULL";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a3=1
            where discharge_location="DIED";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a3=2
            where discharge_location="HOME";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a3=3
            where discharge_location="REHAB";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a3=4
            where discharge_location="HOSPICE";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a3=5
            where discharge_location="ACUTE HOSPITAL";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a3=6
            where discharge_location="AGAINST ADVICE";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a3=7
            where discharge_location="OTHER FACILITY";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a3=8
            where discharge_location="PSYCH FACILITY";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a3=9
            where discharge_location="ASSISTED LIVING";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a3=10
            where discharge_location="HOME HEALTH CARE";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a3=11
            where discharge_location="SKILLED NURSING FACILITY";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a3=12
            where discharge_location="CHRONIC/LONG TERM ACUTE CARE";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a3=13
            where discharge_location="HEALTHCARE FACILITY";
        



########################################################################################


            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a4=0
            where prev_service="ND";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a4=99
            where prev_service="NULL";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a4=1
            where prev_service="MED";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a4=2
            where prev_service="SURG";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a4=3
            where prev_service="OMED";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a4=4
            where prev_service="NSURG";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a4=5
            where prev_service="CMED";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a4=6
            where prev_service="TSURG";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a4=7
            where prev_service="TRAUM";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a4=8
            where prev_service="NMED";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a4=9
            where prev_service="GYN";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a4=10
            where prev_service="ORTHO";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a4=11
            where prev_service="VSURG";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a4=12
            where prev_service="CSURG";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a4=13
            where prev_service="GU";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a4=14
            where prev_service="PSURG";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a4=15
            where prev_service="EYE";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a4=16
            where prev_service="ENT";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a4=17
            where prev_service="OBS";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a4=18
            where prev_service="PSYCH";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a4=19
            where prev_service="DENT";



########################################################################################


            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a5=0
            where curr_service="ND";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a5=1
            where curr_service="SURG";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a5=2
            where curr_service="CSURG";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a5=3
            where curr_service="MED";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a5=4
            where curr_service="VSURG";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a5=5
            where curr_service="NMED";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a5=6
            where curr_service="OMED";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a5=7
            where curr_service="OBS";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a5=8
            where curr_service="CMED";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a5=9
            where curr_service="NSURG";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a5=10
            where curr_service="TSURG";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a5=11
            where curr_service="PSURG";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a5=12
            where curr_service="ORTHO";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a5=13
            where curr_service="GYN";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a5=14
            where curr_service="PSYCH";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a5=15
            where curr_service="ENT";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a5=16
            where curr_service="TRAUM";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a5=17
            where curr_service="GU";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a5=18
            where curr_service="DENT";
        
            update `mimic-four-377221.E1_AdmSer.TabF`  
            set a5=19
            where curr_service="EYE";
        


########################################################################################
'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
