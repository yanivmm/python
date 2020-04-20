
"""

Created on Wed Apr  1 01:26:37 2020

@author: yanivM

"""



#from pandas_datareader import data,wb
import datetime
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
#from plotly.offline import download_plotlyjs,iplot,plot,init_notebook_mode
#import cufflinks as cf
#cf.go_offline

sns.set_context('poster', 0.5)
#reading data and seperating to 6 banks
df = pd.read_pickle(r'C:\Users\97250\Downloads\all_banks')
BAC = df['BAC']
C = df['C']
GS = df['GS']
JPM = df['JPM']
MS = df['MS']
WFC = df['WFC']

#initialize 'bank tickle'
l = [i[0] for i in df.columns]
tickle=[]
for i in l:
    if i not in tickle:
        tickle.append(i)        

#concatination
bank_stock = pd.concat((BAC,C,GS,JPM,MS,WFC),axis=1,keys = tickle)
#set level index
bank_stock.columns.names = ['bank','stock info']

#close price data Frame
close = df.xs(key = 'Close',axis = 1 , level = 1)


#differences for each bank through all period
close.iloc[-1]-close.iloc[0]

#heatmapS for every year of the 'close'
for i in range(6):
    plt.figure(figsize=(12,12))
    sns.heatmap(vmin = 0,vmax = 500,data = close.iloc[365*i:365*(i+1)],cmap = 'Greens')

#showing the major difference between these banks
plt.figure(figsize=(12,12))
sns.heatmap(close[['C','GS']].iloc[:1000],cmap = 'Greens',vmin = 0,vmax = 500)

#numerical diffs between GolmanSacks and City Group
CGS = close[['C','GS']]
CGS[close['C']>close['GS']]
sum(CGS['GS']-CGS['C'])

#print yearly max values for  banks
for i in range(0,1500,365):
    print(CGS.iloc[i:i+365].max())

sns.lmplot(x='Date',y = 'C',data = CGS.reset_index() ,height = 8)
sns.lmplot(x='Date',y = 'GS',data = CGS.reset_index() ,height = 8)


returns = pd.DataFrame()

for i in close.columns:
        returns[i] = close[i].pct_change()
        
g=  sns.PairGrid(returns)
g.map_diag(sns.distplot)
        


close.min()


returns = close.pct_change()

sns.pairplot(returns[1:])

returns2015 = returns.loc[returns.index.year==2015]


sns.distplot(returns2015['MS'],bins=100,color = 'green')


close['BAC'].loc[close.index.year==2008]


close.plot(figsize=(8,8))

close.corr()

