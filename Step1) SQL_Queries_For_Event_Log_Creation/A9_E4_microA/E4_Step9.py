import inline as inline
import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import os

print("")
print("############# STEP 1 : Ignore Warning  ############################################################################  ")


import warnings

warnings.filterwarnings('ignore')

print("############# STEP 1 ############################################################################  ")

symPath='../gcKey/Micro.csv'
Realpath = os.path.realpath(symPath)
df = pd.read_csv(Realpath)



#print(df.to_string())
print(df)

print("############# STEP 2 ############################################################################  ")

#No need
print("############# STEP 3 ############################################################################  ")


dimNumber=171
classColumnTitle= ['rowNum']

X = df.iloc[:,1:dimNumber+1].values
y = df.iloc[:,0].values


print(X)
print(X.shape)
print(y)
print(y.shape)


print("############# STEP 4 ############################################################################  ")

X_std = StandardScaler().fit_transform(X)
print(X_std)

print("############# STEP 10 ############################################################################  ")
#Part 1

print("############# STEP 11 ############################################################################  ")


componentNumber=80
stringList="PC"

def listBuilder(stringList,componentNumber):
    list1 = []
    for i in range(componentNumber):
        txt = f"{stringList}_{i + 1}"
        list1.append(txt)
    return list1

columnTitle=listBuilder(stringList,componentNumber)
print(columnTitle)


print("############# Step5,6,7,8,9,12,13 #######################################################################  ")

pca = PCA(n_components=componentNumber) # Here we can also give the percentage as a paramter to the PCA function as pca = PCA(.95). .95 means that we want to include 95% of the variance. Hence PCA will return the no of components which describe 95% of the variance. However we know from above computation that 2 components are enough so we have passed the 2 components.
principalComponents = pca.fit_transform(X_std)
principalDf = pd.DataFrame(data = principalComponents , columns = columnTitle)

#print(principalDf.head(5))
#print(principalDf.to_string())

print("############# STEP 14 ############################################################################  ")


finalDf = pd.concat([pd.DataFrame(y,columns = classColumnTitle),principalDf], axis = 1)
#print(finalDf.head())
print(finalDf.head())

print("############# STEP Saving Dataframe ############################################################################  ")


import os
symPath2='../gcKey/micro_wo_Approach1.csv'
Realpath2 = os.path.realpath(symPath2)
df2=finalDf.to_csv(Realpath2,index=False)
