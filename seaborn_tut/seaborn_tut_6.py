import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as mplpp

with open("seaborn_tut\\tips.csv") as data:
    data_pd = pd.read_csv(data)

#1
sns.lmplot(x= 'total_bill', y= 'tip', data= data_pd)
mplpp.show()

#2
sns.lmplot(x= 'total_bill', y= 'tip', data= data_pd, hue= 'sex')
mplpp.show()

#3
sns.lmplot(x= 'total_bill', y= 'tip', data= data_pd, hue= 'sex', markers= ['o', 'v'])
mplpp.show()

#4
sns.lmplot(x= 'total_bill', y= 'tip', data= data_pd, col= 'sex')
mplpp.show()

#5
sns.lmplot(x= 'total_bill', y= 'tip', data= data_pd, col= 'sex', row= 'time')
mplpp.show()

#7
sns.lmplot(x= 'total_bill', y= 'tip', data= data_pd, col= 'day', hue= 'sex')
mplpp.show()

#8
sns.lmplot(x= 'total_bill', y= 'tip', data= data_pd, col= 'day', hue= 'sex', aspect= 0.6)
mplpp.show()