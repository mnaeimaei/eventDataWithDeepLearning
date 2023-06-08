import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

        CREATE TABLE  `mimic-four-377221.E4_Micro.Micro_B9`   AS
SELECT 
rowNum	,PC_1	,PC_2	,PC_3	,PC_4	,PC_5	,PC_6	,PC_7	,
PC_8	,PC_9	,PC_10	,PC_11	,PC_12	,PC_13	,PC_14	,PC_15	,
PC_16	,PC_17	,PC_18	,PC_19	,PC_20	,PC_21	,PC_22	,PC_23	,
PC_24	,PC_25	,PC_26	,PC_27	,PC_28	,PC_29	,PC_30	,PC_31	,
PC_32	,PC_33	,PC_34	,PC_35	,PC_36	,PC_37	,PC_38	,PC_39	,
PC_40	,PC_41	,PC_42	,PC_43	,PC_44	,PC_45	,PC_46	,PC_47	,
PC_48	,PC_49	,PC_50	,PC_51	,PC_52	,PC_53	,PC_54	,PC_55	,
PC_56	,PC_57	,PC_58	,PC_59	,PC_60	,PC_61	,PC_62	,PC_63	,
PC_64	,PC_65	,PC_66	,PC_67	,PC_68	,PC_69	,PC_70	,PC_71	,
PC_72	,PC_73	,PC_74	,PC_75	,PC_76	,PC_77	,PC_78	,PC_79	,PC_80	


 FROM `mimic-four-377221.E4_Micro.Micro_B8` 

'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
