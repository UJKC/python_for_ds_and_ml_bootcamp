import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import cufflinks as cf

with open("logistic_regression_tut\\titanic_train.csv") as data:
    data_pd = pd.read_csv(data)

#print(data_pd)

#1
sns.heatmap(data_pd.isnull(),yticklabels=False,cbar=False,cmap='viridis')
plt.show()

#2
sns.countplot(x='Survived',data=data_pd)
plt.show()

#3
sns.countplot(x='Survived',data=data_pd, hue='Sex')
plt.show()

#4
sns.countplot(x='Survived',data=data_pd, hue='Pclass')
plt.show()

#5
data_pd['Age'].hist()
plt.show()

#6
sns.countplot(x='SibSp',data=data_pd)
plt.show()

#7
data_pd['Fare'].hist(color='green',bins=40,figsize=(8,4))
plt.show()

#cf.go_offline()
#data_pd['Fare'].iplot(kind='hist',bins=30,color='green')