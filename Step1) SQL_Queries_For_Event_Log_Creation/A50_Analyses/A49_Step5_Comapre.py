
FileName_EightDk="Dis_All"



###########################################################################################




print("")
print("############# STEP 1 : Warning  ############################################################################  ")
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import os

print("")
print("############# STEP 2 : Importing  ############################################################################  ")

symPath='../File_Analyses/Step3_compare/' + FileName_EightDk +'.csv'
Realpath = os.path.realpath(symPath)
df_Disorders = pd.read_csv(Realpath)




print("")
print("############# STEP 3 : Left Join  ############################################################################  ")



merged_df = df_Disorders


merged_df['col1_set'] = merged_df['Disorders_ML'].str.split(',')
merged_df['col2_set'] = merged_df['Disorders'].str.split(',')

#print(merged_df.to_string())

# calculate the intersection between the sets and the list of values
merged_df['common_values'] = merged_df.apply(lambda x: set(x['col1_set']) & set(x['col2_set']), axis=1)

merged_df['common_values'] = merged_df['common_values'].apply(lambda x: ','.join([str(i) for i in x]))

#print(merged_df.head())

new_df = merged_df[['Type', 'ActivityValueID', 'common_values']]
new_df = new_df.rename(columns={'common_values': 'Icd9_Code_Short_list'})
#print(new_df.head())

print("")
print("############# STEP 4 : Saving  ############################################################################  ")



symPath='../File_Analyses/Step3_compare/'+ FileName_EightDk + '_Final.csv'
Realpath = os.path.realpath(symPath)
new_df.to_csv(symPath, index=False)
