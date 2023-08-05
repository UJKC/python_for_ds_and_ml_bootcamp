import pandas as pd
import numpy as np

data = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})

data1 = data.isnull()

data2 = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

data_pd_2 = pd.DataFrame(data2)

data_pd_2_1 = data_pd_2.pivot_table(values="D", index=["A", "B"], columns=["C"])

def times(x):
    return x ** 2

print(data)
print(data["col1"].unique())
print(data["col1"].nunique())
print(data["col2"].value_counts())
print(data["col1"].apply(times))
print(data["col2"].apply(lambda x: x * 2))
print(data.columns)
print(data.index)
print(data.sort_values("col2"))
print(data1)
print(data_pd_2)
print(data_pd_2_1)