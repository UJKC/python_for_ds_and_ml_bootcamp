import pandas as pd
import numpy as np

data = pd.DataFrame(np.random.randn(5,4), ['A', 'B', 'C', 'D', 'E'], ["W", "X", "Y", "Z"])

data1 = data["W"]

data2 = data[["W", "Z"]]

data3 = data
data3['L'] = data3["W"] + data3["Z"]

data4 = data3.drop("L", axis= 1)

data5 = data3
data5 = data5.drop("L", axis= 1, inplace= True)

data6 = data4.drop("E")

data7 = data.loc["A"]

data8 = data.iloc[3]

data9 = data.loc["B", "Y"]

data10 = data.loc[["A", "B"], ["W", "Z"]]

print(data)
print(data1)
print(data2)
print(data3)
print(data4)
print(data5)
print(data6)
print(data.shape)
print(data7)
print(data8)
print(data9)
print(data10)