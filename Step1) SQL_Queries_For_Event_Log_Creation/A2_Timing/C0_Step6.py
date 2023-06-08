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

create Table  `mimic-four-377221.R_TimeC.C_SH_Date` as


(select 
c.subject_id,
c.hadm_id,
c.mini,
c.maxi,
c.Title_mini,
d.Title as Title_maxi
from

(select 
a.subject_id,
a.hadm_id,
a.mini,
a.maxi,
b.Title as Title_mini
from 
(SELECT 
subject_id, hadm_id, MIN(Timestamp) as mini, MAX(Timestamp) as maxi
FROM `mimic-four-377221.R_TimeB.SH_Date` 
GROUP BY   subject_id, hadm_id      ) a
left join  `mimic-four-377221.R_TimeB.SH_Date` b
on a.subject_id=b.subject_id and
a.hadm_id=b.hadm_id and
a.mini=b.Timestamp) c

left join  `mimic-four-377221.R_TimeB.SH_Date` d
on c.subject_id=d.subject_id and
c.hadm_id=d.hadm_id and
c.maxi=d.Timestamp)

;

###########################################################################		

create Table  `mimic-four-377221.R_TimeC.C_SH_Time` as



(select 
c.subject_id,
c.hadm_id,
c.mini,
c.maxi,
c.Title_mini,
d.Title as Title_maxi
from

(select 
a.subject_id,
a.hadm_id,
a.mini,
a.maxi,
b.Title as Title_mini
from 
(SELECT 
subject_id, hadm_id, MIN(Timestamp) as mini, MAX(Timestamp) as maxi
FROM `mimic-four-377221.R_TimeB.SH_Time` 
GROUP BY   subject_id, hadm_id      ) a
left join  `mimic-four-377221.R_TimeB.SH_Time` b
on a.subject_id=b.subject_id and
a.hadm_id=b.hadm_id and
a.mini=b.Timestamp) c

left join  `mimic-four-377221.R_TimeB.SH_Time` d
on c.subject_id=d.subject_id and
c.hadm_id=d.hadm_id and
c.maxi=d.Timestamp)
;

###########################################################################		

create Table  `mimic-four-377221.R_TimeC.C_SHI_Date` as



(select 
c.subject_id,
c.hadm_id,
c.stay_id,
c.mini,
c.maxi,
c.Title_mini,
d.Title as Title_maxi
from

(select 
a.subject_id,
a.hadm_id,
a.stay_id,
a.mini,
a.maxi,
b.Title as Title_mini
from 
(SELECT 
subject_id, hadm_id, stay_id, MIN(Timestamp) as mini, MAX(Timestamp) as maxi
FROM `mimic-four-377221.R_TimeB.SHI_Date` 
GROUP BY   subject_id, hadm_id  ,stay_id    ) a
left join  `mimic-four-377221.R_TimeB.SHI_Date` b
on a.subject_id=b.subject_id and
a.hadm_id=b.hadm_id and
a.stay_id=b.stay_id and
a.mini=b.Timestamp) c

left join  `mimic-four-377221.R_TimeB.SHI_Date` d
on c.subject_id=d.subject_id and
c.hadm_id=d.hadm_id and
c.stay_id=d.stay_id and
c.maxi=d.Timestamp)
;

###########################################################################		

create Table  `mimic-four-377221.R_TimeC.C_SHI_Time` as



(select 
c.subject_id,
c.hadm_id,
c.stay_id,
c.mini,
c.maxi,
c.Title_mini,
d.Title as Title_maxi
from

(select 
a.subject_id,
a.hadm_id,
a.stay_id,
a.mini,
a.maxi,
b.Title as Title_mini
from 
(SELECT 
subject_id, hadm_id, stay_id, MIN(Timestamp) as mini, MAX(Timestamp) as maxi
FROM `mimic-four-377221.R_TimeB.SHI_Time` 
GROUP BY   subject_id, hadm_id  ,stay_id    ) a
left join  `mimic-four-377221.R_TimeB.SHI_Time` b
on a.subject_id=b.subject_id and
a.hadm_id=b.hadm_id and
a.stay_id=b.stay_id and
a.mini=b.Timestamp) c

left join  `mimic-four-377221.R_TimeB.SHI_Time` d
on c.subject_id=d.subject_id and
c.hadm_id=d.hadm_id and
c.stay_id=d.stay_id and
c.maxi=d.Timestamp)
;

