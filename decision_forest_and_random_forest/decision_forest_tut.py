import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import classification_report,confusion_matrix

from sklearn.ensemble import RandomForestClassifier

from IPython.display import Image

from sklearn.externals import StringIO

from sklearn.tree import export_graphviz

import pydot

data = pd.read_csv('decision_forest_and_random_forest\kyphosis.csv')

sns.pairplot(data, hue='Kyphosis')
plt.show()

# X removes the row Kyphosis
X = data.drop('Kyphosis', axis=1)

# Y contains the row Kyphosis
y = data['Kyphosis']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

# Decision Tree Classifier object
dtree = DecisionTreeClassifier()

# Fit the training data
dtree.fit(X_train,y_train)

# Predicts based on test data
predictions = dtree.predict(X_test)

# Final Report
print(classification_report(y_test,predictions))

# Matrix prediction
print(confusion_matrix(y_test,predictions))

# Tree display

# Titles
features = list(data.columns[1:])

# Creating object
dot_data = StringIO()

# Graph creation
export_graphviz(dtree, out_file=dot_data,feature_names=features,filled=True,rounded=True)

# Get the value
graph = pydot.graph_from_dot_data(dot_data.getvalue())

# Image creation
Image(graph[0].create_png())

plt.show()

# Random Forest

# Call random foest object
rfc = RandomForestClassifier(n_estimators=100)

# Fit the data
rfc.fit(X_train, y_train)

# Make Prediction
rfc_pred = rfc.predict(X_test)

# Print out Random Forest report
print(classification_report(y_test,rfc_pred))

# Make confusion matrix
print(confusion_matrix(y_test,rfc_pred))