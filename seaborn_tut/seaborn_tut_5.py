import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as mplpp

with open("seaborn_tut\\tips.csv") as data:
    data_pd = pd.read_csv(data)

#print(data_pd)

with open("seaborn_tut\\iris.csv") as data1:
    data_pd_1 = pd.read_csv(data1)

#print(data_pd_1)

#1
sns.pairplot(data_pd_1)
mplpp.show()

#2
g = sns.PairGrid(data_pd_1)
g.map_diag(sns.histplot)
g.map_upper(sns.scatterplot)
g.map_lower(sns.kdeplot)
mplpp.show()

#3
g = sns.FacetGrid(data_pd, col="time",  row="smoker")
g.map(sns.distplot, 'total_bill')
mplpp.show()

#4
g = sns.FacetGrid(data= data_pd, row= 'smoker', col= 'time')
g.map(sns.scatterplot, 'total_bill', 'tip')
mplpp.show()