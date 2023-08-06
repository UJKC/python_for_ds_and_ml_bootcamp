import seaborn as sns
import matplotlib.pyplot as mplpp
import pandas as pd
import numpy as np

with open("seaborn_tut\\flights.csv") as data1:
    data_pd_1 = pd.read_csv(data1)

#print(data_pd_1)

data_pd_1_1 = data_pd_1.pivot_table(index= 'month', columns= 'year', values= 'passengers')
print(data_pd_1_1)

#1
sns.heatmap(data_pd_1_1)
mplpp.show()

#2
sns.heatmap(data_pd_1_1, cmap= 'magma', linecolor= 'white', linewidth= 1) #coolwarm
mplpp.show()

#3
sns.clustermap(data_pd_1_1) #coolwarm
mplpp.show()

#4
sns.clustermap(data_pd_1_1, standard_scale= 1) #coolwarm
mplpp.show()