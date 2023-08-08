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

#8
sns.boxplot(x='Pclass',y='Age',data=data_pd,palette='winter')
plt.show()


def impute_age(cols):
    Age = cols[0]
    Pclass = cols[1]
    
    if pd.isnull(Age):

        if Pclass == 1:
            return 37

        elif Pclass == 2:
            return 29

        else:
            return 24

    else:
        return Age

data_pd['Age'] = data_pd[['Age','Pclass']].apply(impute_age,axis=1)

#9
sns.heatmap(data_pd.isnull(),yticklabels=False,cbar=False)
plt.show()

data_pd.drop('Cabin',axis=1,inplace=True)

data_pd.dropna(inplace=True)

sex = pd.get_dummies(data_pd['Sex'],drop_first=True)
embark = pd.get_dummies(data_pd['Embarked'],drop_first=True)

train = pd.concat([data_pd,sex,embark],axis=1)

train.drop(['Sex', 'Embarked', 'Name', 'Ticket', 'PassengerId'],axis=1,inplace=True)