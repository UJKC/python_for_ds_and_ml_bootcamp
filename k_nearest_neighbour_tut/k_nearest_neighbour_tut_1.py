import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

from sklearn.preprocessing import StandardScaler

from sklearn.model_selection import train_test_split

from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import classification_report,confusion_matrix

df = pd.read_csv("k_nearest_neighbour_tut\\Classified_Data",index_col=0)

#print(df)

#Instance creation
scaler = StandardScaler()

#Fit the data in machine learning
scaler.fit(df.drop('TARGET CLASS',axis=1))

#Transform the data
scaled_features = scaler.transform(df.drop('TARGET CLASS',axis=1))

#create a dataframe
df_feat = pd.DataFrame(scaled_features,columns=df.columns[:-1])

#train
X_train, X_test, y_train, y_test = train_test_split(df_feat, df['TARGET CLASS'],
                                                    test_size=0.30, random_state=101)

#instance
knn = KNeighborsClassifier(n_neighbors=1)

#Train
knn.fit(X_train,y_train)

#predict
pred = knn.predict(X_test)

#Answer
print(confusion_matrix(y_test,pred))
print(classification_report(y_test,pred))

#Check for other K
error_rate = []

# Will take some time
for i in range(1,40):
    
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train,y_train)
    pred_i = knn.predict(X_test)
    error_rate.append(np.mean(pred_i != y_test))

#Plot
plt.figure(figsize=(10,6))
plt.plot(range(1,40),error_rate,color='blue', linestyle='dashed', marker='o',
         markerfacecolor='red', markersize=10)
plt.title('Error Rate vs. K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')
plt.show()

# FIRST A QUICK COMPARISON TO OUR K=23
knn = KNeighborsClassifier(n_neighbors=37)

knn.fit(X_train,y_train)
pred = knn.predict(X_test)

print('WITH K=23')
print('\n')
print(confusion_matrix(y_test,pred))
print('\n')
print(classification_report(y_test,pred))