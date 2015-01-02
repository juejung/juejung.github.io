#!/usr/bin/env python

# Here we want to call our two Python functions that are saved in myfunctions.py
# We can import these functions as follows:

import time                     # Imports system time module to time your script
from pylab import *             # Imports numpy, scipy, and matplotlib etc.
import csv                      # Imports .csv file reader
tic = time.clock()              # Start timer
# -----------------------------------------------------------------------------

close('all')  # close all open figures
# --------------------------------------------------------
# A. Read-data and making graphs
# --------------------------------------------------------

# Read in small data from .csv file
# Filepath
filepath = '../'
# In windows you can also specify the absolute path to your data file
# filepath = 'C:/Dropbox/Towson/Teaching/3_ComputationalEconomics/Lectures/Lecture4/'


# ------------- Load data --------------------
data =[]  # Define empty list for data reading
for row in csv.reader(open(filepath+"Lecture_4_Excel_a.csv"), delimiter=','):
    data.append(row)    # read data row by row

# Let's have a look at it, it's a nested list
data

# Split data into header and values
header      = data[0]        # first row contains headers of data
print header
groupNv     = []
groupv      = arange(1,6,1)  # make a vector from 1,2,...,5
freqv       = zeros((5,1),float)
for i in range(1,6):
    print i
    freqv[i-1]  = data[i][1]
    groupNv.append(data[i][0])
    
xv = copy(freqv/sum(freqv)) # calculate relative frequencies

# -------------      
# [1] Bar chart
# -------------
fig1 = figure()
bar(groupv,freqv, align='center')
# Annotate with text
xticks(groupv, groupNv)
for i, val in enumerate(freqv):
    text(i+1, val/2, str(val), va='center', ha='center', color='white')
ylabel('%')
title('Relative frequency table')
show()   
savefig('./Graphs/fig1.pdf') 

# -------------
# [2] Pie chart
# -------------
fig2 = figure()
pie(xv, labels=groupNv, shadow=True)
# Annotate with text
title('Relative frequency table')
show()   

# -------------
# [3] Histogram
# -------------
data =[]
for row in csv.reader(open(filepath+"Lecture_4_Excel_b.csv"), delimiter=','):
    data.append(row)    # read data row by row
#print data
header = data[0]
   
height = zeros((len(data)-1,1),float)   
for i in range(1,len(height)+1):
    #print i
    height[i-1]  = data[i][0]
#print height    

# Initialize
N = len(height) # number of obs.
B = 8           # number of bins in histogram

fig3 = figure()
prob, bins, patches = hist(height, bins=B, align='mid' )
# Annotate with text
for i, p in enumerate(prob):
    percent = int(float(p)/N*100)
    # only annotate non-zero values
    if percent:
        text(bins[i], p, str(percent)+'%', rotation=45, va='bottom', ha='center')
xlabel('Height groups')
ylabel('Number of obs')
title('Histogram of Height')
xlim(min(height),max(height))
show()

# -------------
# [4] Boxplot
# -------------
fig4 = figure()
boxplot(height)
# Annotate with text
title('Boxplot of Height')
show()

# -----------------------------------------------------------
# B. Summary statistics
# -----------------------------------------------------------
# ------------------------------------------
# [1] Measures of central tendency
# ------------------------------------------
N = len(height)   # Number of observations (sample size)
print " -----------------------------------------"  
# Mean - Median - Mode
print "Mean(height)= " + str(mean(height))
print "Median(height)= " + str(median(height))
print "Mode(height)= " + str(st.mode(height)) # Mode (value with highest frequency)
# Summary stats
print "Summary stats: " + str(st.describe(height))
print " -----------------------------------------"  

# ------------------------------------------
# [2] Measures of dispersion
# ------------------------------------------
print "Range= " + str(max(height)-min(height))   # returns smallest a largest element

print "Population variance = " + str(sum((height-mean(height))**2)/N)    # population variance
print "Sample variance     = " + str(sum((height-mean(height))**2)/(N-1))       # sample variance
print "Pop.   standard dev = " + str(sqrt(sum((height-mean(height))**2)/N))
print "Sample standard dev = " + str(sqrt(sum((height-mean(height))**2)/(N-1)))
#or simply
print "Pop. standard dev = " + str(std(height))
print " -----------------------------------------"  

