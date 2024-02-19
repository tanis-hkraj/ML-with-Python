import pandas as pd
data=pd.read_csv("housing_data.csv")
print(data)
# Creating own DataFrame
d={"Cars":["Ferari","Alto","BMW","Thar"],"Speed":[200,150,250,160]}
print(d)
d=pd.DataFrame(d)
print(d)
print(d.shape)

# Data Analytics Process
'''
1. Bussiness Problem: Process of Analytics begins with questions or business problems for stakeholders.
'''