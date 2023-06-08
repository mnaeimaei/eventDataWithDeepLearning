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

create Table  `mimic-four-377221.R_TimeE.E_SHI` as

(SELECT  distinct

a.subject_id,
a.hadm_id,
a.stay_id,
a.mini as mini_Time,
a.maxi as maxi_Time,
a.Title_mini as Title_mini_Time,
a.Title_maxi as Title_maxi_Time,

b.mini as mini_Date,
b.maxi as maxi_Date,
b.Title_mini as Title_mini_Date,
b.Title_maxi as Title_maxi_Date

FROM `mimic-four-377221.R_TimeD.D_SHI_Time` a
left join `mimic-four-377221.R_TimeD.D_SHI_Date` b
on
a.subject_id=b.subject_id
and
a.hadm_id=b.hadm_id
and
a.stay_id=b.stay_id)
;


###########################################################################		

create Table  `mimic-four-377221.R_TimeE.E_SHT` as

SELECT distinct * FROM `mimic-four-377221.R_TimeD.D_SHT_Time` 
;


###########################################################################		

create Table  `mimic-four-377221.R_TimeE.E_SH` as

(SELECT distinct 

a.subject_id,
a.hadm_id,
a.mini as mini_Time,
a.maxi as maxi_Time,
a.Title_mini as Title_mini_Time,
a.Title_maxi as Title_maxi_Time,

b.mini as mini_Date,
b.maxi as maxi_Date,
b.Title_mini as Title_mini_Date,
b.Title_maxi as Title_maxi_Date

FROM `mimic-four-377221.R_TimeD.D_SH_Time` a
left join `mimic-four-377221.R_TimeD.D_SH_Date` b
on
a.subject_id=b.subject_id
and
a.hadm_id=b.hadm_id
)
;

###########################################################################		
create Table  `mimic-four-377221.R_TimeE.E_ST` as

SELECT distinct * FROM `mimic-four-377221.R_TimeD.D_ST_Time` 
;
###########################################################################		

create Table  `mimic-four-377221.R_TimeE.E_S` as

(SELECT distinct

a.subject_id,
a.mini as mini_Time,
a.maxi as maxi_Time,
a.Title_mini as Title_mini_Time,
a.Title_maxi as Title_maxi_Time,

b.mini as mini_Date,
b.maxi as maxi_Date,
b.Title_mini as Title_mini_Date,
b.Title_maxi as Title_maxi_Date

FROM `mimic-four-377221.R_TimeD.D_S_Time` a
left join `mimic-four-377221.R_TimeD.D_S_Date` b
on
a.subject_id=b.subject_id
)
;
###########################################################################		

'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
