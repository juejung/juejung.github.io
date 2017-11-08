# Homework 6
import time                     # Imports system time module to time your script
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats as st
import statsmodels.api as sm
from patsy import dmatrices

tic = time.clock()  # Start timer
plt.close('all')        # close all open figures

# -----------------------------------------------------------------------------
# Exercise 1
# -----------------------------------------------------------------------------
myData = pd.ExcelFile("BaltimoreData.xlsx")

# Check how many sheets we have inside the excel file
myData.sheet_names
[u'Sheet1', u'Sheet2', u'Sheet3']

# Pick one sheet and define it as your DataFrame by parsing a sheet
df = myData.parse("Sheet1")
# Drop rows with NaNs
df = df.dropna() 

# Delete white space from the end of variable names!! 
# But leaves white-space withing variable names in place!!
df = df.rename(columns=lambda x: x.strip())

df.describe()
print(df.head())

# -----------------------------------------------------------------------------
# Exercise 2
# -----------------------------------------------------------------------------
for x in df.columns:
    # Check whether the data type is a number or a string/word
    if (df[x].dtypes) == np.dtype('O'):
        # Data type is a string/word,don't attempt to calculate stats
        pass
    else:
        xv = df[x].values
        print("=======================")
        print('Variable {}:'.format(x))
        print("=======================")
        print('The mean of the variable is {}'.format(np.mean(xv)))
        print('The median of the variable is {}'.format(np.median(xv)))
        print('The standard deviation of the variable is {}'.format(np.std(xv)))
        print('The mode of the variable is {}'.format(st.mode(xv)))

# -----------------------------------------------------------------------------
# Exercise 3
# -----------------------------------------------------------------------------   
fig, ax = plt.subplots()
ax.set_title('Scatterpolt of Median Income and Bachelors Degree')
ax.scatter(df['Median Income'], df['Bachelors degree'])
ax.set_xlabel('Percent Bachelors Degree') #label the axes for clarification
ax.set_ylabel('Median Income')
plt.show()
 
# -----------------------------------------------------------------------------
# Exercise 4
# -----------------------------------------------------------------------------    
df = df.rename(columns={ \
    'Juvenile Arrest Rate*': 'Juvenile_Arrest_Rate', \
    'Homicide Incidence Rate**': 'Homicide_Rate', \
    'Median Income': 'Median_Income', \
    'Families in Poverty': 'Families_in_Poverty', \
    'Bachelors degree': 'Bachelors_degree'})



# Run OLS regression
# This line adds a constant number column to the X-matrix and extracts
# the relevant columns from the dataframe
y, X = dmatrices('Juvenile_Arrest_Rate ~ Population + Median_Income +  \
    Unemployed + Families_in_Poverty + Bachelors_degree', \
    data=df, return_type='dataframe')

res = sm.OLS(y, X).fit()
    
print(res.summary())
print(res.params)

# -----------------------------------------------------------------------------
# Exercise 5
# -----------------------------------------------------------------------------  
df['d_Small'] = 0  # dummy for small counties
df['d_Mid_Size'] = 0  # dummy for midsize counties
# don't need to make dummy for large counties, because you need to drop one 
# dummy coefficient anyways - this is then referred to as the BASE-CATEGORY
 
# This version works, but throws warnings in Pandas 13.0 and up
#df['d_Small'][df['Population'] < 6500] = 1
#df['d_Mid-Size'][(df['Population'] > 6500) & (df['Population'] < 10000)] = 1

# This is the new syntax!!
df.loc[(df['Population'] < 6500), 'd_Small'] = 1
df.loc[(df['Population'] > 6500) & (df['Population'] < 10000), 'd_Mid_Size'] = 1

# Run OLS regression
# This line adds a constant number column to the X-matrix and extracts
# the relevant columns from the dataframe
y, X = dmatrices('Juvenile_Arrest_Rate ~ Population + Median_Income +  \
    Unemployed + d_Small + d_Mid_Size', \
    data=df, return_type='dataframe')

res = sm.OLS(y, X).fit()

print(res.summary())
print(res.params)