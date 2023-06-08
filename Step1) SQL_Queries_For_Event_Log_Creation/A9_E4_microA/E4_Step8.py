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

print("############# STEP 5 #######################################################################  ")



cov_mat = np.cov(X_std.T)
print('Covariance_matrix \n%s' %cov_mat)

print("############# STEP 6 #######################################################################  ")


eig_vals, eig_vecs = np.linalg.eig(cov_mat)

print('Eigenvectors \n%s' %eig_vecs)
print('\nEigenvalues \n%s' %eig_vals)

print("############# STEP 7 ############################################################################  ")
'''

sq_eig=[]
for i in eig_vecs:
    sq_eig.append(i**2)
print(sq_eig)
sum(sq_eig)
print("\nsum of squares of each values in an  eigen vector is \n", 0.27287211+ 0.13862096+0.51986524+ 0.06864169)
for ev in eig_vecs:
    print(np.linalg.norm(ev))
    np.testing.assert_array_almost_equal(1.0, np.linalg.norm(ev))

'''
print("############# STEP 10 ############################################################################  ")

def returnNumpyArray(arr, num):
    # Find the indices of the elements that are less than num
    indices = np.where(arr < num)[0]
    if indices.size == 0:
        # Handle the case where there are no elements less than num
        return None
    # Find the maximum value among those elements
    max_val = np.max(arr[indices])
    if max_val <= num:
        # Find the index of the maximum value
        max_index = np.where(arr == max_val)[0][0]
        return max_index + 1
    else:
        # Handle the case where the maximum value is greater than num
        return None


import os

tot = sum(eig_vals)
print("\nSum of eigen values\n",tot)
var_exp = [(i / tot)*100 for i in sorted(eig_vals, reverse=True)]
print("\n\n1. Variance Explained\n",var_exp)
cum_var_exp = np.cumsum(var_exp)

print("\n\n2. Cumulative Variance Explained\n",cum_var_exp)
print("\n\n3. Percentage of variance the first two principal components each contain\n ",var_exp[0:2])
print("\n\n4. Percentage of variance the first two principal components together contain\n",sum(var_exp[0:2]))
print("\n\n5. the number first principal components that percentage of variance together is <=70 %\n",returnNumpyArray(cum_var_exp,71))
print("\n\n5. the number first principal components that percentage of variance together is <=75 %\n",returnNumpyArray(cum_var_exp,76))
print("\n\n5. the number first principal components that percentage of variance together is <=80 %\n",returnNumpyArray(cum_var_exp,81))
print("\n\n5. the number first principal components that percentage of variance together is <=85 %\n",returnNumpyArray(cum_var_exp,86))
print("\n\n5. the number first principal components that percentage of variance together is <=90 %\n",returnNumpyArray(cum_var_exp,91))
print("\n\n5. the number first principal components that percentage of variance together is <=95 %\n",returnNumpyArray(cum_var_exp,96))


'''

xint = range(1, len(cum_var_exp) + 1)
plt.plot(xint, cum_var_exp)


plt.xlabel("Number of components")
plt.ylabel("Cumulative explained variance")
plt.xticks(xint)
plt.xlim(1, 4, 1)
plt.savefig(os.path.realpath('../gcKey/DimReduc_PCA_EVD_iris_1.png'))
plt.show()

print("############# STEP 10: Approach 1 ############################################################################  ")
import seaborn as sns
df.corr()
correlation = df.corr()
plt.figure(figsize=(10,10))
sns.heatmap(correlation, vmax=1, square=True,annot=True,cmap='cubehelix')

plt.title('Correlation between different fearures')
plt.savefig(os.path.realpath('../gcKey/DimReduc_PCA_EVD_iris_2.png'))
plt.show()


print("############# STEP 10: Approach 2 ############################################################################  ")

cov_mat_std_norm=(cov_mat).dot((cov_mat.shape[0]-1) / (cov_mat.shape[0]))
print(cov_mat_std_norm)


plt.figure(figsize=(8,8))
sns.heatmap(cov_mat_std_norm, vmax=1, square=True,annot=True,cmap='cubehelix')

plt.title('Correlation between different features')
plt.savefig(os.path.realpath('../gcKey/DimReduc_PCA_EVD_iris_3.png'))
plt.show()

'''