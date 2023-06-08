import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            



        CREATE TABLE  `mimic-four-377221.E4_Micro.Micro_B7`   AS
        SELECT
        a.rowNum, a.subject_id, a.hadm_id, a.Timestamp,
        b.PC_1, b.PC_2, b.PC_3, b.PC_4, b.PC_5, b.PC_6, b.PC_7, b.PC_8, b.PC_9, b.PC_10, b.PC_11, b.PC_12, b.PC_13, b.PC_14, b.PC_15, b.PC_16, b.PC_17, b.PC_18, b.PC_19, b.PC_20, b.PC_21, b.PC_22, b.PC_23, b.PC_24, b.PC_25, b.PC_26, b.PC_27, b.PC_28, b.PC_29, b.PC_30, b.PC_31, b.PC_32, b.PC_33, b.PC_34, b.PC_35, b.PC_36, b.PC_37, b.PC_38, b.PC_39, b.PC_40, b.PC_41, b.PC_42, b.PC_43, b.PC_44, b.PC_45, b.PC_46, b.PC_47, b.PC_48, b.PC_49, b.PC_50, b.PC_51, b.PC_52, b.PC_53, b.PC_54, b.PC_55, b.PC_56, b.PC_57, b.PC_58, b.PC_59, b.PC_60, b.PC_61, b.PC_62, b.PC_63, b.PC_64, b.PC_65, b.PC_66, b.PC_67, b.PC_68, b.PC_69, b.PC_70, b.PC_71, b.PC_72, b.PC_73, b.PC_74, b.PC_75, b.PC_76, b.PC_77, b.PC_78, b.PC_79, b.PC_80,
        From `mimic-four-377221.E4_Micro.Micro_B2`   as a
        LEFT JOIN `mimic-four-377221.E4_Micro.Micro_B6_DR`   as b
        ON
        a.rowNum=b.rowNum 
        ;


'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
