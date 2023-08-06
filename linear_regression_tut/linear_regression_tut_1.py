import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

from sklearn import metrics

with open("linear_regression_tut\\USA_Housing.csv") as data:
    data_pd = pd.read_csv(data)

# print(data_pd)
# print(data_pd.describe())

# total price
# sns.pairplot(data_pd)
# plt.show()

# price distribution
# sns.distplot(data_pd['Price'])
# plt.show()

# Heatmap
# sns.heatmap(data_pd.corr())
# plt.show()

# trainig split
# print(data_pd.columns)
# Index(['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
#       'Avg. Area Number of Bedrooms', 'Area Population', 'Price', 'Address'],
X = data_pd[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
             'Avg. Area Number of Bedrooms', 'Area Population']]
y = data_pd['Price']
# testsize- percentage of dataset allocated for trainig set, randomstate- random split occuring in data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)

#Creating and Training the Model
lm = LinearRegression()

#Fitting the model
lm.fit(X_train,y_train)

# print the intercept
#print(lm.intercept_)

# print the coefficient
#print(lm.coef_)

#Answer should be the trained data
coeff_df = pd.DataFrame(lm.coef_,X.columns,columns=['Coefficient'])
#print(coeff_df)

#Predictions from our Mode
predictions = lm.predict(X_test)

#testing for accuracy by scattering
#plt.scatter(y_test,predictions)
#plt.show()

#Distribution graph to find accuracy
#sns.distplot((y_test-predictions),bins=50)
#plt.show()

#Error prediction
print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))