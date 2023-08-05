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


data11 = data10[data10 > 0]

data12 = data6[data6["W"] > 0]

data13 = data6[(data6["W"] > 0) & (data6["Y"] > 0)]

data14 = data6.reset_index()

data15 = ["U", "D", "A", "I"]

data16 = data6
data16["State"] = data15


# Index Levels
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

data17 = pd.DataFrame(np.random.randn(6, 2), hier_index, ["A", "B"])

data18 = data17.loc["G1"]

data19 = data17.loc["G1"].loc[1]

data20 = data17
data20.index.names = ["Groups", "Index"]

data21 = data20.xs(1, axis= 0, level= "Index")

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

print(data11)
print(data12)
print(data13)
print(data14)
print(data15)
print(data16)

print(data17)
print(data18)
print(data19)
print(data20)
print(data21)