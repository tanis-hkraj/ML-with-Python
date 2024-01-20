import numpy as np
import pandas as pd
from io import StringIO
import json
Data='{"employee":"Tanishk","email":"tanishk@gmail.com","job-profile":{"title1":"Team Lead","title2":"Problem-Solver"}}'
data=pd.read_json(Data)
print(data)
df=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data',header=None)
print(df.head)
df.to_json('wine.csv',orient='index')
print(data.to_json())