import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Calling dataset instance
from sklearn.datasets import load_breast_cancer

# Split the data
from sklearn.model_selection import train_test_split

# Get the SVC model
from sklearn.svm import SVC

# Report and matric import
from sklearn.metrics import classification_report,confusion_matrix

# Import grid search
from sklearn.model_selection import GridSearchCV

# Instantiate it
model = SVC()

# Creating instance
cancer = load_breast_cancer()

# From cancer data test the data of feature_names as dataframe
df_feat = pd.DataFrame(cancer['data'], columns=cancer['feature_names'])

# Split the data
X_train, X_test, y_train, y_test = train_test_split(df_feat, cancer['target'], test_size=0.30, random_state=101)

# Train the model
model.fit(X_train,y_train)

# Predict the results
predictions = model.predict(X_test)

# Print the report
print(classification_report(y_test,predictions))

# Print the matrix
print(confusion_matrix(y_test,predictions))

# Grid Values
param_grid = {'C': [0.1,1, 10, 100, 1000], 'gamma': [1,0.1,0.01,0.001,0.0001], 'kernel': ['rbf']}

# Instantiate grid cv
grid = GridSearchCV(SVC(),param_grid,refit=True,verbose=3)

# Fit grid modle
grid.fit(X_train,y_train)

# Best validation score
print(grid.best_params_)

# Best estimator
grid.best_estimator_

# Grid prediction
grid_predictions = grid.predict(X_test)

# Grid report
print(classification_report(y_test,grid_predictions))

# Grid matrix
print(confusion_matrix(y_test,grid_predictions))