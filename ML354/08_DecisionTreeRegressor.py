from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error,mean_absolute_percentage_error
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
tree=DecisionTreeRegressor(max_depth=3)
tree.fit(X,y)
sort_idx=X.flatten().argsort()
# plt.scatter(X,y,color='lightgray')
# plt.plot(X[sort_idx],tree.predict(X)[sort_idx],color='blue',lw=2,linestyle='--')
# plt.xlabel('% lower status of Population [LSTAT]')
# plt.ylabel("Price [MEDV]")
# plt.show()

from sklearn.model_selection import train_test_split
X=df.iloc[:,:-1].values
y=df['MEDV'].values
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)

from sklearn.ensemble import RandomForestRegressor
rfr=RandomForestRegressor(n_estimators=1000,criterion='squared_error',random_state=1,n_jobs=-1)
rfr.fit(X_train,y_train)
y_pred=rfr.predict(X_train)
y_pred_test=rfr.predict(X_test)
print(r2_score(y_test,y_pred_test))
print(r2_score(y_train,y_pred))
print("MSE test: ",mean_squared_error(y_test,y_pred_test))
print("MSE train: ",mean_squared_error(y_train,y_pred))
print("MAE test: ",mean_absolute_error(y_test,y_pred_test))
print("MAE train: ",mean_absolute_error(y_train,y_pred))
print("MAPE test: ",mean_absolute_percentage_error(y_test,y_pred_test))
print("MAPE train: ",mean_absolute_percentage_error(y_train,y_pred))

plt.scatter(y_pred,y_pred-y_train,c='steelblue',edgecolors='white',marker='o',alpha=0.9,label='Training points')
plt.scatter(y_pred_test,y_pred_test-y_test,c='limegreen',edgecolors='white',marker='s',alpha=0.9,label='Testing points')
plt.xlabel('Predicted Values')
plt.ylabel('Residual')
plt.legend(loc='upper left')
plt.hlines(y=0,xmin=10,xmax=50,lw=2,color='red')
plt.xlim([-10,50])
plt.show()
