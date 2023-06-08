import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            



update `mimic-four-377221.E6_BloodGas.bgA4`    	SET Value=flag	 where flag is not null	  and Label="Calculated Bicarbonate, Whole Blood";
update `mimic-four-377221.E6_BloodGas.bgA4`    	SET Value=flag	 where flag is not null	  and Label="Calculated Total CO2, Whole Blood";
update `mimic-four-377221.E6_BloodGas.bgA4`    	SET Value=flag	 where flag is not null	  and Label="Carboxyhemoglobin, Whole Blood";
update `mimic-four-377221.E6_BloodGas.bgA4`    	SET Value=flag	 where flag is not null	  and Label="Chloride, Whole Blood";
update `mimic-four-377221.E6_BloodGas.bgA4`    	SET Value=flag	 where flag is not null	  and Label="Creatinine, Whole Blood";
update `mimic-four-377221.E6_BloodGas.bgA4`    	SET Value=flag	 where flag is not null	  and Label="Free Calcium, Whole Blood";
update `mimic-four-377221.E6_BloodGas.bgA4`    	SET Value=flag	 where flag is not null	  and Label="Glucose, Whole Blood";
update `mimic-four-377221.E6_BloodGas.bgA4`    	SET Value=flag	 where flag is not null	  and Label="Hemoglobin, Whole Blood";
update `mimic-four-377221.E6_BloodGas.bgA4`    	SET Value=flag	 where flag is not null	  and Label="Lactate, Whole Blood";
update `mimic-four-377221.E6_BloodGas.bgA4`    	SET Value=flag	 where flag is not null	  and Label="Methemoglobin, Whole Blood";
update `mimic-four-377221.E6_BloodGas.bgA4`    	SET Value=flag	 where flag is not null	  and Label="pCO2, Whole Blood";
update `mimic-four-377221.E6_BloodGas.bgA4`    	SET Value=flag	 where flag is not null	  and Label="pH, Whole Blood";
update `mimic-four-377221.E6_BloodGas.bgA4`    	SET Value=flag	 where flag is not null	  and Label="pO2, Whole Blood";
update `mimic-four-377221.E6_BloodGas.bgA4`    	SET Value=flag	 where flag is not null	  and Label="Potassium, Whole Blood";
update `mimic-four-377221.E6_BloodGas.bgA4`    	SET Value=flag	 where flag is not null	  and Label="Sodium, Whole Blood";



'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
