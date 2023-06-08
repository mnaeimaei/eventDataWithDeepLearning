import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

        CREATE TABLE  `mimic-four-377221.E4_Micro.Micro_B8`   AS
        SELECT * FROM 
        (SELECT
        b.rowNum, b.PC_1, b.PC_2, b.PC_3, b.PC_4, b.PC_5, b.PC_6, b.PC_7, b.PC_8, b.PC_9, b.PC_10, b.PC_11, b.PC_12, b.PC_13, b.PC_14, b.PC_15, b.PC_16, b.PC_17, b.PC_18, b.PC_19, b.PC_20, b.PC_21, b.PC_22, b.PC_23, b.PC_24, b.PC_25, b.PC_26, b.PC_27, b.PC_28, b.PC_29, b.PC_30, b.PC_31, b.PC_32, b.PC_33, b.PC_34, b.PC_35, b.PC_36, b.PC_37, b.PC_38, b.PC_39, b.PC_40, b.PC_41, b.PC_42, b.PC_43, b.PC_44, b.PC_45, b.PC_46, b.PC_47, b.PC_48, b.PC_49, b.PC_50, b.PC_51, b.PC_52, b.PC_53, b.PC_54, b.PC_55, b.PC_56, b.PC_57, b.PC_58, b.PC_59, b.PC_60, b.PC_61, b.PC_62, b.PC_63, b.PC_64, b.PC_65, b.PC_66, b.PC_67, b.PC_68, b.PC_69, b.PC_70, b.PC_71, b.PC_72, b.PC_73, b.PC_74, b.PC_75, b.PC_76, b.PC_77, b.PC_78, b.PC_79, b.PC_80,
        a.D01, a.D02, a.D03, a.D04, a.D05, a.D06, a.D07, a.D08, a.D09, a.D10, a.D11, a.D12, a.D13, a.D14, a.D15, a.D16, a.D17, a.D18, a.D19, a.D20, a.D21, a.D22, a.D23, a.D24, a.D25, a.D26, a.D27, a.D28, a.D29, a.D30, a.D31, a.D32, a.D33, a.D34, a.D35, a.D36, a.D37, a.D38, a.D39, a.D40, a.D41, a.D42, a.D43, a.D44, a.D45, a.D46, a.D47, a.D48, a.D49, a.D50, a.D51, a.D52, a.D53, a.D54, a.D55, a.D56, a.D57, a.D58, a.D59, a.D60, a.D61, a.D62, a.D63, a.D64, a.D65, a.D66, a.D67, a.D68, a.D69, a.D70, a.D71, a.D72, a.D73,
        From `mimic-four-377221.P_NonEvents.K7`   as a
        LEFT JOIN `mimic-four-377221.E4_Micro.Micro_B7`   as b
        ON
        a.HADM_ID=b.HADM_ID )
        WHERE PC_1 is not null
        ;



'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
