import seaborn as sns
import matplotlib.pyplot as mplpp
#print(sns.get_dataset_names())
#['anagrams', 'anscombe', 'attention', 'brain_networks', 'car_crashes', 'diamonds', 'dots', 'dowjones', 'exercise', 'flights', 'fmri', 'geyser', 'glue', 'healthexp', 'iris', 'mpg', 'penguins', 'planets', 'seaice', 'taxis', 'tips', 'titanic']

#plot = sns.load_dataset('tips')
#plot.head()
#print(plot)

import pandas as pd

with open("seaborn_tut\\tips.csv") as data:
    data_pd = pd.read_csv(data)

#print(data_pd)

#1
sns.distplot(data_pd['total_bill'])
mplpp.show()

#2
sns.distplot(data_pd['total_bill'], kde= False)
mplpp.show()

#3
sns.jointplot(x= 'total_bill', y= 'tip', data= data_pd)
mplpp.show()

#4
sns.jointplot(x= 'total_bill', y= 'tip', data= data_pd, kind= 'hex')
mplpp.show()

#5
sns.jointplot(x= 'total_bill', y= 'tip', data= data_pd, kind= 'reg')
mplpp.show()

#6
sns.jointplot(x= 'total_bill', y= 'tip', data= data_pd, kind= 'kde')
mplpp.show()

#7
sns.pairplot(data_pd)
mplpp.show()

#8
sns.pairplot(data_pd, hue= 'sex')
mplpp.show()

#8
sns.rugplot(data_pd['total_bill'])
mplpp.show()