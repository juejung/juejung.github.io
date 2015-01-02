# -*- coding: utf-8 -*-
"""
# =====================================================================
#
# Scriptfile Lecture 8
# -------------------------
# Computational Economics
# (c) Juergen Jung, 2012
#
# =====================================================================

"""
import math
from pylab import *
from scipy.optimize import fsolve
from mpl_toolkits.mplot3d import Axes3D

# -------------------------------------------
# Root finding
# -------------------------------------------

close('all')  # close all open figure

# Define am example function for which we calculate the root, i.e. find x so that f(x) = 0
def func(x):
    s = log(x) - exp(-x)  # function: f(x)
    return s

def func1(x):
    s = log(x) - exp(-x)  # function: f(x)
    sp= 1.0/x + exp(-x)      # derivative of function: f'(x)
    return array([s,sp])    

# Plot the function
xmin = 1
xmax = 6
x  = arange(xmin, xmax, (xmax - xmin)/200.0)
fx = zeros(len(x),float) # define column vector
for i in range(len(x)):
    fx[i] = func(x[i])
    
#print "fx=" +str(fx)

fig1 = figure()
plot(x, fx)
plot(x, zeros(len(x)))
show()



# 2 Newton-Raphson
print " -------------- Newton Raphson ------------"
def newtonraphson(ftn, x0, tol = 1e-9, maxiter = 100):
    # Newton_Raphson algorithm for solving ftn(x)[1] == 0
    # we assume that ftn is a function of a single variable that returns
    # the function value and the first derivative as a vector of length 2
    #
    # x0 is the initial guess at the root
    # the algorithm terminates when the function value is within distance
    # tol of 0, or the number of iterations exceeds max.iter
    # initialise
    
    x = x0
    fx = ftn(x)
    iter =  0
    # continue iterating until stopping conditions are met
    while ((abs(fx[0]) > tol) and (iter < maxiter)):
        x = x - fx[0]/fx[1]
        fx = ftn(x)
        iter =  iter + 1
        print "At iteration " + str(iter) + " value of x is: " +str(x)

    # output depends on success of algorithm
    if (abs(fx[0]) > tol):
        print "Algorithm failed to converge"
        return(NULL)
    else:
        print "fx = " + str(fx[0])
        print "Algorithm converged"
        return(x)



# Calculate the root of the function calling 'newtonraphson'
newtonraphson(func1, 2)


# 3 Secant method
print " -------------- Secant  ------------"
def secant(ftn, x0, x1, tol = 1e-9, maxiter = 100):
    # Secant algorithm for solving ftn(x) == 0
    # we assume that ftn is a function of a single variable that returns
    # the function value
    #
    # x0 and x1 are the initial guesses around the root
    # the algorithm terminates when the function value is within distance
    # tol of 0, or the number of iterations exceeds max.iter
    #
    # initialize
    fx0 = ftn(x0)
    fx1 = ftn(x1)
    iter =  0
    #
    # continue iterating until stopping conditions are met
    while ((abs(fx1) > tol) and (iter < maxiter)):
        x  = x1 - fx1 * (x1-x0)/(fx1 - fx0) 
        fx0 = ftn(x1)
        fx1 = ftn(x)
        x0  = x1
        x1  = x
        iter =  iter + 1
        print "At iteration "+str(iter)+" value of x is: "+str(x)
# output depends on success of algorithm
    if (abs(fx1) > tol):
        print "Algorithm failed to converge"
        return(NULL)
    else:
       print "Algorithm converged"
       return(x)

# Calculate the root of the function calling 'secant'
secant(func, 1,2)

# 4 Bisection
print " -------------- Biscetion ------------"
def bisection(ftn, xl, xr, tol = 1e-9):
    # applies the bisection algorithm to find x such that ftn(x) == 0
    # we assume that ftn is a function of a single variable
    #
    # x.l and x.r must bracket the fixed point, that is
    # x.l < x.r and ftn(x.l) * ftn(x.r) < 0
    #
    # the algorithm iteratively refines x.l and x.r and terminates when
    # x.r - x.l <= tol
   
    # check inputs
    if (xl >= xr):
        print "error: xl >= xr"
        return(NULL)
        
    fl = ftn(xl)
    fr = ftn(xr)
        
    if (fl == 0):
        return(x.l)
    elif (fr == 0):
        return(x.r)
    elif (fl * fr > 0):
        print "error: ftn(xl) * ftn(xr) > 0"
        return(NULL)
    
    # successively refine x.l and x.r
    n = 0
    while ((xr - xl) > tol):
        xm = (xl + xr)/2.0
        fm = ftn(xm)
        if (fm == 0):
            return(fm)
        elif (fl * fm < 0):
            xr = xm
            fr = fm
        else:
            xl = xm
            fl = fm
        n = n + 1
        print "at iteration "+str(n)+ " the root lies between "+str(xl)+ " and "+str(xr)
    
    # return (approximate) root
    return ((xl + xr)/2.0)

# Calculate the root of the function calling 'secant'
bisection(func, 1,2)

# 5 Use built in 'fsolve'
print " "
print " -------------- Fsolve ------------"
result = fsolve(func, 2) # starting from x = 2
print result