



FileName="eLogFeatureClass_CMP"
componentNumber=3
stringList="pc"


id_col_List= ['rowNum']
X_col_list= ['Item7', 'Item10', 'Item11', 'Item12', 'Item13', 'Item15', 'Item28', 'Item30']
y_col_list= ['D01', 'D02', 'D03', 'D04', 'D05', 'D06', 'D07', 'D08', 'D09', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'D16', 'D17', 'D18', 'D19', 'D20', 'D21', 'D22', 'D23', 'D24', 'D25', 'D26', 'D27', 'D28', 'D29', 'D30', 'D31', 'D32', 'D33', 'D34', 'D35', 'D36', 'D37', 'D38', 'D39', 'D40', 'D41', 'D42', 'D43', 'D44', 'D45', 'D46', 'D47', 'D48', 'D49', 'D50', 'D51', 'D52', 'D53', 'D54', 'D55', 'D56', 'D57', 'D58', 'D59', 'D60', 'D61', 'D62', 'D63', 'D64', 'D65', 'D66', 'D67', 'D68', 'D69', 'D70', 'D71', 'D72', 'D73']
pred_col_list= ['Pred01', 'Pred02', 'Pred03', 'Pred04', 'Pred05', 'Pred06', 'Pred07', 'Pred08', 'Pred09', 'Pred10', 'Pred11', 'Pred12', 'Pred13', 'Pred14', 'Pred15', 'Pred16', 'Pred17', 'Pred18', 'Pred19', 'Pred20', 'Pred21', 'Pred22', 'Pred23', 'Pred24', 'Pred25', 'Pred26', 'Pred27', 'Pred28', 'Pred29', 'Pred30', 'Pred31', 'Pred32', 'Pred33', 'Pred34', 'Pred35', 'Pred36', 'Pred37', 'Pred38', 'Pred39', 'Pred40', 'Pred41', 'Pred42', 'Pred43', 'Pred44', 'Pred45', 'Pred46', 'Pred47', 'Pred48', 'Pred49', 'Pred50', 'Pred51', 'Pred52', 'Pred53', 'Pred54', 'Pred55', 'Pred56', 'Pred57', 'Pred58', 'Pred59', 'Pred60', 'Pred61', 'Pred62', 'Pred63', 'Pred64', 'Pred65', 'Pred66', 'Pred67', 'Pred68', 'Pred69', 'Pred70', 'Pred71', 'Pred72', 'Pred73']


X_col_list_final=id_col_List+y_col_list



print("")
print("############# STEP 1 : PCA  ############################################################################  ")


import warnings
warnings.filterwarnings('ignore')



#######################################################################################################


import pandas as pd
import os

symPath='../File_TrainingData/0DownloadedFiles/' + FileName +'.csv'
Realpath = os.path.realpath(symPath)
df = pd.read_csv(Realpath)



#######################################################################################################
rowID=df[id_col_List]
X = df.drop(X_col_list_final,axis=1)
y = df[y_col_list]
#print("X=\n",X)
#print("y=\n",y)




#######################################################################################################
from sklearn.preprocessing import StandardScaler
X_std = StandardScaler().fit_transform(X)
#print(X_std)



#######################################################################################################

def listBuilder(stringList,componentNumber):
    list1 = []
    for i in range(componentNumber):
        txt = f"{stringList}_{i + 1}"
        list1.append(txt)
    return list1

columnTitle=listBuilder(stringList,componentNumber)
#print(columnTitle)



#######################################################################################################
from sklearn.decomposition import PCA
pca = PCA(n_components=componentNumber) # Here we can also give the percentage as a paramter to the PCA function as pca = PCA(.95). .95 means that we want to include 95% of the variance. Hence PCA will return the no of components which describe 95% of the variance. However we know from above computation that 2 components are enough so we have passed the 2 components.
principalComponents = pca.fit_transform(X_std)
principalDf = pd.DataFrame(data = principalComponents , columns = columnTitle)

#print(principalDf.head(5))
#print(principalDf.to_string())

#######################################################################################################

finalDf = pd.concat([pd.DataFrame(rowID,columns = id_col_List),principalDf,pd.DataFrame(y,columns = y_col_list)], axis = 1)
#print(finalDf.head())
#print(finalDf.to_string())

#######################################################################################################

import os

symPath2='../File_TrainingData/0DownloadedFiles/PCA_' + FileName +'.csv'
Realpath2 = os.path.realpath(symPath2)
df2=finalDf.to_csv(Realpath2,index=False)

print("")
print("PCA was done")



