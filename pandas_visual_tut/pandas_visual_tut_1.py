import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as mplpp

with open("pandas_visual_tut\\df1.csv") as data1:
    data_pd_1 = pd.read_csv(data1, index_col= 0)

df1 = pd.read_csv("pandas_visual_tut\\df1.csv",index_col=0)

#print(data_pd_1)

with open("pandas_visual_tut\\df2.csv") as data2:
    data_pd_2 = pd.read_csv(data2)

#print(data_pd_2)

with open("pandas_visual_tut\\df3.csv") as data3:
    data_pd_3 = pd.read_csv(data3)

#print(data_pd_3)

#1
data_pd_1['A'].hist()
mplpp.show()

#2
data_pd_1['A'].plot.hist()
mplpp.show()

#3
data_pd_1['A'].plot(kind= 'hist')
mplpp.show()

#4
data_pd_2.plot.area()
mplpp.show()

#5
data_pd_2.plot.area(alpha= 0.4)
mplpp.show()

#6
data_pd_2.plot.bar()
mplpp.show()

#7
data_pd_2.plot.bar(stacked= True)
mplpp.show()

#8
#data_pd_2.plot.line(x=data_pd_2.index,y='B',figsize=(12,3),lw=1)
#mplpp.show()

#9
data_pd_2.plot.scatter(x= 'a', y= 'b')
mplpp.show()

#10
data_pd_2.plot.scatter(x= 'a', y= 'b', c= 'c')
mplpp.show()

#11
data_pd_2.plot.scatter(x= 'a', y= 'b', s= data_pd_2['c'] * 100)
mplpp.show()

#12
data_pd_2.plot.box()
mplpp.show()

#13
data_pd = pd.DataFrame(np.random.randn(1000, 2), columns= ["A", 'B']) #no of rows, no of columns
#print(data_pd)
data_pd.plot.hexbin(x= 'A', y= "B", gridsize= 10)
mplpp.show()

#14
data_pd_2.plot.kde()
mplpp.show()