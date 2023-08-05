import pandas as pd
import numpy as np

data = {"A": [1, 2], "B": [3, 4], "C": [5, 6]}

data_pd = pd.DataFrame(data)

data1 = {"A": [1, 2, np.nan], "B": [3, 4, np.nan], "C": [5, np.nan, 6]}

data_pd_1 = pd.DataFrame(data1)

data_pd_1_1 = data_pd_1.dropna()

data_pd_1_2 = data_pd_1.dropna(axis= 1)

data_pd_1_3 = data_pd_1.dropna(thresh= 2)

data_pd_1_4 = data_pd_1.fillna(value= data_pd_1_3["A"].mean())

print(data_pd)
print(data_pd_1)
print(data_pd_1_1)
print(data_pd_1_2)
print(data_pd_1_3)
print(data_pd_1_4)
print(data_pd_1.describe())