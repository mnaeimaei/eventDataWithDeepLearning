import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

#################################################################################

create table `mimic-four-377221.E6_BloodGas.bgA3` as

SELECT distinct 
subject_id, hadm_id, ACT1 as ACT, charttime as Timstamp, NEW_LABEL as Label,
 value, valuenum, valueuom, ref_range_lower, ref_range_upper, flag
 FROM `mimic-four-377221.E6_BloodGas.bgA2` 

union all

 SELECT distinct 
subject_id, hadm_id, ACT2 as ACT, storetime as Timstamp, NEW_LABEL as Label,
 value, valuenum, valueuom, ref_range_lower, ref_range_upper, flag
 FROM `mimic-four-377221.E6_BloodGas.bgA2` ;


#################################################################################

        alter table `mimic-four-377221.E6_BloodGas.bgA3`
        ADD COLUMN Value_N STRING  ;
        

        update `mimic-four-377221.E6_BloodGas.bgA3`
        SET hadm_id=0
        where hadm_id is null;

#################################################################################

        update `mimic-four-377221.E6_BloodGas.bgA3`
        SET value=NULL
        where value="___";
        
        update `mimic-four-377221.E6_BloodGas.bgA3`
        SET value=NULL
        where value="-";

        update `mimic-four-377221.E6_BloodGas.bgA3`
        SET value=NULL
        where value=".";
        
        update `mimic-four-377221.E6_BloodGas.bgA3`
        SET value=NULL
        where value=" ";

#################################################################################

        update `mimic-four-377221.E6_BloodGas.bgA3`
        SET Value_N=CONCAT(valuenum," ",valueuom)
        where value IS NOT NULL 
        AND valuenum IS  NOT NULL
        AND valueuom IS  NOT NULL
        ;
        
        
        update `mimic-four-377221.E6_BloodGas.bgA3`
        SET Value_N=CONCAT(value)
        where value IS NOT NULL 
        AND valuenum IS  NULL
        AND valueuom IS  NULL
        ;
        
        
        update `mimic-four-377221.E6_BloodGas.bgA3`
        SET Value_N=CONCAT(value," ",valueuom)
        where value IS NOT NULL 
        AND valuenum IS  NULL
        AND valueuom IS  NOT NULL
        ;
        
        
        update `mimic-four-377221.E6_BloodGas.bgA3`
        SET Value_N=CONCAT(valuenum)
        where value IS NULL 
        AND valuenum IS  NOT NULL
        AND valueuom IS  NULL
        ;
        
        
       
        update `mimic-four-377221.E6_BloodGas.bgA3`
        SET Value_N=CONCAT(valuenum," ",valueuom)
        where value IS NULL 
        AND valuenum IS  NOT NULL
        AND valueuom IS  NOT NULL
        ;
        
        
        update `mimic-four-377221.E6_BloodGas.bgA3`
        SET Value_N=CONCAT(valuenum)
        where value IS NOT NULL 
        AND valuenum IS  NOT NULL
        AND valueuom IS  NULL
        ;


                
        update `mimic-four-377221.E6_BloodGas.bgA3`
        SET Value_N=CONCAT(valueuom)
        where value IS  NULL 
        AND valuenum IS   NULL
        AND valueuom IS NOT NULL
        ;


        update `mimic-four-377221.E6_BloodGas.bgA3`
        SET Value_N="NULL"
        where value IS  NULL 
        AND valuenum IS   NULL
        AND valueuom IS NULL
        ;


        
        




'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
