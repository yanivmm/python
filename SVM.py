

###   the following data is about flowers
 #   each data consists of several features about the flower
 #    let's figure out how to predict


#import
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset('iris')

sns.pairplot(iris,hue = 'species',palette='Dark2')

# seems like SETOSA is the most differnt flower,
# and no misclassification expected at the prediction

sns.jointplot(x='sepal_width',y='sepal_length',data = iris[iris['species']=='setosa'],kind='kde')

# devide data

X = iris.drop('species',axis=1)
y = iris['species']

#train-test splitting

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

# SVC model to predict future classification

from sklearn.svm import SVC
model = SVC().fit(X_train,y_train)
pred = model.predict(X_test)

# evaluation 

from sklearn.metrics import confusion_matrix,classification_report

print(confusion_matrix(pred,y_test))
print(classification_report(pred,y_test))


# grid Search

# multi-check during run in order to find best parameters

from sklearn.model_selection import GridSearchCV

# 4 parameters check

paramGrid = {'C':[0.1,1,10],'gamma':[1,0.1,0.01]}

# grid search takes the pred' algorithm and the checking range

gridSearch = GridSearchCV(SVC(),param_grid=paramGrid,verbose=3) # verbose =data displayed

# prediction 
gridSearch.fit(X_train,y_train)
pred = gridSearch.predict(X_test)

# grid evaluation

print(confusion_matrix(pred,y_test))
print(classification_report(pred,y_test))

gridSearch.best_parameters_