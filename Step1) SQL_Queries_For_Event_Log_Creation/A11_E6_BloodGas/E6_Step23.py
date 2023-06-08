import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

        ALTER   TABLE `mimic-four-377221.E6_BloodGas.bgB13_C0`  
        ADD    COLUMN  Proprty_int   STRING ;

        UPDATE `mimic-four-377221.E6_BloodGas.bgB13_C0`  
        SET  Proprty_int  = concat("[",Item1, "," ,Item2, "," ,Item4, "," ,Item6, "," ,Item8, "," ,Item9, "," ,Item14, "," ,Item16, "," ,Item17, "," ,Item18, "," ,Item19, "," ,Item20, "," ,Item21, "," ,Item23, "," ,Item24, "," ,Item26, "," ,Item29, "," ,Item32, "," ,Item33, "," ,Item34, "," ,Item35, "," ,Item36, "," ,Item37,"]")
        WHERE Proprty_int  is null ;



ALTER   TABLE `mimic-four-377221.E6_BloodGas.bgB13_C0`
ADD    COLUMN  Property_Str   STRING ;

UPDATE `mimic-four-377221.E6_BloodGas.bgB13_C0`
SET  Property_Str  = concat("[",Alveolar_arterial_Gradient_Whole_Blood, "," ,Assist_Control_Whole_Blood, "," ,Calculated_Bicarbonate_Whole_Blood, "," ,Carboxyhemoglobin_Whole_Blood, "," ,Creatinine_Whole_Blood, "," ,Estimated_GFR_Whole_Blood, "," ,Intubated_Whole_Blood, "," ,Methemoglobin_Whole_Blood, "," ,O2_Flow_Whole_Blood, "," ,Oxygen_Saturation_Whole_Blood, "," ,Oxygen_Whole_Blood, "," ,P50_of_Hemoglobin_Whole_Blood, "," ,pCO2_Body_Fluid, "," ,PEEP_Whole_Blood, "," ,pH_Body_Fluid, "," ,pO2_Body_Fluid_Body_Fluid, "," ,Required_O2_Whole_Blood, "," ,Temperature_Whole_Blood, "," ,Tidal_Volume_Whole_Blood, "," ,Ventilation_Rate_Whole_Blood, "," ,Ventilator_Whole_Blood, "," ,Voided_Specimen_Body_Fluid, "," ,Voided_Specimen_Whole_Blood,"]")
WHERE Property_Str  is null ;

##########################################################################################################################################################################

ALTER   TABLE `mimic-four-377221.E6_BloodGas.bgB13_C1`
ADD    COLUMN  Proprty_int   STRING ;

UPDATE `mimic-four-377221.E6_BloodGas.bgB13_C1`
SET  Proprty_int  = concat("[",Item7, "," ,Item10, "," ,Item11, "," ,Item12, "," ,Item13, "," ,Item15, "," ,Item28, "," ,Item30,"]")
WHERE Proprty_int  is null ;

ALTER   TABLE `mimic-four-377221.E6_BloodGas.bgB13_C1`
ADD    COLUMN  Property_Str   STRING ;

UPDATE `mimic-four-377221.E6_BloodGas.bgB13_C1`
SET  Property_Str  = concat("[",Chloride_Whole_Blood, "," ,Free_Calcium_Whole_Blood, "," ,Glucose_Whole_Blood, "," ,Hematocrit_Calculated_Whole_Blood, "," ,Hemoglobin_Whole_Blood, "," ,Lactate_Whole_Blood, "," ,Potassium_Whole_Blood, "," ,Sodium_Whole_Blood,"]")
WHERE Property_Str  is null ;

##########################################################################################################################################################################

ALTER   TABLE `mimic-four-377221.E6_BloodGas.bgB13_C2`
ADD    COLUMN  Proprty_int   STRING ;

UPDATE `mimic-four-377221.E6_BloodGas.bgB13_C2`
SET  Proprty_int  = concat("[",Item3, "," ,Item5, "," ,Item22, "," ,Item25, "," ,Item27,"]")
WHERE Proprty_int  is null ;


ALTER   TABLE `mimic-four-377221.E6_BloodGas.bgB13_C2`
ADD    COLUMN  Property_Str   STRING ;

UPDATE `mimic-four-377221.E6_BloodGas.bgB13_C2`
SET  Property_Str  = concat("[",Base_Excess_Whole_Blood, "," ,Calculated_Total_CO2_Whole_Blood, "," ,pCO2_Whole_Blood, "," ,pH_Whole_Blood, "," ,pO2_Whole_Blood,"]")
WHERE Property_Str  is null ;

##########################################################################################################################################################################

ALTER   TABLE `mimic-four-377221.E6_BloodGas.bgB13_C3`
ADD    COLUMN  Proprty_int   STRING ;

UPDATE `mimic-four-377221.E6_BloodGas.bgB13_C3`
SET  Proprty_int  = concat("[",Item31,"]")
WHERE Proprty_int  is null ;

ALTER   TABLE `mimic-four-377221.E6_BloodGas.bgB13_C3`
ADD    COLUMN  Property_Str   STRING ;

UPDATE `mimic-four-377221.E6_BloodGas.bgB13_C3`
SET  Property_Str  = concat("[",Specimen_Type_Whole_Blood,"]")
WHERE Property_Str  is null ;



'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
