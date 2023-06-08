




import warnings

warnings.filterwarnings('ignore')

#####################################################################################3

DatasetName = "D12_Test"
id_col_List= ['rowNum']
X_col_list= ['Item1', 'Item2', 'Item3', 'Item4']
y_col_list= ['D1', 'D2']
pred_col_list = ['Pred01', 'Pred02']

X_col_list_final = id_col_List + y_col_list
algName = "DeepMLP_HPT_CPU"

mainDirectory = "../File_TrainingData/"
dataSetDirectory = "0Dataset/"
SavingDirectory = "DeepMLP_CPU/"

# %%

import pandas as pd
import os

symPath = mainDirectory + dataSetDirectory + DatasetName + '.csv'
Realpath = os.path.realpath(symPath)
df = pd.read_csv(Realpath)

print(df)
print("")
print("Dataframe Types:")
print(df.dtypes)
print("")
print("Dataframe column:")
print(list(df.columns))

# %%


import matplotlib.pyplot as plt, seaborn as sns

plt.figure(figsize=(10, 5))
sns.heatmap(df.corr(), annot=True, cmap="rainbow")
plt.show()

print(df.describe())


# %%

X = df.drop(X_col_list_final, axis=1)
y = df[y_col_list]
print("X=\n", X)
print("y=\n", y)
eventFile = df.drop(y_col_list, axis=1)

# %%

from sklearn.preprocessing import StandardScaler

X_std = StandardScaler().fit_transform(X)
print(X_std)

# %%

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_std, y, train_size=0.6, random_state=50)
# print(X_train)
# print(y_train)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

# %%

import tensorflow as tf


def create_model(optimizer, num_neurons, num_hidden_layers):
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Dense(64, activation='relu', input_shape=(4,)))

    for i in range(num_hidden_layers):
        model.add(tf.keras.layers.Dense(num_neurons[i], activation='relu'))

    model.add(tf.keras.layers.Dense(2, activation='sigmoid'))

    model.compile(optimizer=optimizer,
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    return model


# %%

from tensorflow.keras.wrappers.scikit_learn import KerasClassifier

model = KerasClassifier(build_fn=create_model)

# %%

param_grid = {
    'batch_size': [16, 32],
    'epochs': [10, 20],
    'num_hidden_layers': [1, 2, 3],
    'num_neurons': [[128], [128, 256], [128, 256, 128]],  # Vary the number of neurons in each layer
    'optimizer': ['adam', 'rmsprop'],
}

# %%

from sklearn.model_selection import train_test_split, GridSearchCV

grid = GridSearchCV(estimator=model, param_grid=param_grid, cv=3)

# %%

grid_result = grid.fit(X_train, y_train)

# %%

print("Best: %f using %s" % (grid_result.best_score_, grid_result.best_params_))

# %%

best_model = grid_result.best_estimator_

# %%

import joblib

joblib.dump(best_model, mainDirectory + SavingDirectory + algName + "_" + DatasetName + '.joblib')


# %%

def evaluate_model(dt_best):
    loss, accuracy = dt_best.model.evaluate(X_test, y_test)
    print('Test loss:', loss)
    print('Test accuracy:', accuracy)


# %%

import contextlib

with open(mainDirectory + SavingDirectory + algName + "_" + DatasetName + '.txt', 'w') as f:
    print('File Name = ', DatasetName, file=f)
    print('Algorithm = ', algName, file=f)
    with contextlib.redirect_stdout(f):
        evaluate_model(best_model)

# %%

import joblib
import os

symPath = mainDirectory + SavingDirectory + algName + "_" + DatasetName + '.joblib'
Realpath = os.path.realpath(symPath)
clf = joblib.load(Realpath)

#######################################################################################################

import pandas as pd
import os

F = X_test
# print("F=\n",F)

y_pred_prob = clf.model.predict(F)
import numpy as np
y_pred = np.round(y_pred_prob)


#######################################################################################################


from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
# Calculate evaluation metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='micro')  # Choose appropriate average
recall = recall_score(y_test, y_pred, average='micro')  # Choose appropriate average
f1 = f1_score(y_test, y_pred, average='micro')
auc_roc = roc_auc_score(y_test, y_pred_prob)
with open(mainDirectory + SavingDirectory + algName + "_" + DatasetName + '2' +'.txt', 'w') as f:
    print("the accuracy of the model predictions compared to the true labels ", file=f)
    print('accuracy = ', accuracy, file=f)
    print('precision = ', precision, file=f)
    print('recall = ', recall, file=f)
    print('f1 = ', f1, file=f)
    print('auc_roc = ', auc_roc, file=f)
#############################################################3
E = X_std
# print("E=\n",E)

#######################################################################################################
predictions = clf.model.predict(X_test)
# print(predictions)
# print(type(predictions))
# print(predictions.shape)

#######################################################################################################
for i in range(predictions.shape[1]):
    predictions[predictions[:, i] >= 0.5, i] = 1
    predictions[predictions[:, i] < 0.5, i] = 0

predictions = predictions.astype(int)

# print(predictions)
#######################################################################################################

new_df = pd.DataFrame(predictions, columns=pred_col_list)
# print(new_df)
merged_df = pd.merge(eventFile, new_df, left_index=True, right_index=True, how='left')

symPath2 = mainDirectory + SavingDirectory + algName + "_" + DatasetName + '_Result.csv'
Realpath2 = os.path.realpath(symPath2)
merged_df.to_csv(Realpath2, index=False)

# %%

Realpath = os.path.realpath(symPath2)
df3 = pd.read_csv(Realpath)


############################################################################################3
def finalColumn(dataFrame, predinction_col_list, identifier_col_List):
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

df4, finalItems = finalColumn(df3, pred_col_list, id_col_List)
# print(df4)
# print(finalItems)
df5 = df4[finalItems]

############################################################################################3

symPath4 = mainDirectory + SavingDirectory + algName + "_" + DatasetName + '_Result_Summary.csv'
Realpath4 = os.path.realpath(symPath4)
df5.to_csv(Realpath4, index=False)