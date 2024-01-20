import numpy as np
import pandas as pd
from io import StringIO
df=pd.read_csv('02_Panda.csv')#reading a csv file using pandas
print(df.head())
#What if in csv file in place of ',' we use slash or any other char (/) then how to open that file as data frame
df1=pd.read_csv('03_Panda.csv',sep='/')
print(df1.head())
print(df1[df['C1']>5])

data=('a,b,c,d\n'
      '1,2,3,4\n'
      '5,6,7,8\n'
      '9,10,11,12')
print(data)

# to convert a string like string stored in data variable into dataframe
df2=pd.read_csv(StringIO(data),dtype=object)
print(df2)
print(type(df2['a'][1]))
df2=pd.read_csv(StringIO(data),dtype=int)
print(df2)
df2=pd.read_csv(StringIO(data),dtype=float)
print(df2)
df2=pd.read_csv(StringIO(data),dtype={'b':int,'c':int,'a':str,'d':float})
print(df2)
print(df2.dtypes)
#Specifying index
data1=('index,a,b,c\n'
      '1,2,3,4\n'
      '5,6,7,8\n'
      '9,10,11,12')
df3=pd.read_csv(StringIO(data1),dtype=object)
print(df3.head())
df3=pd.read_csv(StringIO(data1),dtype=object,index_col=0)
print(df3.head())
df3=pd.read_csv(StringIO(data1),dtype=object,index_col=False)
print(df3.head())


