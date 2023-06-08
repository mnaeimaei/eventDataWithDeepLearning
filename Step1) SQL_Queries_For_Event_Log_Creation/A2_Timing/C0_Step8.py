import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            



###########################################################################

create Table  `mimic-four-377221.R_TimeD.D_SH_Date` as

select 
subject_id, 
hadm_id, 
mini, 
maxi, 
STRING_AGG(Title_mini , "/" ORDER BY Title_mini) as Title_mini, 
STRING_AGG(Title_maxi , "/" ORDER BY Title_maxi)  as Title_maxi
FROM  `mimic-four-377221.R_TimeC.C_SH_Date` 
GROUP BY subject_id,hadm_id,mini,maxi

;

###########################################################################

create Table  `mimic-four-377221.R_TimeD.D_SH_Time` as

select 
subject_id, 
hadm_id, 
mini, 
maxi, 
STRING_AGG(Title_mini , "/" ORDER BY Title_mini) as Title_mini,  
STRING_AGG(Title_maxi , "/" ORDER BY Title_maxi)  as Title_maxi
FROM  `mimic-four-377221.R_TimeC.C_SH_Time`
GROUP BY subject_id,hadm_id,mini,maxi
;


###########################################################################

create Table  `mimic-four-377221.R_TimeD.D_SHI_Date` as

select 
subject_id, 
hadm_id, 
stay_id,
mini, 
maxi, 
STRING_AGG(Title_mini , "/" ORDER BY Title_mini) as Title_mini, 
STRING_AGG(Title_maxi , "/" ORDER BY Title_maxi)  as Title_maxi
FROM  `mimic-four-377221.R_TimeC.C_SHI_Date`
GROUP BY subject_id,hadm_id,stay_id,mini,maxi
;



###########################################################################

create Table  `mimic-four-377221.R_TimeD.D_SHI_Time` as

select 
subject_id, 
hadm_id, 
stay_id,
mini, 
maxi, 
STRING_AGG(Title_mini , "/" ORDER BY Title_mini) as Title_mini, 
STRING_AGG(Title_maxi , "/" ORDER BY Title_maxi)  as Title_maxi
FROM  `mimic-four-377221.R_TimeC.C_SHI_Time` 
GROUP BY subject_id,hadm_id,stay_id,mini,maxi
;



###########################################################################

create Table  `mimic-four-377221.R_TimeD.D_SHT_Time` as

select 
subject_id, 
hadm_id, 
transfer_id,
mini, 
maxi, 
STRING_AGG(Title_mini , "/" ORDER BY Title_mini) as Title_mini, 
STRING_AGG(Title_maxi , "/" ORDER BY Title_maxi)  as Title_maxi
FROM `mimic-four-377221.R_TimeC.C_SHT_Time` 
GROUP BY subject_id,hadm_id,transfer_id,mini,maxi
;




###########################################################################

create Table  `mimic-four-377221.R_TimeD.D_ST_Time` as

select 
subject_id, 
transfer_id,
mini, 
maxi, 
STRING_AGG(Title_mini , "/" ORDER BY Title_mini) as Title_mini, 
STRING_AGG(Title_maxi , "/" ORDER BY Title_maxi)  as Title_maxi
FROM  `mimic-four-377221.R_TimeC.C_ST_Time` 
GROUP BY subject_id,transfer_id,mini,maxi
;



###########################################################################

create Table  `mimic-four-377221.R_TimeD.D_S_Time` as

select 
subject_id, 
mini, 
maxi, 
STRING_AGG(Title_mini , "/" ORDER BY Title_mini) as Title_mini, 
STRING_AGG(Title_maxi , "/" ORDER BY Title_maxi)  as Title_maxi
FROM `mimic-four-377221.R_TimeC.C_S_Time` 
GROUP BY subject_id,mini,maxi
;



###########################################################################

create Table  `mimic-four-377221.R_TimeD.D_S_Date` as

select 
subject_id, 
mini, 
maxi, 
STRING_AGG(Title_mini , "/" ORDER BY Title_mini) as Title_mini, 
STRING_AGG(Title_maxi , "/" ORDER BY Title_maxi)  as Title_maxi
FROM `mimic-four-377221.R_TimeC.C_S_Date` 
GROUP BY subject_id,mini,maxi
;



###########################################################################


'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
