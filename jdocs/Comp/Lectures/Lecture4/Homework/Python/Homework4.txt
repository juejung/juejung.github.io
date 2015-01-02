# Homework 4

import time                     # Imports system time module to time your script
from pylab import *             # Imports numpy, scipy, and matplotlib etc.
from scipy import stats as st
import csv                      # Imports .csv file reader
import myOLS
tic = time.clock()              # Start timer
close('all')  # close all open figures

# -----------------------------------------------------------------------------
# Exercise 1
# -----------------------------------------------------------------------------
filepath = '../'

data =[]  # Define empty list for data reading
for row in csv.reader(open(filepath+"BaltimoreData.csv"), delimiter=','):
    data.append(row)    # read data row by row

# Let's have a look at it, it's a nested list
data

header = data[0]

#y  = zeros((len(data)-1,1),float)  # Defined as matrix, has two dimensions 
yv = arange(0,(len(data)-1))*0.0   # Defined as vector, has only one dimension

# Careful with this. Do NOT use Populationv = yv to initialize!!  
# If you want to assign Populationv=yv use the copy command like:
# Populationv=yv.copy(), otherwise you
# link the two vectors and changing one, will change the other.
Populationv  =  arange(0,(len(data)-1))*0.0
MedIncomev   =  arange(0,(len(data)-1))*0.0
Unemployedv  =  arange(0,(len(data)-1))*0.0	
FamPovv      =  arange(0,(len(data)-1))*0.0	
BachDegreev  =  arange(0,(len(data)-1))*0.0
JuvArrestv   =  arange(0,(len(data)-1))*0.0	
Homicidesv   =  arange(0,(len(data)-1))*0.0
LifeExpv     =  arange(0,(len(data)-1))*0.0

for i in range(1,len(data)):
    #print i
    Populationv[i-1]   =  data[i][1] 
    MedIncomev[i-1]    =  data[i][2]  
    Unemployedv[i-1]   =  data[i][3] 	
    FamPovv[i-1]       =  data[i][4] 	
    BachDegreev[i-1]   =  data[i][5] 
    JuvArrestv[i-1]    =  data[i][6] 	
    Homicidesv[i-1]    =  data[i][7] 
    LifeExpv[i-1]      =  data[i][8] 

## -----------------------------------------------------------------------------
## Exercise 2
## -----------------------------------------------------------------------------
nameList = [Populationv, MedIncomev, Unemployedv, FamPovv, BachDegreev, JuvArrestv, Homicidesv, LifeExpv]
nameListStr = ['Population',' MedIncome', 'Unemployed', 'FamPov', 'BachDegree', 'JuvArrest', 'Homicides', 'LifeExp']
for i in range(len(nameList)):
    #print str(i)
    print "======================="
    print str(nameListStr[i])
    print "======================="
    print "Mean:      " + str(mean(nameList[i]))
    print "Median:    " + str(median(nameList[i]))
    print "Mode:      " + str(st.mode(nameList[i]))
    print "Stand.Dev: " + str(std(nameList[i]))

# -----------------------------------------------------------------------------
# Exercise 3
# -----------------------------------------------------------------------------   
fig1 = figure()
title("Percent of Bachelor's Degrees vs. Median Income")
plot(BachDegreev,MedIncomev,'o') 
xlabel('Percent Bachelors Degree') #label the axes for clarification
ylabel('Median Income')
show()
 
# -----------------------------------------------------------------------------
# Exercise 4
# -----------------------------------------------------------------------------    
yv = JuvArrestv
# Stack vectors together into matrix to be called by OLS
x = array([Populationv, MedIncomev,Unemployedv,BachDegreev,FamPovv]).transpose()

reg=myOLS.ols(yv,x,"Juvenile Arrest Rate",["Population","Median Income","Unemployment","Bachelor's Degrees","Families in Poverty"])
#reg.b
#reg.p
reg.summary()


# -----------------------------------------------------------------------------
# Exercise 5
# -----------------------------------------------------------------------------   
x1  = zeros((len(data)-1,6),float)

for i in range(0,len(Population)):
    #print i
    x1[i,0]    = MedIncomev[i] # 
    x1[i,1]    = Unemployedv[i] #
    x1[i,2]    = BachDegreev[i] #
    x1[i,3]    = FamPovv[i] #
    if Populationv[i] < 6500:  x1[i,4] = 1 # d_S
    if (Populationv[i] >= 6500 and Populationv[i]<=10000):  x1[i,5] = 1 # d_M

reg=myOLS.ols(yv,x1,"Juvenile Arrest Rate",["Median Income","Unemployment","Bachelor's Degrees","Families in Poverty","d_S","d_M"])
#reg.b
#reg.p
reg.summary()    