import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

with open("linear_regression_tut\\USA_Housing.csv") as data:
    data_pd = pd.read_csv(data)

#print(data_pd)
#print(data_pd.describe())

#total price
#sns.pairplot(data_pd)
#plt.show()

#price distribution
#sns.distplot(data_pd['Price'])
#plt.show()

#Heatmap
sns.heatmap(data_pd.corr())
plt.show()