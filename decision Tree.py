# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 23:40:26 2020

@author: yanivM

subject:

"""



import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

loans = pd.read_csv(r'C:\Users\97250\Desktop\studied\R ,python\חומר קורס ניתוח מידע\15-Decision-Trees-and-Random-Forests\loan_data.csv')

# some data info:
loans.describe()
loans.head()

# quick review of the columns

loans.select_dtypes(['object']).columns
loans['purpose'].value_counts()
loans.iloc[2]

#countplots of the class

sns.countplot(data=loans,x='not.fully.paid')
sns.countplot(data=loans,x='credit.policy')

# dual histogram of the of FICO to each class

plt.figure(figsize=(10,6))
loans[loans['not.fully.paid']==1]['fico'].hist(alpha=0.5,color='blue',bins=30,label='fully.paid')
loans[loans['not.fully.paid']==0]['fico'].hist(alpha=0.5,color='red',bins=30,label='not.fully.paid')
plt.legend()
plt.xlabel('FICO')

# A try to see an impact of the loan's purpose and to return it

plt.figure(figsize=(11,7))
sns.countplot(x='purpose',hue='not.fully.paid',data=loans,palette='Set1')

# A try to see an impact of the loan's interest and to return it

plt.figure(figsize=(11,7))
sns.lmplot(y='int.rate',x='fico',data=loans,hue='credit.policy',
           col='not.fully.paid',palette='Set1')

loans.info()

final_data = pd.get_dummies(loans,columns=['purpose'],drop_first=True)


#       train/test splitting
from sklearn.model_selection import train_test_split

X = final_data.drop('not.fully.paid',axis=1)
y = final_data['not.fully.paid']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=101)


#       desicion tree model and evaluation

from sklearn.tree import DecisionTreeClassifier

dtree = DecisionTreeClassifier()

dtree.fit(X_train,y_train)

predictions = dtree.predict(X_test)


from sklearn.metrics import classification_report,confusion_matrix

print(classification_report(y_test,predictions))
print(confusion_matrix(y_test,predictions))

#           random forest model and evaluation

from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier(n_estimators=600)

rfc.fit(X_train,y_train)

predictions = rfc.predict(X_test)


print(classification_report(y_test,predictions))
print(confusion_matrix(y_test,predictions))
