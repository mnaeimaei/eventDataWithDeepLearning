import os
from google.cloud import bigquery

symPath = '../gcKey/SNOMED_CT_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

###################################
################################### Go to SQL \ Query 10_SCT
###################################
# Perform a query.
query1 = f'''            

       CREATE TABLE  `snomed-ct-377221.SCT_3.PaperB`   AS 
        SELECT DISTINCT * FROM   (
        SELECT DISTINCT * FROM (  
        SELECT DISTINCT s0 , s1   FROM `snomed-ct-377221.SCT_3.PaperA` 
        UNION ALL 
        SELECT DISTINCT s1 , s2   FROM `snomed-ct-377221.SCT_3.PaperA` 
        UNION ALL 
        SELECT DISTINCT s2 , s3   FROM `snomed-ct-377221.SCT_3.PaperA` 
        UNION ALL 
        SELECT DISTINCT s3 , s4   FROM `snomed-ct-377221.SCT_3.PaperA` 
        UNION ALL 
        SELECT DISTINCT s4 , s5   FROM `snomed-ct-377221.SCT_3.PaperA` 
        UNION ALL 
        SELECT DISTINCT s5 , s6   FROM `snomed-ct-377221.SCT_3.PaperA` 
        UNION ALL 
        SELECT DISTINCT s6 , s7   FROM `snomed-ct-377221.SCT_3.PaperA` 
        UNION ALL 
        SELECT DISTINCT s7 , s8   FROM `snomed-ct-377221.SCT_3.PaperA` 
        UNION ALL 
        SELECT DISTINCT s8 , s9   FROM `snomed-ct-377221.SCT_3.PaperA` 
        UNION ALL 
        SELECT DISTINCT s9 , s10   FROM `snomed-ct-377221.SCT_3.PaperA` 
        UNION ALL 
        SELECT DISTINCT s10 , s11   FROM `snomed-ct-377221.SCT_3.PaperA` 
        UNION ALL 
        SELECT DISTINCT s11 , s12   FROM `snomed-ct-377221.SCT_3.PaperA` 
        UNION ALL 
        SELECT DISTINCT s12 , s13   FROM `snomed-ct-377221.SCT_3.PaperA` 
        UNION ALL 
        SELECT DISTINCT s13 , s14   FROM `snomed-ct-377221.SCT_3.PaperA` 
        UNION ALL 
        SELECT DISTINCT s14 , s15   FROM `snomed-ct-377221.SCT_3.PaperA` 
        UNION ALL 
        SELECT DISTINCT s15 , s16   FROM `snomed-ct-377221.SCT_3.PaperA` 
        UNION ALL 
        SELECT DISTINCT s16 , s17   FROM `snomed-ct-377221.SCT_3.PaperA` 
        UNION ALL 
        SELECT DISTINCT s17 , s18   FROM `snomed-ct-377221.SCT_3.PaperA` 
        UNION ALL 
        SELECT DISTINCT s18 , s19   FROM `snomed-ct-377221.SCT_3.PaperA` 
        UNION ALL 
        SELECT DISTINCT s19 , s20   FROM `snomed-ct-377221.SCT_3.PaperA` 
        UNION ALL 
        SELECT DISTINCT s20 , s21   FROM `snomed-ct-377221.SCT_3.PaperA` 
        UNION ALL 
        SELECT DISTINCT s21 , s22   FROM `snomed-ct-377221.SCT_3.PaperA` 
        UNION ALL 
        SELECT DISTINCT s22 , s23   FROM `snomed-ct-377221.SCT_3.PaperA` 
        UNION ALL 
        SELECT DISTINCT s23 , s24   FROM `snomed-ct-377221.SCT_3.PaperA` 
        UNION ALL 
        SELECT DISTINCT s24 , s25   FROM `snomed-ct-377221.SCT_3.PaperA` 
        UNION ALL 
        SELECT DISTINCT s25 , s26   FROM `snomed-ct-377221.SCT_3.PaperA` 
        UNION ALL 
        SELECT DISTINCT s26 , s27   FROM `snomed-ct-377221.SCT_3.PaperA` 
        UNION ALL 
        SELECT DISTINCT s27 , s28   FROM `snomed-ct-377221.SCT_3.PaperA` 
        UNION ALL 
        SELECT DISTINCT s28 , s29   FROM `snomed-ct-377221.SCT_3.PaperA` 
        UNION ALL 
        SELECT DISTINCT s29 , s30   FROM `snomed-ct-377221.SCT_3.PaperA` 
        UNION ALL 
        SELECT DISTINCT s30 , s31   FROM `snomed-ct-377221.SCT_3.PaperA` 
       )
       WHERE  s0 is not null AND s1 is not null );
################################################################################
        CREATE TABLE  `snomed-ct-377221.SCT_3.PaperC`   AS 
        SELECT DISTINCT * FROM (  
        SELECT DISTINCT s0   FROM `snomed-ct-377221.SCT_3.PaperB` 
        UNION ALL 
        SELECT DISTINCT s1   FROM `snomed-ct-377221.SCT_3.PaperB` 
       );



'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
