
FileName_AdmSer="F1"
FileName_Transfer="F2"
FileName_MicroA="F3"
FileName_MicroB="F4"
FileName_RT="F5"
FileName_CMP="F6"
FileName_ABG="F7"
FileName_Specimen="F8"



###########################################################################################


AdmSer_Type="Logistic"
Transfer_Type="Transfer"
MicroA_Type="Mirobiology_Sample"
MicroB_Type="Microbiology_Result"
RT_Type="Respiratory_Therapy"
CMP_Type="CMP"
ABG_Type="ABG"
Specimen_Type="ABG_specimen_type"


print("")
print("############# STEP 1 : Warning  ############################################################################  ")
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import os

print("")
print("############# STEP 2 : Importing  ############################################################################  ")

symPath='../File_Analyses/Step1_eight_Summary/' + FileName_AdmSer +'.csv'
Realpath = os.path.realpath(symPath)
df_AdmSer = pd.read_csv(Realpath)


symPath='../File_Analyses/Step1_eight_Summary/' + FileName_Transfer +'.csv'
Realpath = os.path.realpath(symPath)
df_Transfer = pd.read_csv(Realpath)

symPath='../File_Analyses/Step1_eight_Summary/' + FileName_MicroA +'.csv'
Realpath = os.path.realpath(symPath)
df_MicroA = pd.read_csv(Realpath)

symPath='../File_Analyses/Step1_eight_Summary/' + FileName_MicroB +'.csv'
Realpath = os.path.realpath(symPath)
df_MicroB= pd.read_csv(Realpath)

symPath='../File_Analyses/Step1_eight_Summary/' + FileName_RT +'.csv'
Realpath = os.path.realpath(symPath)
df_RT = pd.read_csv(Realpath)


symPath='../File_Analyses/Step1_eight_Summary/' + FileName_CMP +'.csv'
Realpath = os.path.realpath(symPath)
df_CMP = pd.read_csv(Realpath)

symPath='../File_Analyses/Step1_eight_Summary/' + FileName_ABG +'.csv'
Realpath = os.path.realpath(symPath)
df_ABG = pd.read_csv(Realpath)

symPath='../File_Analyses/Step1_eight_Summary/' + FileName_Specimen +'.csv'
Realpath = os.path.realpath(symPath)
df_Specimen = pd.read_csv(Realpath)

print("")
print("############# STEP 3 : Add Column  ############################################################################  ")



df_AdmSer['Activity_Origin']=AdmSer_Type
df_Transfer['Activity_Origin']=Transfer_Type
df_MicroA['Activity_Origin']=MicroA_Type
df_MicroB['Activity_Origin']=MicroB_Type
df_RT['Activity_Origin']=RT_Type
df_CMP['Activity_Origin']=CMP_Type
df_ABG['Activity_Origin']=ABG_Type
df_Specimen['Activity_Origin']=Specimen_Type


print("")
print("############# STEP 4 : Union  ############################################################################  ")

df_concatenated = pd.concat([df_AdmSer, df_Transfer, df_MicroA, df_MicroB, df_RT, df_CMP, df_ABG, df_Specimen])
#print(df_concatenated)

print("")
print("############# STEP 4 : Saving  ############################################################################  ")


symPath='../File_Analyses/Step1_eight_Summary/All_Dk.csv'
Realpath = os.path.realpath(symPath)
df_concatenated.to_csv(symPath, index=False)


