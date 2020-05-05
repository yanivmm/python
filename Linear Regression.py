
#import
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import seaborn as sns

#         read file

path = r'C:\Users\97250\Desktop\studied\R ,python\ניתוח מידע\Ecommerce Customers.csv'
cust = pd.read_csv(path)


#         explore data

# A try to search the most affecting column on the Yearly Amount Spent and other
sns.jointplot(x='Time on Website',y='Yearly Amount Spent',data=cust)

sns.jointplot(x='Time on App',y='Yearly Amount Spent',data=cust)

sns.lmplot(x='Length of Membership',y='Yearly Amount Spent',data = cust)

#pairplot
sns.pairplot(cust)


###       Training and Testing Data

from sklearn.model_selection import train_test_split

X=cust[['Avg. Session Length', 'Time on App','Time on Website', 'Length of Membership']]

y=cust['Yearly Amount Spent']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)


#       model

from sklearn.linear_model import LinearRegression

lm =LinearRegression().fit(X_train,y_train)

lm.coef_

prediction = lm.predict(X_test)


# visual plot of the differences between y_test and prediction
sns.scatterplot(x = y_test,y = prediction, hue =(abs(prediction-y_test)))

# numerical evaluation

MAE = np.mean(abs(prediction-y_test))
MSE = np.mean((prediction-y_test)**2)
RMSE= np.sqrt(np.mean((prediction-y_test)**2))
print('\n')
print('MAE: '+str(MAE),'MSE: '+str(MSE),'RMSE: '+str(RMSE),sep = '\n')


# plot of the residuals of the y_test and prediction

residuals = (y_test-prediction)
plt.figure(figsize=(12,8))
sns.distplot(residuals,bins = 60,color='red')
# it's a normal distribution therefore it's a fine model.!


#creating a dataframe of the coefficients and its values

coefficient = lm.coef_
col  = ['Avg. Session Length', 'Time on App','Time on Website', 'Length of Membership']
coefficient_data = pd.DataFrame(coefficient,col,columns = ['coefficient'])
coefficient_data = coefficient_data.sort_values('coefficient',ascending=False)

# visual affect
coefficient_data.plot(kind ='bar',figsize=(12,8),color='gold',fontsize = 18)
plt.title('\n Coefficients and its values\n',fontsize=34)

# only two most affecting coefficients
print('\n')
for i in range(2):
    print(coefficient_data.index[i])
