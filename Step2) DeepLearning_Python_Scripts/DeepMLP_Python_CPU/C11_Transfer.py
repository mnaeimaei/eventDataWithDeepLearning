





import warnings

warnings.filterwarnings('ignore')

#####################################################################################3

DatasetName = "D11_Transfer"
id_col_List= ['rowNum']
X_col_list= ['a1', 'a2']
y_col_list= ['D01', 'D02', 'D03', 'D04', 'D05', 'D06', 'D07', 'D08', 'D09', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'D16', 'D17', 'D18', 'D19', 'D20', 'D21', 'D22', 'D23', 'D24', 'D25', 'D26', 'D27', 'D28', 'D29', 'D30', 'D31', 'D32', 'D33', 'D34', 'D35', 'D36', 'D37', 'D38', 'D39', 'D40', 'D41', 'D42', 'D43', 'D44', 'D45', 'D46', 'D47', 'D48', 'D49', 'D50', 'D51', 'D52', 'D53', 'D54', 'D55', 'D56', 'D57', 'D58', 'D59', 'D60', 'D61', 'D62', 'D63', 'D64', 'D65', 'D66', 'D67', 'D68', 'D69', 'D70', 'D71', 'D72', 'D73']
pred_col_list= ['Pred01', 'Pred02', 'Pred03', 'Pred04', 'Pred05', 'Pred06', 'Pred07', 'Pred08', 'Pred09', 'Pred10', 'Pred11', 'Pred12', 'Pred13', 'Pred14', 'Pred15', 'Pred16', 'Pred17', 'Pred18', 'Pred19', 'Pred20', 'Pred21', 'Pred22', 'Pred23', 'Pred24', 'Pred25', 'Pred26', 'Pred27', 'Pred28', 'Pred29', 'Pred30', 'Pred31', 'Pred32', 'Pred33', 'Pred34', 'Pred35', 'Pred36', 'Pred37', 'Pred38', 'Pred39', 'Pred40', 'Pred41', 'Pred42', 'Pred43', 'Pred44', 'Pred45', 'Pred46', 'Pred47', 'Pred48', 'Pred49', 'Pred50', 'Pred51', 'Pred52', 'Pred53', 'Pred54', 'Pred55', 'Pred56', 'Pred57', 'Pred58', 'Pred59', 'Pred60', 'Pred61', 'Pred62', 'Pred63', 'Pred64', 'Pred65', 'Pred66', 'Pred67', 'Pred68', 'Pred69', 'Pred70', 'Pred71', 'Pred72', 'Pred73']


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