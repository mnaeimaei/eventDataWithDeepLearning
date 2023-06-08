import csv
import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.spatial.distance import pdist, squareform
from scipy import exp
from sklearn.preprocessing import StandardScaler
from scipy.linalg import eigh

print("")
print("############# STEP 1 : Ignore Warning  ############################################################################  ")


import warnings

warnings.filterwarnings('ignore')


print("")
print("############# STEP 2 : Importing the Data  ############################################################################  ")

symPath='../gcKey/ABG_Transposed.csv'
Realpath = os.path.realpath(symPath)
df = pd.read_csv(Realpath)
#print(df.head())

print("")
print("############# STEP 3 : Deviding DataFrames  ############################################################################  ")

X = df.iloc[:, 1:]
y = df[["Items"]]
print("")
print("dataset X:")
#print(X.to_string)
print("")
print("dataset X firsts rows:")
#print(X.head())
print("")
print("Check shape of the dataset X:")
#print(X.shape)
print("")
print("View summary of dataset X: ")
#print(X.info())
print("")
print("Check for missing values in dataset: ")
#print(X.isnull().sum())
print("")
print("View the statistical summary of numerical variables :")
#print(X.describe())


print("")
print("dataset y:")
#print(y)
print("")
print("Check shape of the dataset Y:")
#print(y.shape)


print("")
print("############# STEP 3 : Ranging Chart  ############################################################################  ")


rowN=len(df. index)
print("Number of rows:")
print(rowN)

ChartRange=10

print("")
print("############# STEP 4  : Feature Scaling  ############################################################################  ")

'''
cols = X.columns

from sklearn.preprocessing import MinMaxScaler

ms = MinMaxScaler()

X = ms.fit_transform(X)

X = pd.DataFrame(X, columns=[cols])
print(X.head())

'''


print("")
print("############# STEP 5  : Elbow  ############################################################################  ")

'''

from sklearn.cluster import KMeans
cs = []
for i in range(1, ChartRange):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
    kmeans.fit(X)
    cs.append(kmeans.inertia_)
plt.plot(range(1, ChartRange), cs)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('CS')
plt.savefig(os.path.realpath('../gcKey/Clustring_Elbow_ABG.png'))
plt.show()



print("")
print("############# STEP 5  : silhouette  ############################################################################  ")


import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_score

# Generate sample data
#X, y = make_blobs(n_samples=1000, centers=4, random_state=42)

# Perform K-means clustering for a range of K values
silhouette_scores = []
for k in range(2, ChartRange):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    score = silhouette_score(X, kmeans.labels_)
    silhouette_scores.append(score)

# Plot silhouette scores against K values
plt.plot(range(2, ChartRange), silhouette_scores)
plt.xlabel('Number of clusters')
plt.ylabel('Silhouette score')
plt.savefig(os.path.realpath('../gcKey/Clustring_Silhouette_ABG.png'))
plt.show()
plt.show()

'''
print("")
print("############# STEP 5 : Clustring based on Elbow and Add the cluster labels ############################################################################  ")

Clust_num=4



print("")
print("############# STEP 5 : Clustring based on Elbow and Add the cluster labels ############################################################################  ")

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=Clust_num, random_state=0)

kmeans.fit(X)


labels = kmeans.labels_

X['Cluster'] = labels
#print(X)




print("")
print("############# STEP 17 : K-Means model parameters study  ############################################################################  ")

df['Cluster'] = labels
#print(df)

print("")
df_clustered = df[["Items","Cluster"]]
#print(df_clustered)

symPath2='../gcKey/ABG_Clustered.csv'
Realpath2 = os.path.realpath(symPath2)
df2=df.to_csv(Realpath2,index=False)

symPath2='../gcKey/ABG_Clustered_Summary.csv'
Realpath2 = os.path.realpath(symPath2)
df2=df_clustered.to_csv(Realpath2,index=False)
