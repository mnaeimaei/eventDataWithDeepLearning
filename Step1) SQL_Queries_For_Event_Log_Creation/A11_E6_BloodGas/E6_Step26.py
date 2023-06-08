import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            


        
        
        
        
        
        CREATE TABLE  `mimic-four-377221.E6_BloodGas.bgB14_C0`   AS
        SELECT
        a.rowNum, a.subject_id, a.hadm_id, 
        b.Activity, b.Activity_Synonym,         
        a.Timstamp,
        b.Type, b.Proprty_int, b.Property_Str,
        
        b.Item1, b.Item2, b.Item4, b.Item6, b.Item8, b.Item9, b.Item14, b.Item16, b.Item17, b.Item18, b.Item19, b.Item20, b.Item21, b.Item23, b.Item24, b.Item26, b.Item29, b.Item32, b.Item33, b.Item34, b.Item35, b.Item36, b.Item37, b.Alveolar_arterial_Gradient_Whole_Blood, b.Assist_Control_Whole_Blood, b.Calculated_Bicarbonate_Whole_Blood, b.Carboxyhemoglobin_Whole_Blood, b.Creatinine_Whole_Blood, b.Estimated_GFR_Whole_Blood, b.Intubated_Whole_Blood, b.Methemoglobin_Whole_Blood, b.O2_Flow_Whole_Blood, b.Oxygen_Saturation_Whole_Blood, b.Oxygen_Whole_Blood, b.P50_of_Hemoglobin_Whole_Blood, b.pCO2_Body_Fluid, b.PEEP_Whole_Blood, b.pH_Body_Fluid, b.pO2_Body_Fluid_Body_Fluid, b.Required_O2_Whole_Blood, b.Temperature_Whole_Blood, b.Tidal_Volume_Whole_Blood, b.Ventilation_Rate_Whole_Blood, b.Ventilator_Whole_Blood, b.Voided_Specimen_Body_Fluid, b.Voided_Specimen_Whole_Blood
        
        From `mimic-four-377221.E6_BloodGas.bgA6`   as a
        LEFT JOIN `mimic-four-377221.E6_BloodGas.bgB13_C0`   as b
        ON
        a.rowNum=b.rowNum 
        ;
        
    ###############################################################################
        
        CREATE TABLE  `mimic-four-377221.E6_BloodGas.bgB14_C1`   AS
        SELECT
        a.rowNum, a.subject_id, a.hadm_id, 
        b.Activity, b.Activity_Synonym,         
        a.Timstamp,
        b.Type, b.Proprty_int, b.Property_Str,
        b.Item7, b.Item10, b.Item11, b.Item12, b.Item13, b.Item15, b.Item28, b.Item30, b.Chloride_Whole_Blood, b.Free_Calcium_Whole_Blood, b.Glucose_Whole_Blood, b.Hematocrit_Calculated_Whole_Blood, b.Hemoglobin_Whole_Blood, b.Lactate_Whole_Blood, b.Potassium_Whole_Blood, b.Sodium_Whole_Blood,

        
        From `mimic-four-377221.E6_BloodGas.bgA6`   as a
        LEFT JOIN `mimic-four-377221.E6_BloodGas.bgB13_C1`   as b
        ON
        a.rowNum=b.rowNum 
        ;
        
     ###############################################################################
        
        CREATE TABLE  `mimic-four-377221.E6_BloodGas.bgB14_C2`   AS
        SELECT
        a.rowNum, a.subject_id, a.hadm_id, 
        b.Activity, b.Activity_Synonym,         
        a.Timstamp,
        b.Type, b.Proprty_int, b.Property_Str,
        b.Item3, b.Item5, b.Item22, b.Item25, b.Item27, b.Base_Excess_Whole_Blood, b.Calculated_Total_CO2_Whole_Blood, b.pCO2_Whole_Blood, b.pH_Whole_Blood, b.pO2_Whole_Blood,

        
        From `mimic-four-377221.E6_BloodGas.bgA6`   as a
        LEFT JOIN `mimic-four-377221.E6_BloodGas.bgB13_C2`   as b
        ON
        a.rowNum=b.rowNum 
        ;
        
        
     ###############################################################################
        
        CREATE TABLE  `mimic-four-377221.E6_BloodGas.bgB14_C3`   AS
        SELECT
        a.rowNum, a.subject_id, a.hadm_id, 
        b.Activity, b.Activity_Synonym,         
        a.Timstamp,
        b.Type, b.Proprty_int, b.Property_Str,
        b.Item31, b.Specimen_Type_Whole_Blood,

        
        From `mimic-four-377221.E6_BloodGas.bgA6`   as a
        LEFT JOIN `mimic-four-377221.E6_BloodGas.bgB13_C3`   as b
        ON
        a.rowNum=b.rowNum 
        ;



'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
