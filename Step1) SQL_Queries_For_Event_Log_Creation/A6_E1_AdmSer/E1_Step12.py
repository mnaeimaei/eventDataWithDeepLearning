import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            


        CREATE   TABLE `mimic-four-377221.E1_AdmSer.kkk6`  AS
        SELECT   DISTINCT subject_id, hadm_id, Activity, Activity_Synonym, Timestamp FROM `mimic-four-377221.E1_AdmSer.TabF` ;


        ALTER   TABLE `mimic-four-377221.E1_AdmSer.kkk6`  
        ADD    COLUMN  Col1 STRING ;

        UPDATE `mimic-four-377221.E1_AdmSer.kkk6`  
        SET  Col1  = "A"
        WHERE Col1 is null ;


        CREATE   TABLE `mimic-four-377221.E1_AdmSer.kkk67`  AS
        SELECT   
        Row_number() over (partition by Col1) as rowNum,  subject_id, hadm_id, Activity, Activity_Synonym, Timestamp

        FROM `mimic-four-377221.E1_AdmSer.kkk6`  ;


        CREATE   TABLE `mimic-four-377221.E1_AdmSer.TabF0`  AS
        SELECT   
        a.rowNum,
        a.subject_id, a.hadm_id, a.Activity, a.Activity_Synonym, a.Timestamp,
        b.admission_location, b.admission_type, b.discharge_location, b.prev_service, b.curr_service, b.a1, b.a2, b.a3, b.a4, b.a5, b.Property_Str, b.Proprty_int, b.Type
        FROM `mimic-four-377221.E1_AdmSer.kkk67`     a
        LEFT JOIN `mimic-four-377221.E1_AdmSer.TabF`     b
        ON  a.subject_id = b.subject_id AND a.hadm_id = b.hadm_id AND a.Activity = b.Activity AND a.Activity_Synonym = b.Activity_Synonym AND a.Timestamp = b.Timestamp;
        

        drop table `mimic-four-377221.E1_AdmSer.kkk6`  ;
        drop table `mimic-four-377221.E1_AdmSer.kkk67`  ;
        drop table `mimic-four-377221.E1_AdmSer.TabF`  ;
        
        ALTER   TABLE `mimic-four-377221.E1_AdmSer.TabF0`  
        ADD    COLUMN  Property_col STRING ;

        UPDATE `mimic-four-377221.E1_AdmSer.TabF0`  
        SET  Property_col  = "[admission_location, admission_type, discharge_location, prev_service, curr_service]"
        WHERE Property_col is null ;
        




    




'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
