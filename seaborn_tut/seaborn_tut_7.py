import pandas as pd
import seaborn as sns
import matplotlib.pyplot as mplpp

with open("seaborn_tut\\tips.csv") as data:
    data_pd = pd.read_csv(data)

#print(data_pd)

#1
sns.set_style('darkgrid')
sns.countplot(x='sex',data= data_pd)
mplpp.show()

#2
sns.set_style('whitegrid')
sns.countplot(x='sex',data= data_pd)
mplpp.show()

#3
sns.set_style('ticks')
sns.countplot(x='sex',data= data_pd)
mplpp.show()

#4
sns.set_style('ticks')
sns.countplot(x='sex',data= data_pd)
sns.despine()
mplpp.show()

#5
mplpp.figure(figsize= (12, 2))
sns.countplot(x='sex',data= data_pd)
mplpp.show()

#6
sns.set_context('poster', font_scale= 3)
sns.countplot(x='sex',data= data_pd)
mplpp.show()