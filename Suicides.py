"""
Created on Sun Jul 19 01:07:00 2020

@author: YanivMaimon

"""

#pre

path = r'C:\Users\97250\Desktop\studied\R ,python\Datasets Kaggle\suicide_workFlow.csv'
import pandas as pd
data = pd.read_csv(path)
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')


# agg count function
    
def agg(colum,d='numOfSuicides'):  ### d='r' will show relative data.
    
    """
    Aggregation function.
    
    Input:
        Colum - string or list of strings.
        The column data to aggregate with.
        d- string.
        If 'r' than relative data is shown.
        
    Return:
        DataFrame's aggregated form by given column(s).
    """
    
    if d == 'r':#you can choose wether to show a relative numOfSuicides
        d='suicides/100k'
        
    if type(colum) != list: # if one column has been given
        return data.groupby(colum).sum()[d].sort_values(ascending=False)
    else:
        return data.groupby(colum).sum()[[d]].sort_values(ascending=False,by =d)#.unstack(0)
    
    

dic = {'l':(24,18),'m':(16,12),'s':(12,8)}    
    
# plot function
def show(data,s = 'm',st='',save=False):
    """
    Plots Bar chart.
    input:
        data - df.
        st   - string-to print in title.
        s    - Output size.
    """
    
    scale = dic[s]
    kind = 'line' if len(data.shape)==2 else 'bar' #len(data.shape)==2 means: 2 dimentional data
    
    data.plot(kind = kind,lw = (scale[0]//4),figsize = scale,fontsize = scale[0]+4)
    plt.title("\n " + st +"\n",fontsize = 2*scale[0])
    plt.legend(loc='upper right',prop={'size':1.2*scale[0]})
    if save:
        plt.savefig(r'C:\Users\97250\Desktop\studied\R ,python\Datasets Kaggle\Outputs data\Suicide\'' + st + '.png')
        
# heatmap function
def heat(data,s='m',st=''):
    
    scale = dic[s]
    
    sns.set(font_scale=1.8)
    plt.figure(figsize=scale)
    sns.heatmap(data = data ,lw=1 ,linecolor = 'white',cmap = 'Reds', annot = True)
    plt.title('Suicides based on '+ st +': \n',fontsize = 2*scale[0])
    #plt.savefig(r'C:\Users\97250\Desktop\studied\R ,python\Datasets Kaggle\Outputs data\Suicide\'' + st + '.png')  

# worst years?
    
heat(agg(['age','country'])[:10])




###################################



#       Deadly years



col = 'numOfSuicides'#'suicides/100k'
# agg. data
yearlyData = data.groupby('year').sum()[col]
# show
show(yearlyData,'m','year',True)


####################


#      Time line for each country through time


def topCountries(top=10):
    """
    This func return data for top countries throughout time.
    """
    #top 10 deadly countries
    countries = agg('country')[:top].index
    #grab aggregated data for these countries
    dataOfTop10 = agg(['year','country']).query("country in @countries")### interesting...
    #unstack data
    dataOfTop10 = dataOfTop10.unstack(1)
    #remove multiindexes
    dataOfTop10 = dataOfTop10.transpose().reset_index(level=0, drop=True).transpose()
    #sort by year
    dataOfTop10.sort_index(inplace=True)
    return dataOfTop10

#Show time lines
show(topCountries())


##############################################


# golden age suicides

#change age
data['age'] = data['age'].apply(lambda x : x.split()[0])
#grab olds data
oldData = data.query("age =='75+'")

dataOfTop10 = oldData.groupby('country').sum()['suicides/100k'].sort_values(ascending=False)[:10]
#show
show(dataOfTop10,'l','each country of the golden age',True)


############################

#top 10 countries by decades 


def decadeDecoder(year):
    """
    convert year to decade.
    """
    
    decade = int(str(year)[2])
    decoder = {
            8:'1980\'',
            9:'1990\'',
            0:'2000\'',
            1:'2010\''
            }
    
    return decoder[decade]

#convert
data['decade'] = data['year'].apply(decadeDecoder)

#show
show(agg('decade').sort_index(),'l','the suicide\'s rate for each decade',True)

##########################

#top 10 countries for each decade

for i in data['decade'].unique(): # run for each decade
    decadeData = data.query("decade == @i")
    dataOfTop10 = decadeData.groupby('country').sum()['suicides/100k'].sort_values(ascending=False)[:20]
    show(dataOfTop10,'s','The suicides rate for the years '+ i+' for top 10 countries',True)

#########################
    
#          devirative

#     visual    

#initialize    
devi = pd.DataFrame()

dataOfTop10 = topCountries()
# filll DF in deviratove:
for i in dataOfTop10.columns:
    devi[i] = dataOfTop10[i].pct_change()   
# show
show(devi,'m','The devirative suicides for each country through years')    
    
###########

#       mathmatical

polandYearly = devi.transpose().loc['Poland']
polandMax = devi.max().loc['Poland']
    
polandYearly
    
    


#########################


#           other calculations

# the highest varianced caountries of the deriative relative suicides nums.#woww
devi.var().sort_values(ascending=False)

# variance of age groups
data.groupby('age').var()['suicides/100k'].sort_values(ascending=False)[:10]

#       countries with highest AVG of suicides per each 'age group' 

 #top 10 deadly countries
countries = agg('country')[:10].index
#grab aggregated data for these countries
dataOfTop10 = data.query("country in @countries")
#agg. AVG
dataOfTop10 = dataOfTop10.groupby(['age','country']).mean()['suicides/100k']
# each 'group age'
dataOfTop10 = dataOfTop10.reset_index().sort_values(by = ['age','suicides/100k'],ascending=False)
dataOfTop10.set_index('age',inplace=True)

####################



#       top variant /average countries

var = data.groupby('country').var()['suicides/100k'].sort_values(ascending=False)[:10]
mean= data.groupby('country').mean()['suicides/100k'].sort_values(ascending=False)[:10]

# The countries that have high variance **and** high AVG.
# instersect
deadlyCountries = pd.Series(list(set(var.index) & set(mean.index)))

#######

#       top variant /average years

var = data.groupby('year').var()['suicides/100k'].sort_values(ascending=False)[:10]
mean= data.groupby('year').mean()['suicides/100k'].sort_values(ascending=False)[:10]

# The years with the highest AVG and VAR.
deadlyYears = pd.Series(list(set(var.index) & set(mean.index)))


#########################################################


############        final!!             #################


########################################################
