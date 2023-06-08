import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            




        CREATE   TABLE `mimic-four-377221.P_NonEvents.kkk6`  AS
        SELECT   DISTINCT subject_id, hadm_id FROM `mimic-four-377221.P_NonEvents.K4` ;


        ALTER   TABLE `mimic-four-377221.P_NonEvents.kkk6`  
        ADD    COLUMN  Col1 STRING ;

        UPDATE `mimic-four-377221.P_NonEvents.kkk6`  
        SET  Col1  = "A"
        WHERE Col1 is null ;


        CREATE   TABLE `mimic-four-377221.P_NonEvents.kkk67`  AS
        SELECT   
        Row_number() over (partition by Col1) as rowNum,  subject_id, hadm_id

        FROM `mimic-four-377221.P_NonEvents.kkk6`  ;


        CREATE   TABLE `mimic-four-377221.P_NonEvents.K5`  AS
        SELECT   
        a.rowNum,
        a.subject_id, a.hadm_id,
        b.seq_num, b.icd_code, b.icd_version, b.long_title
        FROM `mimic-four-377221.P_NonEvents.kkk67`     a
        LEFT JOIN `mimic-four-377221.P_NonEvents.K4`     b
        ON  a.subject_id = b.subject_id AND a.hadm_id = b.hadm_id;


        drop table `mimic-four-377221.P_NonEvents.kkk6`  ;
        drop table `mimic-four-377221.P_NonEvents.kkk67`  ;








'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
