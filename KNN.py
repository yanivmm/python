

#import

import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import math

#read data
path = r'C:\Users\97250\Desktop\studied\R ,python\ניתוח מידע\חומר קורס ניתוח מידע\14-K-Nearest-Neighbors\KNN_Project_Data'
data = pd.read_csv(path)
data = pd.DataFrame(data)


#explore
data.head()
data.info()

sns.pairplot(data = data.drop('Target Class',axis=1),hue = "Target Class")


# scaling data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(data.drop('TARGET CLASS',axis = 1))
scalesFeatures = scaler.transform(data.drop('TARGET CLASS',axis = 1))

# data without label
X = pd.DataFrame(scalesFeatures,columns = data.columns[:-1])
X.head()

#       Train Test Split


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, data['TARGET CLASS'], test_size=0.3, random_state=101)


# KNN model
from sklearn.neighbors import KNeighborsClassifier
# 1 neighbour
knn = KNeighborsClassifier(n_neighbors=1).fit(X_train,y_train)

prediction = knn.predict(X_test)

# evaluation
from sklearn.metrics import classification_report,confusion_matrix

print(confusion_matrix(y_test ,prediction ))
print(classification_report(y_test,prediction))


# plot error in wide range of k neighbours

error = []
for k in range (1,40):
    knn = KNeighborsClassifier(n_neighbors=k).fit(X_train,y_train)
    prediction = knn.predict(X_test)
    error.append(np.mean(y_test != prediction))

print(error)

plt.figure(figsize=(12,8))

plt.plot(range(1,40), error ,marker = 'o',markersize = 12)
plt.xlabel('k value')
plt.ylabel('error')
plt.title('error by k- NN')

# algo with the best neighbour(10)
knn = KNeighborsClassifier(n_neighbors=10).fit(X_train,y_train)
prediction = knn.predict(X_test)
print(classification_report(prediction,y_test))
