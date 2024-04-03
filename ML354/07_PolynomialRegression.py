from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score,mean_squared_error
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_csv('https://raw.githubusercontent.com/rasbt/'
              'python-machine-learning-book-2nd-edition'
              '/master/code/ch10/housing.data.txt',
              sep='\s+')
df.columns=['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS',
            'RAD','TAX','PTRATIO','B','LSTAT','MEDV']
X=df[['LSTAT']].values # Simple Linear Regression
# X - explainatory Variable
y=df[['MEDV']].values

regr=LinearRegression()

# Creating Quadratic features
quadratic=PolynomialFeatures(degree=2)
cubic=PolynomialFeatures(degree=3)
X4=PolynomialFeatures(degree=4)
X_quad=quadratic.fit_transform(X)
X_cubic=cubic.fit_transform(X)
X_4=X4.fit_transform(X)

# Fit the features
X_fit=np.arange(X.min(),X.max(),1)[:,np.newaxis]
regr=regr.fit(X,y)
y_lin_fit=regr.predict(X_fit)
linear_r2=r2_score(y,regr.predict(X))

print("Linear R2_Score: %.3f"%linear_r2)

# X_fit1=np.arange(X_quad.min(),X_quad.max(),1)[:,np.newaxis]
regr=regr.fit(X_quad,y)
y_quad_fit=regr.predict(quadratic.fit_transform(X_fit))
quadratic_r2=r2_score(y,regr.predict(X_quad))
print("Quadratic R2_Score: %.3f"%quadratic_r2)

regr=regr.fit(X_cubic,y)
y_cubic_fit=regr.predict(cubic.fit_transform(X_fit))
cubic_r2=r2_score(y,regr.predict(X_cubic))
print("Cubic R2_Score: %.3f"%cubic_r2)

regr=regr.fit(X_4,y)
y_4_fit=regr.predict(X4.fit_transform(X_fit))
X4_r2=r2_score(y,regr.predict(X_4))
print("Power4 R2_Score: %.3f"%X4_r2)

plt.scatter(X,y,label='Training points',color='lightblue')
plt.plot(X_fit,y_lin_fit,label='Linear ( d = 1 )',lw=2,linestyle=":")
plt.plot(X_fit,y_quad_fit,label='Linear ( d = 2 )',lw=2,linestyle="-",color='green')
plt.plot(X_fit,y_cubic_fit,label='Linear ( d = 3 )',lw=2,linestyle="--",color='red')
plt.plot(X_fit,y_4_fit,label='Linear ( d = 4 )',lw=2,linestyle="-.",color='yellow')
plt.xlabel('% lower status populate rate [LSTAT]')
plt.ylabel('Price [MEDV]')
plt.legend(loc='upper right')
plt.show()
