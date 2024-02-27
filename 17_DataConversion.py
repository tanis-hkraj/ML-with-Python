import pandas as pd
df=pd.read_csv("Data.csv")
print(df)
print("-------------------------------------------------------")
# using get_dummies function to convert the categorical datatype to numerical and storing the dataframe in new variable df1...
df1=pd.get_dummies(df['Purchased'])

#using pd.concat to concatanate the dataframes
# df and df1 and storing the concatenated dataframe in df
df=pd.concat([df,df1],axis=1)

#removing the column 'purchased' from df as it is of no use now..
df.drop('Purchased',axis=1,inplace=True)
print(df)
print("-------------------------------------------------------")

#Importing LabelEncoder from Sklearn
# Library from pre-processing module
from sklearn.preprocessing import LabelEncoder
df2=pd.read_csv("Data.csv")
# Creating a instance of label encoder
le=LabelEncoder()

# Using .fit_transform function to fit label
# encoder and return encoded label
label=le.fit_transform(df2['Purchased'])

print(label)
print("-------------------------------------------------------")
df2['Purchased']=label
print(df2)
print("-------------------------------------------------------")