###########################################################################		

create Table  `mimic-four-377221.R_TimeC.C_SHT_Time` as



(select 
c.subject_id,
c.hadm_id,
c.transfer_id,
c.mini,
c.maxi,
c.Title_mini,
d.Title as Title_maxi
from

(select 
a.subject_id,
a.hadm_id,
a.transfer_id,
a.mini,
a.maxi,
b.Title as Title_mini
from 
(SELECT 
subject_id, hadm_id, transfer_id, MIN(Timestamp) as mini, MAX(Timestamp) as maxi
FROM `mimic-four-377221.R_TimeB.SHT_Time` 
GROUP BY   subject_id, hadm_id  ,transfer_id    ) a
left join  `mimic-four-377221.R_TimeB.SHT_Time` b
on a.subject_id=b.subject_id and
a.hadm_id=b.hadm_id and
a.transfer_id=b.transfer_id and
a.mini=b.Timestamp) c

left join  `mimic-four-377221.R_TimeB.SHT_Time` d
on c.subject_id=d.subject_id and
c.hadm_id=d.hadm_id and
c.transfer_id=d.transfer_id and
c.maxi=d.Timestamp)
;

###########################################################################		

create Table  `mimic-four-377221.R_TimeC.C_ST_Time` as



(select 
c.subject_id,
c.transfer_id,
c.mini,
c.maxi,
c.Title_mini,
d.Title as Title_maxi
from

(select 
a.subject_id,
a.transfer_id,
a.mini,
a.maxi,
b.Title as Title_mini
from 
(SELECT 
subject_id, transfer_id, MIN(Timestamp) as mini, MAX(Timestamp) as maxi
FROM `mimic-four-377221.R_TimeB.ST_Time` 
GROUP BY   subject_id, transfer_id      ) a
left join  `mimic-four-377221.R_TimeB.ST_Time` b
on a.subject_id=b.subject_id and
a.transfer_id=b.transfer_id and
a.mini=b.Timestamp) c

left join  `mimic-four-377221.R_TimeB.ST_Time` d
on c.subject_id=d.subject_id and
c.transfer_id=d.transfer_id and
c.maxi=d.Timestamp)
;



###########################################################################		

create Table  `mimic-four-377221.R_TimeC.C_S_Time` as



(select 
c.subject_id,
c.mini,
c.maxi,
c.Title_mini,
d.Title as Title_maxi
from

(select 
a.subject_id,
a.mini,
a.maxi,
b.Title as Title_mini
from 
(SELECT 
subject_id,  MIN(Timestamp) as mini, MAX(Timestamp) as maxi
FROM `mimic-four-377221.R_TimeB.S_Time` 
GROUP BY   subject_id      ) a
left join  `mimic-four-377221.R_TimeB.S_Time` b
on a.subject_id=b.subject_id and
a.mini=b.Timestamp) c

left join  `mimic-four-377221.R_TimeB.S_Time` d
on c.subject_id=d.subject_id and
c.maxi=d.Timestamp)
;


###########################################################################		

create Table  `mimic-four-377221.R_TimeC.C_S_Date` as


(select 
c.subject_id,
c.mini,
c.maxi,
c.Title_mini,
d.Title as Title_maxi
from

(select 
a.subject_id,
a.mini,
a.maxi,
b.Title as Title_mini
from 
(SELECT 
subject_id,  MIN(Timestamp) as mini, MAX(Timestamp) as maxi
FROM `mimic-four-377221.R_TimeB.S_Date` 
GROUP BY   subject_id      ) a
left join  `mimic-four-377221.R_TimeB.S_Date` b
on a.subject_id=b.subject_id and
a.mini=b.Timestamp) c

left join  `mimic-four-377221.R_TimeB.S_Date` d
on c.subject_id=d.subject_id and
c.maxi=d.Timestamp)
;

###########################################################################		

'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
