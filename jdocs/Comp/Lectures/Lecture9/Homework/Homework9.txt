# -*- coding: utf-8 -*-
"""
# =====================================================================
#
# Scriptfile Homework 9
# -------------------------
# Computational Economics
# (c) Juergen Jung, 2012
#
# =====================================================================

"""
import math
from pylab import *
import scipy.optimize as optimize
from mpl_toolkits.mplot3d import Axes3D

close('all')  # close all open figure

# -----------------------------------------------------------------
# Multivariate optimization
# -----------------------------------------------------------------

# Here we want to optimize the following functions: f3, f4

# -------------------------------------------------
# Exercise 3
# -------------------------------------------------
def f_profit(x):
    f = (4 * (x[0]**0.33 + x[1]**0.67) - 0.75*x[0] - 1.84*x[1])
    return(f)

def f_profit_neg(x):
    f = - f_profit(x)
    return(f)
    
## Plot function f3
fig2 = figure()
ax = gca(projection='3d')
X = arange(0, 8.0, .25)
Y = arange(0, 8.0, .25)
X, Y = meshgrid(X, Y)

Z = zeros((len(X),len(Y)),float)
for i in range(len(X)):
    for j in range(len(Y)):
        Z[i][j] = f_profit([X[i][j],Y[i][j]])
        # print "i=" +str(i) + ", j= " + str(j) + ", Z=" + str(Z[i][j])
        
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.jet,
        linewidth=0, antialiased=False)
show()

## -----------------------------------------------------
## Maximize
## -----------------------------------------------------

## f3
for x0 in arange(0.0, 5.0, 1.0):
    for y0 in arange(0.0, 5.0, 1.0):
        print "optimize.fmin: f3 " +str([x0,y0]) + ' --> ' + str(optimize.fmin(f_profit_neg, array([x0,y0])))        
        print " ----------------------------------------- "

   


