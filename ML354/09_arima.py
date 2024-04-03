import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller

#generating the sample data

np.random.seed(0)
dates=pd.date_range(start='2024-01-01',end='2024-12-31')
data=np.random.randn(len(dates))
# print(len(data))
data=np.cumsum(data)
df=pd.DataFrame(data,index=dates,columns=['Value'])


train_size=int(len(df)*0.8)
train,test=df[:train_size],df[train_size:]
def check_stationarity(timeseries):
    result=adfuller(timeseries)
    print('ADF Statistice: ',result[0])
    print('p-value',result[1])
    print('Critical Value: ')
    for key, value in result[4].items():
        print('\t%s: %.3f'%(key,value))
check_stationarity(train['Value'])

train_diff=train.diff().dropna()
check_stationarity(train_diff['Value'])
X_train=np.arange(len(train)).reshape(-1,1)
Y_train=train['Value']
regressor=LinearRegression()
regressor.fit(X_train,Y_train)
trend=regressor.predict(X_train)
model=ARIMA(train_diff, order=(5,1,0))
fitted_model=model.fit()
predictions_diff=fitted_model.forecast(steps=len(test))[0]
predictions_diff=pd.Series(predictions_diff, index=test.index)
predictions=predictions_diff + trend[-1]

plt.figure(figsize=(12,66))
plt.plot(train.index, train['Value'], label='Training data')
plt.plot(test.index, test['Value'], label='Testing data')
plt.plot(predictions.index,predictions,label='Prediction')
plt.title('ARIMA model with Linear Regression')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.show()