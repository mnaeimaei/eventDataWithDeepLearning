import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

        CREATE   TABLE `mimic-four-377221.E4_Micro.kkk6`  AS
        SELECT   DISTINCT subject_id, hadm_id, Timestamp FROM `mimic-four-377221.E4_Micro.Micro_B1` ;


        ALTER   TABLE `mimic-four-377221.E4_Micro.kkk6`  
        ADD    COLUMN  Col1 STRING ;

        UPDATE `mimic-four-377221.E4_Micro.kkk6`  
        SET  Col1  = "A"
        WHERE Col1 is null ;


        CREATE   TABLE `mimic-four-377221.E4_Micro.kkk67`  AS
        SELECT   
        Row_number() over (partition by Col1) as rowNum,  subject_id, hadm_id, Timestamp

        FROM `mimic-four-377221.E4_Micro.kkk6`  ;


        CREATE   TABLE `mimic-four-377221.E4_Micro.Micro_B2`  AS
        SELECT   
        a.rowNum,
        a.subject_id, a.hadm_id, a.Timestamp,
        b.test_name, b.spec_type_desc, b.test_name_Syn, b.spec_type_desc_Syn
        FROM `mimic-four-377221.E4_Micro.kkk67`     a
        LEFT JOIN `mimic-four-377221.E4_Micro.Micro_B1`     b
        ON  a.subject_id = b.subject_id AND a.hadm_id = b.hadm_id AND a.Timestamp = b.Timestamp;
        

        drop table `mimic-four-377221.E4_Micro.kkk6`  ;
        drop table `mimic-four-377221.E4_Micro.kkk67`  ;



'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
