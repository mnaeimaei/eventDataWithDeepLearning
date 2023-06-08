import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            


create table `mimic-four-377221.E4_Micro.Micro_B5`    as

SELECT 

subject_id, hadm_id, Timestamp, Activity, Activity_Synonym, TYPE, Property, 

Test_1, Test_2, Test_3, Test_4, Test_5, Test_6, Test_7, Test_8, Test_9, Test_10, Test_11, Test_12, Test_13, Test_14, Test_15, Test_16, Test_17, Test_18, Test_19, Test_20, Test_21, Test_22, Test_23, Test_24, Test_25, Test_26, Test_27, Test_28, Test_29, Test_30, Test_31, Test_32, Test_33, Test_34, Test_35, Test_36, Test_37, Test_38, Test_39, Test_40, Test_41, Test_42, Test_43, Test_44, Test_45, Test_46, Test_47, Test_48, Test_49, Test_50, Test_51, Test_52, Test_53, Test_54, Test_55, Test_56, Test_57, Test_58, Test_59, Test_60, Test_61, Test_62, Test_63, Test_64, Test_65, Test_66, Test_67, Test_68, Test_69, Test_70, Test_71, Test_72, Test_73, Test_74, Test_75, Test_76, Test_77, Test_78, Test_79, Test_80, Test_81, Test_82, Test_83, Test_84, Test_85, Test_86, Test_87, Test_88, Test_89, Test_90, Test_91, Test_92, Test_93, Test_94, Test_95, Test_96, Test_97, Test_98, Test_99, Test_100, Test_101, Test_102, Test_103, Test_104, Test_105, Test_106, Test_107, Test_108, Test_109, Test_110, Test_111, Test_112, Test_113, Test_114, Test_115, Test_116, Test_117, Test_118, Test_119, Test_120, Test_121, Test_122, Test_123, Test_124, Test_125, Test_126, Test_127, Test_128, Test_129, Test_130, Test_131, Test_132, Test_133, Test_134, Test_135, Test_136, Test_137, Test_138, Test_139, Test_140, Test_141, Test_142, Test_143, Test_144, Test_145, Test_146, Test_147, Test_148, Test_149, Test_150, Test_151, Test_152, Test_153, Test_154, Test_155, Test_156, Test_157, Test_158, Test_159, Test_160, Test_161, Test_162, Test_163, Test_164, Test_165, Test_166, Test_167, Test_168, Test_169, Test_170, Test_171

FROM `mimic-four-377221.E4_Micro.Micro_B4` 


'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
