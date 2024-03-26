from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt 
import pandas as pd

df=pd.read_csv('https://raw.githubusercontent.com/rasbt/'
              'python-machine-learning-book-2nd-edition'
              '/master/code/ch10/housing.data.txt',
              sep='\s+')

df.columns=['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS',
            'RAD','TAX','PTRATIO','B','LSTAT','MEDV']
print(df)
from sklearn.model_selection import train_test_split
X=df.iloc[:,:-1].values #except the last attribute/col/explanatory variable
Y=df['MEDV'].values #only one col/response variable
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2)
#Test size =20%
lr=LinearRegression() #creating the object of the model
lr.fit(X_train,Y_train) #training of the model based on 80% training
Y_train_pred=lr.predict(X_train) #predicting the trsining data
Y_test_pred=lr.predict(X_test) #prediction of testing data
from sklearn.metrics import mean_squared_error,r2_score
print('MSE train: %.3f, test: %.3f'%(mean_squared_error(Y_train,Y_train_pred),mean_squared_error(Y_test,Y_test_pred)))