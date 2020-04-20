

"""

Created on Mon Mar 30 12:58:52 2020

@author: yanivmM

"""

#import
import seaborn as sns
import matplotlib.pyplot as plt

#general setttings
sns.set_context('poster',1)
sns.set_style('whitegrid')

#load data to 'ti'
ti = sns.load_dataset('titanic')

# =============================================================================
# 
# 'data = __'  noticement!!
# every function needs data 
# every function with tow data arguments for example: (x,y) needs "data =..."
#     therefore ,no need to specify x = ti['age'] , only  x='age'
# distplot doesn't have 'data' therefore ti['age'] is essential
# countplot supports both 
# 
# =============================================================================

# all sort of plots
plt.figure(figsize = (12,12))  #set-size command to heatmap\plot   must run with the graphic-plot command
sns.jointplot(x='fare',y='age',data= ti)
sns.distplot(ti['fare'], kde =False,color = 'pink')
sns.boxplot(x='class',y='age',data=ti)
sns.swarmplot(x='class',y='age',data=ti)
sns.violinplot(x='class',y='age',data=ti)
sns.countplot(x='sex',data=ti)  #or : sns.countplot(x=ti['sex'])


#heatmap
ticorr = ti.corr() #initialize correlation matrix
plt.figure(figsize = (20,20))  #set-size command to heatmap\plot   #must run simultaneously with the plotting command
sns.heatmap(ticorr,lw=1 ,linecolor = 'white',cmap = 'Blues', annot = True)
sns.clustermap(ticorr,figsize = (12,12) ,annot = True)

# facet Grid 
# several graphs together
# size intialize inside
g = sns.FacetGrid(ti,col = 'sex',size = 10,aspect=0.5)
g.map(sns.distplot,'age')




"""
general note about size :

plt.figure(figsize = (a,b)) works in the folowing functions :
heatmap, distplot,swarmplot,boxplot,countplot,violinplot.

doesn't work in these: 
clustermap (has its own param. - 'figsize') , FacetGrid (its own param. - 'size')

"""
