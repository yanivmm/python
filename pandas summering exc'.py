"""
Created on Sat Mar 28 17:28:10 2020

@author: yanivM
"""

import numpy as np
import pandas as pd

sal = pd.read_csv(r'C:\Users\97250\Desktop\קורסים מתקדמים\ניתוח מידע פייתון\Salaries.csv')

#mean and max 
sal['BasePay'].mean()
sal['OvertimePay'].max()

#jobTitle and Salary of specific man
sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['JobTitle']
sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['TotalPayBenefits']

#all information about top and lowest earner man
sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].max()]
sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].min()]

sal.groupby('Year').mean()['BasePay']

#unique count of JobTitle
sal['JobTitle'].nunique()
 
#5most common jobTitles
sal['JobTitle'].value_counts().head(5)

#how many 'chief' reffrernces in job title
print(len(list(filter(lambda x:'CHIEF' in x or 'Chief' in x , sal['JobTitle']))))

#initializing series of job titles's length
lenTitleSeries = [len(list(sal['JobTitle'][i])) for i in range(len(sal))]

#correlation
np.corrcoef(lenTitleSeries,sal['TotalPayBenefits'])