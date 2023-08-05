import pandas as pd

data = ['a', 'b', 'c']

data1 = [1, 2, 3]

data2 = {'a': 1, 'b': 2, 'c': 3}

data3 = pd.Series([1,2,3],["Ujwal", "Udai", "ME"])

data_pd = pd.Series(data= data)
print(data_pd)

data_pd_1 = pd.Series(data= data1)
print(data_pd_1)

data_pd_12 = pd.Series(data= data, index= data1)
print(data_pd_12)

data_pd_2 = pd.Series(data2)
print(data_pd_2)

print(data3)
print(data3["Ujwal"])