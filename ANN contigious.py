
"""
Created on Sun Apr 19 17:52:01 2020

@author: Yaniv

subject:  ANN Contigious Data

"""


# import
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')



# contigious data path
contigious_data_path = r'C:\Users\97250\Desktop\studied\R ,python\ניתוח מידע\11-Linear-Regression\USA_Housing.csv'

data = pd.read_csv(contigious_data_path)


#prepaing data
#The foloowing steps are:

   # 1. explore data
   # 2. devide data to X and Y
   # 3. scaling
   # 4. converting to values (necessary to ANN algo.)
   # 5. train/test splitting


#sum of NA's
data.isnull().sum()
#no NA's

# a little search of data
data.head()
data.iloc[0]
data.columns
data.select_dtypes(['object']).columns

# X without address or the class label
   
X = data.drop(['Address','Price'],axis=1)
y = data['Price']

from sklearn.preprocessing import MinMaxScaler

cols = X.columns
X = MinMaxScaler().fit_transform(X)
X = pd.DataFrame(X,columns = cols)

X = X.values
y = y.values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

#The following steps are:

   # 1. import TensorFlow
   # 2. import additional modules
   # 3. create model


#       creating thr model


#import TensorFlow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout
from tensorflow.keras.callbacks import EarlyStopping



model = Sequential()

model.add(Dense(5,activation = 'relu'))

model.add(Dense(2,activation = 'relu'))

#model.add(Dense(3,activation = 'relu'))

model.add(Dense(1))


model.compile(optimizer='adam',loss='mse')
early = EarlyStopping(monitor='val_loss',mode='min',verbose =1,patience=25)
model.fit(X_train,y_train,epochs = 100,validation_data = (X_test,y_test),callbacks =[early])


#       visualize the model

#prepare
loss = model.history.history['loss']
val_loss = model.history.history['val_loss']
error = pd.DataFrame(loss,val_loss).reset_index()
error.columns = ['loss','val_loss']

#plot grath
error.plot(figsize=(12,12),lw=5,fontsize=24)
plt.legend(loc='upper left',prop={'size':20})

#prediction and evaluation
pred = model.predict(X_test)
y_test = y_test.reshape(1500,1)


#evaluation

from sklearn.metrics import mean_absolute_error,mean_squared_error

#model.evaluate(X_train,y_train)
MAE =round(mean_absolute_error(pred,y_test))
print('The RMSE is: ' , round(np.sqrt(mean_squared_error(pred,y_test))))
print('The mean absolute error is: ' , round(mean_absolute_error(pred,y_test)))

if np.mean(y_test)>(0.5*MAE):
    print("algorithm sucks")

"""
pred = np.float64(pred).round()
pred=pred.reshape(6484,1)
"""


#Dropout model

model = Sequential()

model.add(Dense(5,activation = 'relu'))
model.add(Dropout(0.5))

model.add(Dense(2,activation = 'relu'))
model.add(Dropout(0.5))

#model.add(Dense(3,activation = 'relu'))
#model.add(Dropout(0.5))

model.add(Dense(1))


model.compile(optimizer='adam',loss='mse')
early = EarlyStopping(monitor='val_loss',mode='min',verbose =1,patience=25)
model.fit(X_train,y_train,epochs = 100,validation_data = (X_test,y_test),callbacks =[early])

loss = model.history.history['loss']
val_loss = model.history.history['val_loss']
errorDropout = pd.DataFrame(loss,val_loss).reset_index()
errorDropout.columns = ['loss','val_loss']


#plot grath
errorDropout.plot(figsize=(12,12),lw=5,fontsize=24)
plt.legend(loc='upper left',prop={'size':20})

#prediction
pred = model.predict(X_test)
y_test = y_test.reshape(1500,1)


#evaluation

#model.evaluate(X_train,y_train)
MAE =round(mean_absolute_error(pred,y_test))
print('The RMSE is: ' , round(np.sqrt(mean_squared_error(pred,y_test))))
print('The mean absolute error is: ' , round(mean_absolute_error(pred,y_test)))

