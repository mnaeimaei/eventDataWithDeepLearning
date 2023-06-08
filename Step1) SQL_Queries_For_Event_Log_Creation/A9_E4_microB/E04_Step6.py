import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set ab_name_Syn="ab_00"
            where ab_name="no antibiotic";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set ab_name_Syn="ab_01"
            where ab_name="MEROPENEM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set ab_name_Syn="ab_02"
            where ab_name="TOBRAMYCIN";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set ab_name_Syn="ab_03"
            where ab_name="TRIMETHOPRIM/SULFA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set ab_name_Syn="ab_04"
            where ab_name="CLINDAMYCIN";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set ab_name_Syn="ab_05"
            where ab_name="VANCOMYCIN";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set ab_name_Syn="ab_06"
            where ab_name="CEFEPIME";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set ab_name_Syn="ab_07"
            where ab_name="GENTAMICIN";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set ab_name_Syn="ab_08"
            where ab_name="CEFTAZIDIME";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set ab_name_Syn="ab_09"
            where ab_name="CIPROFLOXACIN";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set ab_name_Syn="ab_10"
            where ab_name="CEFTRIAXONE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set ab_name_Syn="ab_11"
            where ab_name="CEFAZOLIN";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set ab_name_Syn="ab_12"
            where ab_name="PIPERACILLIN/TAZO";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set ab_name_Syn="ab_13"
            where ab_name="AMPICILLIN";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set ab_name_Syn="ab_14"
            where ab_name="PENICILLIN G";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set ab_name_Syn="ab_15"
            where ab_name="LINEZOLID";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set ab_name_Syn="ab_16"
            where ab_name="LEVOFLOXACIN";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set ab_name_Syn="ab_17"
            where ab_name="DAPTOMYCIN";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set ab_name_Syn="ab_18"
            where ab_name="TETRACYCLINE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set ab_name_Syn="ab_19"
            where ab_name="AMPICILLIN/SULBACTAM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set ab_name_Syn="ab_20"
            where ab_name="PIPERACILLIN";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set ab_name_Syn="ab_21"
            where ab_name="CEFUROXIME";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set ab_name_Syn="ab_22"
            where ab_name="AMIKACIN";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set ab_name_Syn="ab_23"
            where ab_name="IMIPENEM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set ab_name_Syn="ab_24"
            where ab_name="ERYTHROMYCIN";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set ab_name_Syn="ab_25"
            where ab_name="NITROFURANTOIN";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set ab_name_Syn="ab_26"
            where ab_name="RIFAMPIN";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set ab_name_Syn="ab_27"
            where ab_name="OXACILLIN";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set ab_name_Syn="ab_99"
            where ab_name="no need antibiotic";


'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
