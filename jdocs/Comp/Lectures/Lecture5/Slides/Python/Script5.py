#!/usr/bin/env python

# Here we want to call our two Python functions that are saved in myfunctions.py
# We can import these functions as follows:

import time                     # Imports system time module to time your script
from pylab import *             # Imports numpy, scipy, and matplotlib etc.
from scipy import stats as st
import myFunctions as mfunc

tic = time.clock()              # Start timer
# -----------------------------------------------------------------------------
close('all')  # close all open figures


# --------------------------------------------
# 1 Use simple user defined functions
# --------------------------------------------

# Now we call these functions with function arguments
print mfunc.hw1(2.6,4.0)

mfunc.hw2(2.5,5.6)

# --------------------------------------------
# 2 Advanced Graphing using loops and functions
# --------------------------------------------


# ----------------------------------------
## 2.1 Graphing functions with two input arguments z = f(x,y)
# ----------------------------------------
from mpl_toolkits.mplot3d import Axes3D

X = arange(1, 11, 1)
Y = arange(1, 11, 1)

X, Y = meshgrid(X, Y)
xn, yn = X.shape

f = 	zeros((xn,xn),float)   # Define matrix size nxn with zero entries
for i in range(xn):
    for j in range(yn):
        #print i,j
        f[i,j] = sin(X[i,j]*Y[i,j])
        
fig1=figure()
ax = Axes3D(fig1)
ax.plot_wireframe(X, Y, f, rstride=2, cstride=2)
show()


# ----------------------------------------
## 2.2 Same thing but different function.
# ----------------------------------------
def g(x, y):
    res=(1 + y * 2) ** (-x / y) * (1 + y * 1) ** (x / y)
    return res

X = linspace(0.01, 1, 20)
X, Y = meshgrid(X, X)
xn, yn = X.shape

f = 	zeros((xn,xn),float)   # Define matrix size nxn with zero entries
for i in range(xn):
    for j in range(yn):
        f[i,j] = g(X[i,j], Y[i,j])

fig2=figure()
ax = Axes3D(fig2)
ax.plot_wireframe(X, Y, f, rstride=2, cstride=2)
show()

# ----------------------------------------
# 3  In class example
# ----------------------------------------
def jstdev(xv):
    n       = len(xv)
    xmean   = sum(xv)/n
    stdev   = math.sqrt(sum((xv-xmean)**2)/n)
    return stdev

# Let's check whether we got it right?
xv = array([2.,4.,3.5,95.,12.4,-1.])
print('Population standard deviation: ', jstdev(xv))
print('Population standard deviation: ', std(xv))
    
    
# -----------------------------------------------------------------------------
toc = time.clock()              # Stop timer
print "Time passed: " + str(toc - tic)



    
