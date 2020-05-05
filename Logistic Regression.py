
#       import
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import math


#read file
path = r'C:\Users\97250\Desktop\studied\R ,python\ניתוח מידע\חומר קורס ניתוח מידע\13-Logistic-Regression\advertising.csv'
ad_data = pd.read_csv(path)

#first explore
ad_data.head()

ad_data.info()

ad_data.describe()


#        Exploratory Data Analysis

#explore calls distribution
sns.distplot(ad_data['Age'],bins = 60)

# Serach affected columns on each other
sns.jointplot(x='Age',y='Area Income',data=ad_data)

sns.jointplot(x='Age',y='Daily Time Spent on Site',data=ad_data ,kind = 'kde',color='red')

sns.jointplot(x='Daily Time Spent on Site',y='Daily Internet Usage',data=ad_data, color='green')

#pair plot
sns.pairplot(data = ad_data,hue = 'Clicked on Ad',hue_order=[1,0])



#       train/test split

from sklearn.model_selection import train_test_split

ad_data.columns

# choosing the right columns
X = ad_data[['Daily Time Spent on Site', 'Age', 'Area Income']]
y = ad_data['Clicked on Ad']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)


#       model
from sklearn.linear_model import LogisticRegression

lg = LogisticRegression().fit(X_train,y_train)

pred = lg.predict(X_test)

# evaluation
from sklearn.metrics import classification_report
print(classification_report(pred , y_test))
