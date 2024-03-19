from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib as plt 
import pandas as pd

df=pd.read_csv('https://raw.githubusercontent.com/rasbt/'
              'python-machine-learning-book-2nd-edition'
              '/master/code/ch10/housing.data.txt',
              sep='\s+')
df.columns=['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS',
            'RAD','TAX','PTRATIO','B','LSTAT','MEDV']
print(df)

import matplotlib.pyplot as plt 
import seaborn as sns 
cols=['LSTAT','INDUS','NOX','RM','MEDV'] 
sns.pairplot(df[cols],height=2.5) 
plt.tight_layout() 
plt.show()

import numpy as np
cm=np.corrcoef(df[cols].values.T) 
# Difference Btw corr() and corrcoef()
# corr() : you will get labeling of the matrix as 0,1,2,.....
# corrcoef(): no labling of matrix
# .T means matrix inclined towards row-wise
# you can use (rowvar=False/True)

sns.set(font_scale=1.5)
hm=sns.heatmap(cm,cbar=True,annot=True,square=True,fmt='.2f',annot_kws={'size':15},yticklabels=cols,xticklabels=cols)
plt.show()

X=df[['RM']].values # Simple Linear Regression
# X - explainatory Variable
Y=df[['MEDV']].values
# Y - one Response Variable
from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(X,Y)
print("Slope: %.3f"%lr.coef_[0])
print("Intercept: %.3f"%lr.intercept_)

def lin_regplot(X,Y,model):
    plt.scatter(X,Y,c='green',s=70)
    plt.plot(X,model.predict(X))
    return None
lin_regplot(X,Y,lr)
plt.xlabel("Average number of rooms(RM)")
plt.ylabel("Price in $ (MEDV)")
plt.show() 


