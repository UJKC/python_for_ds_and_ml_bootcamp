import seaborn as sns
import matplotlib.pyplot as mplpp
import pandas as pd
import numpy as np

with open("seaborn_tut\\tips.csv") as data:
    data_pd = pd.read_csv(data)

#print(data_pd)

#1
sns.barplot(x= 'sex', y= 'total_bill', data= data_pd)
mplpp.show()

#2
sns.barplot(x='sex',y='total_bill',data=data_pd,estimator=np.std)
mplpp.show()

#3
sns.countplot(x= 'sex', data= data_pd)
mplpp.show()

#4
sns.boxplot(x= 'day', y= 'total_bill', data= data_pd) #outlier
mplpp.show()

#5
sns.boxplot(x= 'day', y= 'total_bill', data= data_pd, hue= 'smoker') #outlier
mplpp.show()

#6
sns.violinplot(x= 'day', y= 'total_bill', data= data_pd)
mplpp.show()

#7
sns.stripplot(x= 'day', y= 'total_bill', data= data_pd)
mplpp.show()

#8
sns.stripplot(x= 'day', y= 'total_bill', data= data_pd, jitter= True)
mplpp.show()

#9
sns.stripplot(x= 'day', y= 'total_bill', data= data_pd, jitter= True, hue= 'sex')
mplpp.show()

#10
sns.swarmplot(x= 'day', y= 'total_bill', data= data_pd)
mplpp.show()