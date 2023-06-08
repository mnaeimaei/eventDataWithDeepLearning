import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            


        alter table `mimic-four-377221.E6_BloodGas.bgA5`
        ADD COLUMN Label_Syn STRING  ;
        

 
    
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label_Syn="Item1"
            where Label="Alveolar-arterial Gradient, Whole Blood";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label_Syn="Item2"
            where Label="Assist/Control, Whole Blood";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label_Syn="Item3"
            where Label="Base Excess, Whole Blood";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label_Syn="Item4"
            where Label="Calculated Bicarbonate, Whole Blood";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label_Syn="Item5"
            where Label="Calculated Total CO2, Whole Blood";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label_Syn="Item6"
            where Label="Carboxyhemoglobin, Whole Blood";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label_Syn="Item7"
            where Label="Chloride, Whole Blood";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label_Syn="Item8"
            where Label="Creatinine, Whole Blood";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label_Syn="Item9"
            where Label="Estimated GFR (MDRD equation), Whole Blood";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label_Syn="Item10"
            where Label="Free Calcium, Whole Blood";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label_Syn="Item11"
            where Label="Glucose, Whole Blood";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label_Syn="Item12"
            where Label="Hematocrit, Calculated, Whole Blood";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label_Syn="Item13"
            where Label="Hemoglobin, Whole Blood";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label_Syn="Item14"
            where Label="Intubated, Whole Blood";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label_Syn="Item15"
            where Label="Lactate, Whole Blood";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label_Syn="Item16"
            where Label="Methemoglobin, Whole Blood";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label_Syn="Item17"
            where Label="O2 Flow, Whole Blood";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label_Syn="Item18"
            where Label="Oxygen Saturation, Whole Blood";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label_Syn="Item19"
            where Label="Oxygen, Whole Blood";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label_Syn="Item20"
            where Label="P50 of Hemoglobin, Whole Blood";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label_Syn="Item21"
            where Label="pCO2, Body Fluid";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label_Syn="Item22"
            where Label="pCO2, Whole Blood";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label_Syn="Item23"
            where Label="PEEP, Whole Blood";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label_Syn="Item24"
            where Label="pH, Body Fluid";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label_Syn="Item25"
            where Label="pH, Whole Blood";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label_Syn="Item26"
            where Label="pO2, Body Fluid, Body Fluid";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label_Syn="Item27"
            where Label="pO2, Whole Blood";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label_Syn="Item28"
            where Label="Potassium, Whole Blood";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label_Syn="Item29"
            where Label="Required O2, Whole Blood";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label_Syn="Item30"
            where Label="Sodium, Whole Blood";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label_Syn="Item31"
            where Label="Specimen Type, Whole Blood";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label_Syn="Item32"
            where Label="Temperature, Whole Blood";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label_Syn="Item33"
            where Label="Tidal Volume, Whole Blood";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label_Syn="Item34"
            where Label="Ventilation Rate, Whole Blood";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label_Syn="Item35"
            where Label="Ventilator, Whole Blood";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label_Syn="Item36"
            where Label="Voided Specimen, Body Fluid";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label_Syn="Item37"
            where Label="Voided Specimen, Whole Blood";
        

        
##################################################################################

    

    
    





'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
