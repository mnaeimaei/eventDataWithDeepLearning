import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

CREATE TABLE  `mimic-four-377221.E6_BloodGas.bgB13_C0`   AS
SELECT
a.rowNum, a.Item1, a.Item2, a.Item4, a.Item6, a.Item8, a.Item9, a.Item14, a.Item16, a.Item17, a.Item18, a.Item19, a.Item20, a.Item21, a.Item23, a.Item24, a.Item26, a.Item29, a.Item32, a.Item33, a.Item34, a.Item35, a.Item36, a.Item37,
b.Alveolar_arterial_Gradient_Whole_Blood, b.Assist_Control_Whole_Blood, b.Calculated_Bicarbonate_Whole_Blood, b.Carboxyhemoglobin_Whole_Blood, b.Creatinine_Whole_Blood, b.Estimated_GFR_Whole_Blood, b.Intubated_Whole_Blood, b.Methemoglobin_Whole_Blood, b.O2_Flow_Whole_Blood, b.Oxygen_Saturation_Whole_Blood, b.Oxygen_Whole_Blood, b.P50_of_Hemoglobin_Whole_Blood, b.pCO2_Body_Fluid, b.PEEP_Whole_Blood, b.pH_Body_Fluid, b.pO2_Body_Fluid_Body_Fluid, b.Required_O2_Whole_Blood, b.Temperature_Whole_Blood, b.Tidal_Volume_Whole_Blood, b.Ventilation_Rate_Whole_Blood, b.Ventilator_Whole_Blood, b.Voided_Specimen_Body_Fluid, b.Voided_Specimen_Whole_Blood,
From `mimic-four-377221.E6_BloodGas.bgB11_C0`   as a
LEFT JOIN `mimic-four-377221.E6_BloodGas.bgB12`   as b
ON
a.rowNum=b.rowNum
;



CREATE TABLE  `mimic-four-377221.E6_BloodGas.bgB13_C1`   AS
SELECT
a.rowNum, a.Item7, a.Item10, a.Item11, a.Item12, a.Item13, a.Item15, a.Item28, a.Item30,
b.Chloride_Whole_Blood, b.Free_Calcium_Whole_Blood, b.Glucose_Whole_Blood, b.Hematocrit_Calculated_Whole_Blood, b.Hemoglobin_Whole_Blood, b.Lactate_Whole_Blood, b.Potassium_Whole_Blood, b.Sodium_Whole_Blood,
From `mimic-four-377221.E6_BloodGas.bgB11_C1`   as a
LEFT JOIN `mimic-four-377221.E6_BloodGas.bgB12`   as b
ON
a.rowNum=b.rowNum
;



CREATE TABLE  `mimic-four-377221.E6_BloodGas.bgB13_C2`   AS
SELECT
a.rowNum, a.Item3, a.Item5, a.Item22, a.Item25, a.Item27,
b.Base_Excess_Whole_Blood, b.Calculated_Total_CO2_Whole_Blood, b.pCO2_Whole_Blood, b.pH_Whole_Blood, b.pO2_Whole_Blood,
From `mimic-four-377221.E6_BloodGas.bgB11_C2`   as a
LEFT JOIN `mimic-four-377221.E6_BloodGas.bgB12`   as b
ON
a.rowNum=b.rowNum
;


CREATE TABLE  `mimic-four-377221.E6_BloodGas.bgB13_C3`   AS
SELECT
a.rowNum, a.Item31,
b.Specimen_Type_Whole_Blood,
From `mimic-four-377221.E6_BloodGas.bgB11_C3`   as a
LEFT JOIN `mimic-four-377221.E6_BloodGas.bgB12`   as b
ON
a.rowNum=b.rowNum
;


'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
