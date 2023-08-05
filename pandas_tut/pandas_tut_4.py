import pandas as pd

data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}

data_pd = pd.DataFrame(data)

data_pd_1 = data_pd[data_pd["Company"] == "GOOG"]

data_pd_2 = data_pd.groupby("Company")

print(data_pd)
print(data_pd_1)
print(data_pd_2)
print(data_pd_2.describe())
print(data_pd_2.count())
print(data_pd_2.max())
print(data_pd_2.describe().transpose())