import numpy as np
import pandas as pd
import html5lib
from io import StringIO
import json
Data='{"employee":"Tanishk","email":"tanishk@gmail.com","job-profile":{"title1":"Team Lead","title2":"Problem-Solver"}}'
data=pd.read_json(Data)
print(data)
df=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data',header=None)
print(df.head)
df.to_json('wine.csv',orient='records')
print(df)
print(data.to_json(orient="records"))
#Web Scrapping: Reading Table from a webpage
url='https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/'
dfs=pd.read_html(url)#return a list of tables
print(dfs[0])
print(type(dfs))
url1='https://en.wikipedia.org/wiki/Mobile_country_code'
dfs1=pd.read_html(url1)
print(dfs1[1])
