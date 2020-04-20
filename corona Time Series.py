# -*- coding: utf-8 -*-
"""

Created on Mon Apr 20 17:12:30 2020

@author: Yaniv Maimon

version : 1.2

"""


# import 
import matplotlib.pyplot as plt
import pandas as pd

# import EXCEL file all sheets

path = r'C:\Users\97250\Desktop\studied\R ,python\corona\coronaWorldWide.xlsx'
x = pd.read_excel(path, sheet_name=None)


#changing columns names to unified form

for i in x:
    if x[i].columns[0]=='Country,Other' :
        x[i].columns = ['Country', 'TotalCases', 'NewCases', 'TotalDeaths', 'NewDeaths','TotalRecovered', 'ActiveCases', 'Serious,Critical', 'Tot Cases/1M pop','Deaths/1M pop', 'Reported1st case', 'ratio']
    

#check
for i in x:
    print(x[i].columns[0])


###      creating Time Series TotalDEaths table 


#initialize
data = pd.DataFrame(x['2020-04-20']['Country'])

#fill
for i in x:
    current_data = x[i][['Country','TotalDeaths']]
    data = data.merge(current_data, on='Country')

#set country as index    
data.set_index('Country',inplace=True)


#changing columns names to dates
l = [i for i in x]
data.columns = l    

#sorting -   failure
top_10_countries = data.sort_values('2020-04-20',axis=1).iloc[:10]


selected_countries = data.transpose()[['USA', 'Israel', 'Sweden', 'UK',
                                       'France', 'Italy', 'Spain']]


# plot graphs of countries deaths throuth time
selected_countries.plot(lw = 5,figsize=(12,8))
plt.legend(loc='upper left',prop={'size':20})

