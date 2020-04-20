



"""
Created on Tue Mar 31 01:11:10 2020

@author: yanivM
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#from plotly.offline import download_plotlyjs,iplot,plot
sns.set_context('poster',0.6)

#reading data
df = pd.read_csv(r'C:\Users\97250\911.csv')
df = pd.DataFrame(df)

#additional commands
df.info()
df['zip'].value_counts().head(5)
df['twp'].value_counts().head(5)
df['title'].nunique()

#initialize 'reason' column
df['reason'] = df['title'].apply(lambda x: x.split(':')[0])

df['reason'].value_counts()

#reason dist.
plt.figure(figsize= (12,12))
sns.countplot(x='reason',data=df)

#converting timeStamp to date time
df['timeStamp'] = df['timeStamp'].apply(lambda x : pd.to_datetime(x))

#extracting date details as additional columns
df['hour'] = df['timeStamp'].apply(lambda x : x.hour)
df['month'] = df['timeStamp'].apply(lambda x : x.month)
df['day of month'] = df['timeStamp'].apply(lambda x : x.day)

#creating day of week from dayOfMonth
dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
df['day of week'] = df['timeStamp'].apply(lambda x:dmap[x.dayofweek])

#'reason' countplot for [day ,month]
plt.figure(figsize= (8,8))
sns.countplot(x = df['day of week'], hue = df['reason'])
plt.figure(figsize= (8,8))
sns.countplot(x = df['month'], hue = df['reason'])

#groupby 'month'
byMonth  = df.groupby('month').count()
plt.figure(figsize= (12,12))
plt.plot(byMonth['lat'])

#initializg date column
df['date'] = df['timeStamp'].apply(lambda x:x.date())

#groupby   'date'
byDate = df.groupby('date').count()
plt.figure(figsize= (12,12))
plt.plot(byDate['lat'],'b',lw=0.5)

#liniar modek
byMonth.reset_index(inplace = True)
sns.lmplot(x='month',y = 'twp',data = byMonth)


#aggregation of all calls by day of week and hour into a table -'x'
x = df.groupby(['hour','day of week']).count().unstack(0)['lat']
#heatmap and clustermap of 'x'
plt.figure(figsize=(14,14))
sns.heatmap(x, lw=1,linecolor= 'white',cmap = 'Greens')
sns.clustermap(x, lw=1,linecolor= 'white',cmap = 'Greens')


#same process for day of week and month
y = df.groupby(['month','day of week']).count().unstack(0)['lat']
plt.figure(figsize=(14,14))
sns.heatmap(x, lw=1,linecolor= 'white',cmap = 'Greens')
sns.clustermap(x,lw=1,linecolor= 'white',cmap = 'Greens') #failed beacuse NANs

#filling nans with mean
y[8].fillna(value = y[8].mean(),inplace = True)
y[12].fillna(value = y[12].mean(),inplace = True)
#run again
sns.clustermap(x,lw=1,linecolor= 'white',cmap = 'Greens')




