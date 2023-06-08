import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            


create table `mimic-four-377221.E4_MicroB.Micro_C1` as

select distinct * from
(SELECT
subject_id, hadm_id, storetime as Timestamp, test_name, org_name, ab_name,interpretation
FROM `mimic-four-377221.E4_Micro.Micro_A` 
where storetime is not null 

union all

select
subject_id, hadm_id, storedate as Timestamp, test_name, org_name, ab_name, interpretation
FROM `mimic-four-377221.E4_Micro.Micro_A` 
where storetime is  null );

#############################################################################

        UPDATE `mimic-four-377221.E4_MicroB.Micro_C1`  
        SET  org_name  = "no organism grew"
        WHERE org_name is null ;

#############################################################################
        UPDATE `mimic-four-377221.E4_MicroB.Micro_C1`  
        SET  ab_name  = "no need antibiotic"
        WHERE org_name  = "no organism grew";
        
        UPDATE `mimic-four-377221.E4_MicroB.Micro_C1`  
        SET  ab_name  = "no antibiotic"
        WHERE org_name <> "no organism grew" and ab_name is null;
        


#############################################################################
        UPDATE `mimic-four-377221.E4_MicroB.Micro_C1`  
        SET  interpretation  = "no need interpretation"
        WHERE org_name  = "no organism grew";
        
        UPDATE `mimic-four-377221.E4_MicroB.Micro_C1`  
        SET  interpretation  = "no interpretation"
        WHERE org_name <> "no organism grew"  and interpretation is null;



#############################################################################

'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
