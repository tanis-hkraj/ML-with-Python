import pandas as pd
#pandas is a data analysing tool in python
import numpy as np
# Data-Frame: a 2D labled data structure with columns of potentially different types
# Creating a dataFrame using pandas
df=pd.DataFrame(np.arange(0,30).reshape(5,6),index=["Row1","Row2","Row3","Row4","Row5"],columns=["C1","C2","C3","C4","C5","C6"])
print(df)
# Accessing the elements
# 1. .loc  2. .iloc 3. Direct column access
print(df.loc["Row3"])
print(type(df.loc["Row3"]))
print(df[["C2","C5"]])

print(df.iloc[0:2,0:3])# works same as in numpy
# converting DataFrames into arrays
print(df.iloc[:,1:].values)
print(df.iloc[:,1:].values.shape)
#checking data frames whether it has a null value
print(df.isnull().sum())
# Counting number of occurences of an element in the column
print(df["C3"].value_counts())
# Finding unique elements in a column
print(df["C4"].unique())
#Data Frame info
print(df.info())
print(df.describe())