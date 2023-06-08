
FileName="eLogFeatureClass_Specimen"
id_col_List= ['rowNum']
y_col_list= ['D01', 'D02', 'D03', 'D04', 'D05', 'D06', 'D07', 'D08', 'D09', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'D16', 'D17', 'D18', 'D19', 'D20', 'D21', 'D22', 'D23', 'D24', 'D25', 'D26', 'D27', 'D28', 'D29', 'D30', 'D31', 'D32', 'D33', 'D34', 'D35', 'D36', 'D37', 'D38', 'D39', 'D40', 'D41', 'D42', 'D43', 'D44', 'D45', 'D46', 'D47', 'D48', 'D49', 'D50', 'D51', 'D52', 'D53', 'D54', 'D55', 'D56', 'D57', 'D58', 'D59', 'D60', 'D61', 'D62', 'D63', 'D64', 'D65', 'D66', 'D67', 'D68', 'D69', 'D70', 'D71', 'D72', 'D73']
X_col_list_final=id_col_List+y_col_list


print("")
print("############# STEP 1 : Ignore Warning  ############################################################################  ")


import warnings
warnings.filterwarnings('ignore')



print("")
print("############# STEP 2 : Importing File  ############################################################################  ")
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import os

symPath='../File_TrainingData/0DownloadedFiles/' + FileName +'.csv'
Realpath = os.path.realpath(symPath)
df = pd.read_csv(Realpath)



print("############# STEP 3 ############################################################################  ")


X = df.drop(X_col_list_final,axis=1)

#print(X)
#print(X.shape)


print("############# STEP 4 ############################################################################  ")
from sklearn.preprocessing import StandardScaler
X_std = StandardScaler().fit_transform(X)
#print(X_std)

print("############# STEP 5 #######################################################################  ")


import numpy as np
cov_mat = np.cov(X_std.T)
#print('Covariance_matrix \n%s' %cov_mat)

print("############# STEP 6 #######################################################################  ")


eig_vals, eig_vecs = np.linalg.eig(cov_mat)

#print('Eigenvectors \n%s' %eig_vecs)
#print('\nEigenvalues \n%s' %eig_vals)

print("############# STEP 7 ############################################################################  ")


sq_eig=[]
for i in eig_vecs:
    sq_eig.append(i**2)
#print(sq_eig)
sum(sq_eig)
#print("\nsum of squares of each values in an  eigen vector is \n", 0.27287211+ 0.13862096+0.51986524+ 0.06864169)
for ev in eig_vecs:
    #print(np.linalg.norm(ev))
    np.testing.assert_array_almost_equal(1.0, np.linalg.norm(ev))




print("############# STEP 8 ############################################################################  ")

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
var_exp = [(i / tot)*100 for i in sorted(eig_vals, reverse=True)]

cum_var_exp = np.cumsum(var_exp)

cum_var_exp02=var_exp[0:2]
sum_cum_var_exp02=sum(var_exp[0:2])
returnNumpyArray_cum_var_exp_71=returnNumpyArray(cum_var_exp,71)
returnNumpyArray_cum_var_exp_76=returnNumpyArray(cum_var_exp,76)
returnNumpyArray_cum_var_exp_81=returnNumpyArray(cum_var_exp,81)
returnNumpyArray_cum_var_exp_86=returnNumpyArray(cum_var_exp,86)
returnNumpyArray_cum_var_exp_91=returnNumpyArray(cum_var_exp,91)
returnNumpyArray_cum_var_exp_96=returnNumpyArray(cum_var_exp,96)




print("############# STEP 10 ############################################################################  ")


import contextlib
with open('../File_TrainingData/1PCA/PCA_'+ FileName +'.txt', 'w') as f:
    print('File Name = ',FileName, file=f)
    print('Algorithm = PCA', file=f)
    print("\nSum of eigen values\n", tot, file=f)
    print("\n\nVariance Explained\n", var_exp, file=f)
    print("\n\nCumulative Variance Explained\n", cum_var_exp, file=f)
    print("\n\nPercentage of variance the first two principal components each contain\n ",returnNumpyArray_cum_var_exp_71, file=f)
    print("\n\nPercentage of variance the first two principal components together contain\n", sum_cum_var_exp02, file=f)
    print("\n\nthe number first principal components that percentage of variance together is <=70 %\n",returnNumpyArray_cum_var_exp_71, file=f)
    print("\n\nthe number first principal components that percentage of variance together is <=75 %\n",returnNumpyArray_cum_var_exp_76, file=f)
    print("\n\nthe number first principal components that percentage of variance together is <=80 %\n",returnNumpyArray_cum_var_exp_81, file=f)
    print("\n\nthe number first principal components that percentage of variance together is <=85 %\n",returnNumpyArray_cum_var_exp_86, file=f)
    print("\n\nthe number first principal components that percentage of variance together is <=90 %\n",returnNumpyArray_cum_var_exp_91, file=f)
    print("\n\nthe number first principal components that percentage of variance together is <=95 %\n",returnNumpyArray_cum_var_exp_96, file=f)
    print(' ', file=f)


