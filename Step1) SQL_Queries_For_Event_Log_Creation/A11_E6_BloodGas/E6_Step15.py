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
import time

start = time.time()

print("")
print("############# STEP 1  ############################################################################  ")


symPath='../gcKey/ABG.csv'
Realpath = os.path.realpath(symPath)
df = pd.read_csv(Realpath)

print("")
print("############# STEP 2 : Transpose Data  ############################################################################  ")


df_T=df.set_index('rowNum').transpose()
df_T = df_T.reset_index()
df_T.rename(columns = {'index':'Items'}, inplace = True)
#print(df_T.to_string())
symPath2='../gcKey/ABG_Transposed.csv'
Realpath2 = os.path.realpath(symPath2)
df2=df_T.to_csv(Realpath2,index=False)

end = time.time()
print(end - start)
