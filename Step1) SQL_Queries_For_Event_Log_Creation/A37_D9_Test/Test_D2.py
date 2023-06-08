

FileName="Test"
componentNumber=3
stringList="pc"

id_col_List= ['rowNum']
X_col_list= ['Item1', 'Item2', 'Item3', 'Item4']
y_col_list= ['D1', 'D2']
pred_col_list= ['Pred1', 'Pred2']
X_col_list_final=id_col_List+y_col_list
algType="D2_DecisionTree_"
algorithmDir="DecisionTree"
#algorithmDir="LogisticRegression"
#algorithmDir="RandomForest"


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


print("")
print("############# STEP 2 : Files  ############################################################################  ")

FileName="PCA_" + FileName
X_col_list= columnTitle

print("")
print("Files was done")



print("")
print("############# STEP 1 : Decision_Tree  ############################################################################  ")
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import os

symPath='../File_TrainingData/0DownloadedFiles/' + FileName +'.csv'
Realpath = os.path.realpath(symPath)
df = pd.read_csv(Realpath)


#######################################################################################################


X = df.drop(X_col_list_final,axis=1)
y = df[y_col_list]
#print("X=\n",X)
#print("y=\n",y)
eventFile=df.drop(y_col_list,axis=1)

#######################################################################################################

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.6, random_state=50)
#print(X_train)
#print(y_train)
#print(X_train.shape)
#print(X_test.shape)


#######################################################################################################

from sklearn import tree
from sklearn.multioutput import MultiOutputClassifier
from sklearn.model_selection import GridSearchCV


dt_classifier = tree.DecisionTreeClassifier(random_state=42)
multi_classifier = MultiOutputClassifier(dt_classifier)

# Define the hyperparameter grid for the internal estimator (DecisionTreeClassifier)
param_grid = {"estimator__max_depth": [2, 3, 4, 5],
              "estimator__min_samples_split": [2, 4, 6, 8],
              "estimator__min_samples_leaf": [1, 2, 3],
              "estimator__criterion": ["gini", "entropy"]}

# Create a GridSearchCV object
grid_search = GridSearchCV(multi_classifier, param_grid=param_grid, cv=5)

# Fit the GridSearchCV object to the data
grid_search.fit(X_train, y_train)


#print(grid_search.fit(X_train, y_train))


#######################################################################################################

score_df = pd.DataFrame(grid_search.cv_results_)
#print(score_df.to_string())


#######################################################################################################

score_df_large=score_df.nlargest(5,"mean_test_score")
#print(score_df_large.to_string())

#######################################################################################################

dt_best = grid_search.best_estimator_
#print(dt_best)


#######################################################################################################


#print("Tuned Decision Tree Parameters: {}".format(grid_search.best_params_))
#print("Best train score is {}".format(grid_search.best_score_))


#######################################################################################################

dt_best.fit(X_train, y_train)





#######################################################################################################
from sklearn.metrics import confusion_matrix, accuracy_score, f1_score, classification_report

def evaluate_model(dt_classifier):
    print("Train Accuracy :", accuracy_score(y_train, dt_classifier.predict(X_train)))
    print("Test Accuracy (Evaluation) :", accuracy_score(y_test, dt_classifier.predict(X_test)))
    print("Test Accuracy (Evaluation) :", dt_classifier.score(X_test, y_test))
    print("Test F1 Score (Evaluation) :", f1_score(y_test, dt_classifier.predict(X_test), average='macro'))
    print("Test Scores (Evaluation) :\n", classification_report(y_test, dt_classifier.predict(X_test)))


#######################################################################################################

evaluate_model(dt_best)

import contextlib
with open('../File_TrainingData/'+algorithmDir+'/'+algType+ FileName +'.txt', 'w') as f:
    print('File Name = ',FileName, file=f)
    print('Algorithm = ', algType, file=f)
    print(' ', file=f)
    #print('Hello, World!', file=f)
    with contextlib.redirect_stdout(f):
        evaluate_model(dt_best)


#######################################################################################################

import joblib
joblib.dump(dt_best,'../File_TrainingData/'+algorithmDir+'/'+algType+FileName+'.joblib')

#######################################################################################################




print("")
print("############# STEP 2 : Using Decition Tree ############################################################################  ")


#######################################################################################################

import joblib
import os

symPath='../File_TrainingData/'+algorithmDir+'/'+algType+FileName+'.joblib'
Realpath = os.path.realpath(symPath)
clf = joblib.load(Realpath)


#######################################################################################################

import pandas as pd
import os


E = eventFile.drop(id_col_List,axis=1)
#print("E=\n",E)



#######################################################################################################
predictions = clf.predict(E)
#print(predictions)


#######################################################################################################

new_df = pd.DataFrame(predictions, columns=pred_col_list)
#print(new_df)
merged_df = pd.merge(eventFile, new_df, left_index=True, right_index=True, how='left')



symPath2='../File_TrainingData/'+algorithmDir+'/'+algType+FileName +  '_Result.csv'
Realpath2 = os.path.realpath(symPath2)
merged_df.to_csv(Realpath2,index=False)


print("")
print("############# STEP 3 : Create Final File ############################################################################  ")



Realpath = os.path.realpath(symPath2)
df3 = pd.read_csv(Realpath)

############################################################################################3
def finalColumn(dataFrame, predinction_col_list,identifier_col_List):
    dataFrame['Disorders'] = "No_Diesease"
    for i in range(len(predinction_col_list)):
        new_list1 = predinction_col_list.copy()
        new_list2 = new_list1[i]
        txt1 = f"{i + 1}"
        dataFrame.loc[dataFrame[new_list2] == 1, 'Disorders'] = dataFrame['Disorders'] + "," + txt1

    dataFrame['Disorders'] = dataFrame['Disorders'].str.replace('No_Diesease,', "")
    finalItems = identifier_col_List.copy()
    finalItems.append('Disorders')

    return dataFrame, finalItems

############################################################################################

df4, finalItems=finalColumn(df3,pred_col_list,id_col_List)
#print(df4)
#print(finalItems)
df5=df4[finalItems]

############################################################################################3

symPath4='../File_TrainingData/'+algorithmDir+'/'+algType+FileName + '_Result_Summary.csv'
Realpath4 = os.path.realpath(symPath4)
df5.to_csv(Realpath4,index=False)






