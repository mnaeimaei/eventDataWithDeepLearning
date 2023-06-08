import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

               alter table `mimic-four-377221.E6_BloodGas.bgA5`
        ADD COLUMN Label2 STRING  ;


            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label2="Alveolar_arterial_Gradient_Whole_Blood"
            where Label="Alveolar-arterial Gradient, Whole Blood";

            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label2="Assist_Control_Whole_Blood"
            where Label="Assist/Control, Whole Blood";

            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label2="Base_Excess_Whole_Blood"
            where Label="Base Excess, Whole Blood";

            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label2="Calculated_Bicarbonate_Whole_Blood"
            where Label="Calculated Bicarbonate, Whole Blood";

            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label2="Calculated_Total_CO2_Whole_Blood"
            where Label="Calculated Total CO2, Whole Blood";

            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label2="Carboxyhemoglobin_Whole_Blood"
            where Label="Carboxyhemoglobin, Whole Blood";

            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label2="Chloride_Whole_Blood"
            where Label="Chloride, Whole Blood";

            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label2="Creatinine_Whole_Blood"
            where Label="Creatinine, Whole Blood";

            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label2="Estimated_GFR_Whole_Blood"
            where Label="Estimated GFR (MDRD equation), Whole Blood";

            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label2="Free_Calcium_Whole_Blood"
            where Label="Free Calcium, Whole Blood";

            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label2="Glucose_Whole_Blood"
            where Label="Glucose, Whole Blood";

            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label2="Hematocrit_Calculated_Whole_Blood"
            where Label="Hematocrit, Calculated, Whole Blood";

            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label2="Hemoglobin_Whole_Blood"
            where Label="Hemoglobin, Whole Blood";

            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label2="Intubated_Whole_Blood"
            where Label="Intubated, Whole Blood";

            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label2="Lactate_Whole_Blood"
            where Label="Lactate, Whole Blood";

            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label2="Methemoglobin_Whole_Blood"
            where Label="Methemoglobin, Whole Blood";

            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label2="O2_Flow_Whole_Blood"
            where Label="O2 Flow, Whole Blood";

            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label2="Oxygen_Saturation_Whole_Blood"
            where Label="Oxygen Saturation, Whole Blood";

            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label2="Oxygen_Whole_Blood"
            where Label="Oxygen, Whole Blood";

            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label2="P50_of_Hemoglobin_Whole_Blood"
            where Label="P50 of Hemoglobin, Whole Blood";

            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label2="pCO2_Body_Fluid"
            where Label="pCO2, Body Fluid";

            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label2="pCO2_Whole_Blood"
            where Label="pCO2, Whole Blood";

            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label2="PEEP_Whole_Blood"
            where Label="PEEP, Whole Blood";

            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label2="pH_Body_Fluid"
            where Label="pH, Body Fluid";

            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label2="pH_Whole_Blood"
            where Label="pH, Whole Blood";

            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label2="pO2_Body_Fluid_Body_Fluid"
            where Label="pO2, Body Fluid, Body Fluid";

            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label2="pO2_Whole_Blood"
            where Label="pO2, Whole Blood";

            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label2="Potassium_Whole_Blood"
            where Label="Potassium, Whole Blood";

            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label2="Required_O2_Whole_Blood"
            where Label="Required O2, Whole Blood";

            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label2="Sodium_Whole_Blood"
            where Label="Sodium, Whole Blood";

            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label2="Specimen_Type_Whole_Blood"
            where Label="Specimen Type, Whole Blood";

            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label2="Temperature_Whole_Blood"
            where Label="Temperature, Whole Blood";

            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label2="Tidal_Volume_Whole_Blood"
            where Label="Tidal Volume, Whole Blood";

            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label2="Ventilation_Rate_Whole_Blood"
            where Label="Ventilation Rate, Whole Blood";

            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label2="Ventilator_Whole_Blood"
            where Label="Ventilator, Whole Blood";

            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label2="Voided_Specimen_Body_Fluid"
            where Label="Voided Specimen, Body Fluid";

            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Label2="Voided_Specimen_Whole_Blood"
            where Label="Voided Specimen, Whole Blood";



##################################################################################










'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
