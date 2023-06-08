import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

        CREATE   TABLE `mimic-four-377221.E4_MicroB.kkk6`  AS
        SELECT   DISTINCT subject_id, hadm_id, Timestamp, test_name, org_name FROM `mimic-four-377221.E4_MicroB.Micro_C1` ;


        ALTER   TABLE `mimic-four-377221.E4_MicroB.kkk6`  
        ADD    COLUMN  Col1 STRING ;

        UPDATE `mimic-four-377221.E4_MicroB.kkk6`  
        SET  Col1  = "A"
        WHERE Col1 is null ;


        CREATE   TABLE `mimic-four-377221.E4_MicroB.kkk67`  AS
        SELECT   
        Row_number() over (partition by Col1) as rowNum,  subject_id, hadm_id, Timestamp, test_name, org_name

        FROM `mimic-four-377221.E4_MicroB.kkk6`  ;


        CREATE   TABLE `mimic-four-377221.E4_MicroB.Micro_C3`  AS
        SELECT   
        a.rowNum,
        a.subject_id, a.hadm_id, a.Timestamp, a.test_name, a.org_name,
        b.ab_name, b.interpretation, b.test_name_Syn, b.org_name_Syn, b.ab_name_Syn, b.interpretation_Syn
        FROM `mimic-four-377221.E4_MicroB.kkk67`     a
        LEFT JOIN `mimic-four-377221.E4_MicroB.Micro_C2`     b
        ON  a.subject_id = b.subject_id AND a.hadm_id = b.hadm_id AND a.Timestamp = b.Timestamp AND a.test_name = b.test_name AND a.org_name = b.org_name;


        drop table `mimic-four-377221.E4_MicroB.kkk6`  ;
        drop table `mimic-four-377221.E4_MicroB.kkk67`  ;


'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