if np.mean(y_test)>(0.5*MAE):
    print("algorithm sucks")

#stable amount of nurons model

model = Sequential()

model.add(Dense(3,activation = 'relu'))
model.add(Dropout(0.5))

model.add(Dense(3,activation = 'relu'))
model.add(Dropout(0.5))

model.add(Dense(3,activation = 'relu'))
model.add(Dropout(0.5))

model.add(Dense(1))


model.compile(optimizer='adam',loss='mse')
early = EarlyStopping(monitor='val_loss',mode='min',verbose =1,patience=25)
model.fit(X_train,y_train,epochs = 100,validation_data = (X_test,y_test),callbacks =[early])

loss = model.history.history['loss']
val_loss = model.history.history['val_loss']
errorStableNuerons = pd.DataFrame(loss,val_loss).reset_index()
errorStableNuerons.columns = ['loss','val_loss']


#plot grath
errorStableNuerons.plot(figsize=(12,12),lw=5,fontsize=24)
plt.legend(loc='upper left',prop={'size':20})

#prediction
pred = model.predict(X_test)
y_test = y_test.reshape(1500,1)

#evaluation

#model.evaluate(X_train,y_train)
MAE =round(mean_absolute_error(pred,y_test))
print('The RMSE is: ' , round(np.sqrt(mean_squared_error(pred,y_test))))
print('The mean absolute error is: ' , round(mean_absolute_error(pred,y_test)))

if np.mean(y_test)>(0.5*MAE):
    print("algorithm sucks")




# activation function - htan model

model = Sequential()

model.add(Dense(5,activation = 'tanh'))
model.add(Dropout(0.5))

model.add(Dense(3,activation = 'tanh'))
model.add(Dropout(0.5))

#model.add(Dense(3,activation = 'tanh'))
#model.add(Dropout(0.5))

model.add(Dense(1))


model.compile(optimizer='adam',loss='mse')
early = EarlyStopping(monitor='val_loss',mode='min',verbose =1,patience=25)
model.fit(X_train,y_train,epochs = 100,validation_data = (X_test,y_test),callbacks =[early])

loss = model.history.history['loss']
val_loss = model.history.history['val_loss']
errorHtan = pd.DataFrame(loss,val_loss).reset_index()
errorHtan.columns = ['loss','val_loss']


#plot grath
errorDropout.plot(figsize=(12,12),lw=5,fontsize=24)
plt.legend(loc='upper left',prop={'size':20})

#prediction
pred = model.predict(X_test)
y_test = y_test.reshape(1500,1)

#evaluation

#model.evaluate(X_train,y_train)
MAE =round(mean_absolute_error(pred,y_test))

print('The mean absolute error is: ' ,MAE)
if np.mean(y_test)>(0.5*MAE):
    print("algorithm sucks")



###         plots all method evaluations graphs




# creating a list of all models

models    = [error, errorDropout, errorStableNuerons, errorHtan]
modelsStr = 'error error-Dropout error-Stable-Nuerons error-Htan'.split()


# for each model plot loss and val_loss on a diiferent subplot graph

plt.figure(figsize=(16,12))
for i, model in enumerate(models):
    plt.subplot(2,2,i+1)
    model['loss'].plot(lw=2,color = 'r',fontsize=16)
    plt.title(modelsStr[i],fontsize=30,color='gold')


#plot all errors loss in one graph

plt.figure(figsize=(12,12))
for i,model in enumerate(models):
    model['loss'].plot(lw = 5,figsize=(16,12), fontsize=18,label= (modelsStr[i]+' loss'))
    plt.legend(loc='left',prop={'size':20})
    plt.title("All loss from all methods\n",fontsize=40)


#scatter plots of loss and validation loss per each method
    
plt.figure(figsize=(16,12))
for i, model in enumerate(models):
    plt.subplot(2,2,i+1)
    sns.scatterplot(x='loss',y='val_loss',data=model)
    plt.title((modelsStr[i]),fontsize=30,color='gold')
    plt.xlabel('loss',fontsize=22)
    plt.ylabel('val_loss',fontsize=22)
    

