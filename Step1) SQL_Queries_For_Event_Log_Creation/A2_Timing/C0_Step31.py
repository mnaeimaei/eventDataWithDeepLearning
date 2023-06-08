import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            





################################################


#Step1
update `mimic-four-377221.R_TimeI.I_All_p22` 
set 
s1=subject_id, h1=hadm_id, i1=stay_id, t1=transfer_id, min1=min_S, max1=max_S

where min_S=min_T and max_S=max_T;



###########################################################################################



#Step2
update `mimic-four-377221.R_TimeI.I_All_p22` 
set 
s1=subject_id, h1=0,       i1=stay_id, t1=transfer_id, min1=min_T, max1=min_S,
s2=subject_id, h2=hadm_id, i2=stay_id, t2=transfer_id, min2=min_S, max2=max_S


where min_S>min_T and max_S=max_T;


###########################################################################################



#Step3
update `mimic-four-377221.R_TimeI.I_All_p22` 
set 
s1=subject_id, h1=0,       i1=stay_id, t1=transfer_id, min1=min_T, max1=min_S,
s2=subject_id, h2=hadm_id, i2=stay_id, t2=transfer_id, min2=min_S, max2=max_T,
s3=subject_id, h3=hadm_id, i3=0,       t3=0,           min3=max_T, max3=max_S

where min_S>min_T and max_S>max_T;


###########################################################################################



#Step4
update `mimic-four-377221.R_TimeI.I_All_p22` 
set 
s1=subject_id, h1=0,       i1=stay_id, t1=transfer_id, min1=min_T, max1=min_S,
s2=subject_id, h2=hadm_id, i2=stay_id, t2=transfer_id, min2=min_S, max2=max_S,
s3=subject_id, h3=0,       i3=stay_id, t3=transfer_id, min3=max_S, max3=max_T

where min_S>min_T and max_S<max_T;


###########################################################################################



#Step5
update `mimic-four-377221.R_TimeI.I_All_p22` 
set 
s1=subject_id, h1=hadm_id, i1=0,       t1=0,           min1=min_S, max1=min_T,
s2=subject_id, h2=hadm_id, i2=stay_id, t2=transfer_id, min2=min_T, max2=max_S

where min_S<min_T and max_S=max_T;


###########################################################################################



#Step6
update `mimic-four-377221.R_TimeI.I_All_p22` 
set 
s1=subject_id, h1=hadm_id, i1=0,       t1=0,           min1=min_S, max1=min_T,
s2=subject_id, h2=hadm_id, i2=stay_id, t2=transfer_id, min2=min_T, max2=max_T,
s3=subject_id, h3=hadm_id, i3=0,       t3=0,           min3=max_T, max3=max_S

where min_S<min_T and max_S>max_T;



###########################################################################################



#Step7
update `mimic-four-377221.R_TimeI.I_All_p22` 
set 
s1=subject_id, h1=hadm_id, i1=0,       t1=0,           min1=min_S, max1=min_T,
s2=subject_id, h2=hadm_id, i2=stay_id, t2=transfer_id, min2=min_T, max2=max_S,
s3=subject_id, h3=0,       i3=stay_id, t3=transfer_id, min3=max_S, max3=max_T

where min_S<min_T and max_S<max_T;


###########################################################################################



#Step8
update `mimic-four-377221.R_TimeI.I_All_p22` 
set 
s1=subject_id, h1=hadm_id, i1=stay_id, t1=transfer_id, min1=min_S, max1=max_T,
s2=subject_id, h2=hadm_id, i2=0,       t2=0,           min2=max_T, max2=max_S


where min_S=min_T and max_S>max_T;



###########################################################################################



#Step9
update `mimic-four-377221.R_TimeI.I_All_p22` 
set 
s1=subject_id, h1=hadm_id, i1=stay_id, t1=transfer_id, min1=min_S, max1=max_S,
s2=subject_id, h2=0,       i2=stay_id, t2=transfer_id, min2=max_S, max2=max_T


where min_S=min_T and max_S<max_T;


###########################################################################################



#Step10
update `mimic-four-377221.R_TimeI.I_All_p22` 
set 
s1=subject_id, h1=0,       i1=stay_id, t1=transfer_id, min1=min_S, max1=max_S,
s2=subject_id, h2=hadm_id, i2=0,       t2=0,           min2=min_T, max2=max_T


where min_S>min_T and min_S>=max_T and max_S>min_T and max_S>max_T;



###########################################################################################



#Step11
update `mimic-four-377221.R_TimeI.I_All_p22` 
set 
s1=subject_id, h1=0,       i1=stay_id, t1=transfer_id, min1=min_S, max1=max_S,
s2=subject_id, h2=hadm_id, i2=0,       t2=0,           min2=min_T, max2=max_T

where min_S<min_T and min_S<max_T and max_S<=min_T and max_S<max_T;



###########################################################################################





'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