# ------------------------------------------
# [3] Measures of relative standing
# ------------------------------------------
print "1 quartile (25th percentile) = " + str(st.scoreatpercentile(height, 25))
print "2 quartile (50th percentile) = " + str(st.scoreatpercentile(height, 50))
print "3 quartile (75th percentile) = " + str(st.scoreatpercentile(height, 75))
# Inter quartile rante: Q3-Q1 or P_75-P_25
print "IQR = (P75-P25) = " + str(st.scoreatpercentile(height, 75)-st.scoreatpercentile(height, 25))
print " -----------------------------------------" 
    
# -----------------------------------------------
# [4] Measures of linear relationship
# -----------------------------------------------
data =[]
for row in csv.reader(open(filepath+"Lecture_4_Excel_b.csv"), delimiter=','):
    data.append(row)    # read data row by row
#print data
header = data[0]
   
height  = zeros((len(data)-1,1),float)   
age     = zeros((len(data)-1,1),float)   
for i in range(1,len(height)+1):
    #print i
    height[i-1] = data[i][0] 
    age[i-1]    = data[i][3] 

# --------------------------------
# [4.1] Covariance
# --------------------------------
n = len(age)
x = age
y = height

print "Population covariance= " + str(sum((x-mean(x))*(y-mean(y)))/n)           # Population covariance
print "Sample covariance= " + str(sum((x-mean(x))*(y-mean(y)))/(n-1))       # sample covariance

# --------------------------------
# [4.2] Correlation coefficient
# --------------------------------
print "Correlation coefficient= " + str((sum((x-mean(x))*(y-mean(y)))/n)/(std(x)*std(y)))
print " -----------------------------------------"  

# --------------------------------
# [4.3] Regression line
# --------------------------------

# -------------------------
# Example 1: Simple example
# -------------------------
x = arange(1,9,1)
y = array([6,1,9,5,17,12,14,15])

# Simply use polyfit(x,y,1) , however this only works for one independent
# variable
p = polyfit(x,y,1)
print "p = " + str(p)

# -------------
# Scatterplot 
# ------------- 
fig4 = figure()
title('Linear regression with polyfit()')
plot(x,y, 'o', label = 'data')
plot(x,polyval(p,x),'-', label = 'Linear regression')
legend(loc='best') 
show()


# A more general method uses ols from myOLS.py
import myOLS
mymodel = myOLS.ols(y,x,'y',['x1'])
mymodel.b               # return estimated coefficients
mymodel.p               # return coefficient p-values
mymodel.summary()       # print results

# Prediction: size of 8.5 will produce a math score of ...
betas =mymodel.b
print "Prediction of y for x=8.5 is: " + str(sum(betas * array([1,8.5])))


# -------------------------
# Example 2: More real data
# -------------------------
# OLS with categorical (dummy variables)

data =[]
for row in csv.reader(open(filepath+"Lecture_4_Excel_b.csv"), delimiter=','):
    data.append(row)    # read data row by row
#print data
header = data[0]
   
y  = zeros((len(data)-1,1),float)   
x  = zeros((len(data)-1,7),float)
   
for i in range(1,len(height)+1):
    #print i
    y[i-1,0]            = data[i][2] # AverageMathSAT
    
    x[i-1,0]    = data[i][0] # height
    x[i-1,1]    = data[i][3] # age
    x[i-1,2]    = data[i][4] # d_female
    if data[i][6] == 'Hisp':  x[i-1,3] = 1 # d_hispanic
    if data[i][6] == 'Mex':  x[i-1,4] = 1 # d_mexican
    if data[i][6] == 'Oth': x[i-1,5] = 1 # d_other
    if data[i][6] == 'Wht': x[i-1,6] = 1 # d_white

print shape(x)
print shape(y)

mymodel = myOLS.ols(y[:,0],x[:,0:7],'y',['height','age','d_female','d_hisp','d_mex','d_other','d_white'])
mymodel.b               # return estimated coefficients
mymodel.p               # return coefficient p-values
mymodel.summary()       # print results

## Prediction: size of 8.5 will produce a math score of ...
betas = mymodel.b
print "Prediction: " +str(sum(betas * array([1,2.5,22,1,0,0,1,0])))

# -----------------------------------------------------------------------------
toc = time.clock()              # Stop timer
print "Time passed: " + str(toc - tic)

