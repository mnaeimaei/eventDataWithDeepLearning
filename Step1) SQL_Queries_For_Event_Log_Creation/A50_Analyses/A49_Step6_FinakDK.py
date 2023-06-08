

FileName_EightDK="Dis_T_Final"
FileName_Dk_empty="4_M4_Event_Potential_ML"

print("")
print("############# STEP 1 : Warning  ############################################################################  ")
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import os

print("")
print("############# STEP 2 : Importing  ############################################################################  ")

symPath='../File_Analyses/Step3_DK/' + FileName_EightDK +'.csv'
Realpath = os.path.realpath(symPath)
df_EightDKs = pd.read_csv(Realpath)


symPath='../File_Analyses/Step3_DK/' + FileName_Dk_empty +'.csv'
Realpath = os.path.realpath(symPath)
df_Dk_empty = pd.read_csv(Realpath)

#print(df_EightDKs.head())
#print(df_Dk_empty.head())



print("")
print("############# STEP 3 : Left Join  ############################################################################  ")

df_Dk_empty_outputColumn=['dkID', 'Activity', 'Activity_Synonym', 'Activity_Origin', 'Activity_Value_ID']
df_EightDKs_outputColumn=['Icd9_Code_Short_list']
on_tableA=['Activity_Origin', 'Activity_Value_ID']
on_tableB=['Activity_Origin', 'ActivityValueID']

merged_df = pd.merge(df_Dk_empty, df_EightDKs, left_on=on_tableA, right_on=on_tableB, how='left')
#print(merged_df.to_string())

print("")
print("############# STEP 4 : Selection  ############################################################################  ")

new_df = merged_df[['dkID', 'Activity', 'Activity_Synonym', 'Activity_Origin', 'Activity_Value_ID', 'Icd9_Code_Short_list_y']]
new_df = new_df.rename(columns={'Icd9_Code_Short_list_y': 'Icd9_Code_Short_list'})
#print(new_df.to_string())

print("")
print("############# STEP 5 : Saving  ############################################################################  ")



symPath='../File_Analyses/Step3_DK/'+FileName_Dk_empty+'_Final.csv'
Realpath = os.path.realpath(symPath)
new_df.to_csv(symPath, index=False)