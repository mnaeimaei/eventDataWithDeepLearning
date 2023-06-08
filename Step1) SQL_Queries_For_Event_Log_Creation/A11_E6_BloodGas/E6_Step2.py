import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            
##########################################################################


create table `mimic-four-377221.E6_BloodGas.bgA2` as
SELECT * FROM  `mimic-four-377221.E6_BloodGas.bgA1` ;

##########################################################################

        alter table `mimic-four-377221.E6_BloodGas.bgA2`
        ADD COLUMN NEW_LABEL STRING  ;
##########################################################################

update `mimic-four-377221.E6_BloodGas.bgA2`    	SET NEW_LABEL="Specimen Type, Whole Blood"  	where label="Specimen Type"	  and fluid="Blood";
update `mimic-four-377221.E6_BloodGas.bgA2`    	SET NEW_LABEL="Voided Specimen, Whole Blood"  	where label="Voided Specimen"	  and fluid="Blood";
update `mimic-four-377221.E6_BloodGas.bgA2`    	SET NEW_LABEL="Assist/Control, Whole Blood"  	where label="Assist/Control"	  and fluid="Blood";
update `mimic-four-377221.E6_BloodGas.bgA2`    	SET NEW_LABEL="Estimated GFR (MDRD equation), Whole Blood"  	where label="Estimated GFR (MDRD equation)"	  and fluid="Blood";
update `mimic-four-377221.E6_BloodGas.bgA2`    	SET NEW_LABEL="P50 of Hemoglobin, Whole Blood"  	where label="P50 of Hemoglobin"	  and fluid="Blood";
update `mimic-four-377221.E6_BloodGas.bgA2`    	SET NEW_LABEL="Calculated Bicarbonate, Whole Blood"  	where label="Calculated Bicarbonate, Whole Blood"	  and fluid="Blood";
update `mimic-four-377221.E6_BloodGas.bgA2`    	SET NEW_LABEL="Calculated Total CO2, Whole Blood"  	where label="Calculated Total CO2"	  and fluid="Blood";
update `mimic-four-377221.E6_BloodGas.bgA2`    	SET NEW_LABEL="Carboxyhemoglobin, Whole Blood"  	where label="Carboxyhemoglobin"	  and fluid="Blood";
update `mimic-four-377221.E6_BloodGas.bgA2`    	SET NEW_LABEL="Chloride, Whole Blood"  	where label="Chloride, Whole Blood"	  and fluid="Blood";
update `mimic-four-377221.E6_BloodGas.bgA2`    	SET NEW_LABEL="Creatinine, Whole Blood"  	where label="Creatinine, Whole Blood"	  and fluid="Blood";
update `mimic-four-377221.E6_BloodGas.bgA2`    	SET NEW_LABEL="Free Calcium, Whole Blood"  	where label="Free Calcium"	  and fluid="Blood";
update `mimic-four-377221.E6_BloodGas.bgA2`    	SET NEW_LABEL="Glucose, Whole Blood"  	where label="Glucose"	  and fluid="Blood";
update `mimic-four-377221.E6_BloodGas.bgA2`    	SET NEW_LABEL="Hemoglobin, Whole Blood"  	where label="Hemoglobin"	  and fluid="Blood";
update `mimic-four-377221.E6_BloodGas.bgA2`    	SET NEW_LABEL="Lactate, Whole Blood"  	where label="Lactate"	  and fluid="Blood";
update `mimic-four-377221.E6_BloodGas.bgA2`    	SET NEW_LABEL="Methemoglobin, Whole Blood"  	where label="Methemoglobin"	  and fluid="Blood";
update `mimic-four-377221.E6_BloodGas.bgA2`    	SET NEW_LABEL="pCO2, Whole Blood"  	where label="pCO2"	  and fluid="Blood";
update `mimic-four-377221.E6_BloodGas.bgA2`    	SET NEW_LABEL="pH, Whole Blood"  	where label="pH"	  and fluid="Blood";
update `mimic-four-377221.E6_BloodGas.bgA2`    	SET NEW_LABEL="pO2, Whole Blood"  	where label="pO2"	  and fluid="Blood";
update `mimic-four-377221.E6_BloodGas.bgA2`    	SET NEW_LABEL="Potassium, Whole Blood"  	where label="Potassium, Whole Blood"	  and fluid="Blood";
update `mimic-four-377221.E6_BloodGas.bgA2`    	SET NEW_LABEL="Sodium, Whole Blood"  	where label="Sodium, Whole Blood"	  and fluid="Blood";
update `mimic-four-377221.E6_BloodGas.bgA2`    	SET NEW_LABEL="Alveolar-arterial Gradient, Whole Blood"  	where label="Alveolar-arterial Gradient"	  and fluid="Blood";
update `mimic-four-377221.E6_BloodGas.bgA2`    	SET NEW_LABEL="Base Excess, Whole Blood"  	where label="Base Excess"	  and fluid="Blood";
update `mimic-four-377221.E6_BloodGas.bgA2`    	SET NEW_LABEL="Hematocrit, Calculated, Whole Blood"  	where label="Hematocrit, Calculated"	  and fluid="Blood";
update `mimic-four-377221.E6_BloodGas.bgA2`    	SET NEW_LABEL="Intubated, Whole Blood"  	where label="Intubated"	  and fluid="Blood";
update `mimic-four-377221.E6_BloodGas.bgA2`    	SET NEW_LABEL="O2 Flow, Whole Blood"  	where label="O2 Flow"	  and fluid="Blood";
update `mimic-four-377221.E6_BloodGas.bgA2`    	SET NEW_LABEL="Oxygen, Whole Blood"  	where label="Oxygen"	  and fluid="Blood";
update `mimic-four-377221.E6_BloodGas.bgA2`    	SET NEW_LABEL="Oxygen Saturation, Whole Blood"  	where label="Oxygen Saturation"	  and fluid="Blood";
update `mimic-four-377221.E6_BloodGas.bgA2`    	SET NEW_LABEL="PEEP, Whole Blood"  	where label="PEEP"	  and fluid="Blood";
update `mimic-four-377221.E6_BloodGas.bgA2`    	SET NEW_LABEL="Required O2, Whole Blood"  	where label="Required O2"	  and fluid="Blood";
update `mimic-four-377221.E6_BloodGas.bgA2`    	SET NEW_LABEL="Temperature, Whole Blood"  	where label="Temperature"	  and fluid="Blood";
update `mimic-four-377221.E6_BloodGas.bgA2`    	SET NEW_LABEL="Tidal Volume, Whole Blood"  	where label="Tidal Volume"	  and fluid="Blood";
update `mimic-four-377221.E6_BloodGas.bgA2`    	SET NEW_LABEL="Ventilation Rate, Whole Blood"  	where label="Ventilation Rate"	  and fluid="Blood";
update `mimic-four-377221.E6_BloodGas.bgA2`    	SET NEW_LABEL="Ventilator, Whole Blood"  	where label="Ventilator"	  and fluid="Blood";
update `mimic-four-377221.E6_BloodGas.bgA2`    	SET NEW_LABEL="Voided Specimen, Body Fluid"  	where label="Voided Specimen"	  and fluid="Other Body Fluid";
update `mimic-four-377221.E6_BloodGas.bgA2`    	SET NEW_LABEL="pCO2, Body Fluid"  	where label="pCO2, Body Fluid"	  and fluid="Other Body Fluid";
update `mimic-four-377221.E6_BloodGas.bgA2`    	SET NEW_LABEL="pH, Body Fluid"  	where label="pH"	  and fluid="Other Body Fluid";
update `mimic-four-377221.E6_BloodGas.bgA2`    	SET NEW_LABEL="pO2, Body Fluid, Body Fluid"  	where label="pO2, Body Fluid"	  and fluid="Other Body Fluid";


#####################################################################

        alter table `mimic-four-377221.E6_BloodGas.bgA2`
        ADD COLUMN ACT1 STRING  ;
        
        alter table `mimic-four-377221.E6_BloodGas.bgA2`
        ADD COLUMN ACT2 STRING  ;

#####################################################################
update `mimic-four-377221.E6_BloodGas.bgA2`
    	SET ACT1="charttime"  
    		where ACT1 is null;
    		
    		
update `mimic-four-377221.E6_BloodGas.bgA2`
    	SET ACT2="storetime"  
    		where ACT2 is null;


#####################################################################
'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
