# -*- coding: utf-8 -*-
"""
# =====================================================================
#
# Scriptfile Lecture 9
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

# -------------------------------------------
# Optimization
# -------------------------------------------

close('all')  # close all open figure

# Define am example function for which we calculate the root, i.e. find x so that f(x) = 0
def f1(x):
    # gamma(2,3) density
    if (x < 0): 
        return array([0, 0, 0])
    if (x == 0): 
        return array([0, 0, NaN])
    y = exp(-2.0*x)
    return array([4.0 * x**2.0 * y, 8.0 * x*(1.0-x)*y, 8.0*(1.0 - 2.0 * x**2.0)*y])

def f1simple(x):
    # gamma(2,3) density
    if (x < 0): 
        return (0)
    if (x == 0): 
        return (NaN)
    y = exp(-2*x)
    return (4 * x**2 * y)
    
def f1simpleNeg(x):
    # gamma(2,3) density
    if (x < 0): 
        return (0)
    if (x == 0): 
        return (NaN)
    y = exp(-2*x)
    return (-(4 * x**2 * y))
    
# Plot the function
xmin = 0
xmax = 6
x  = arange(xmin, xmax, (xmax - xmin)/200.0)
fx = zeros(len(x),float) # define column vector
for i in range(len(x)):
    fx[i] = f1(x[i])[0]
    
#print "fx=" +str(fx)

fig1 = figure()
plot(x, fx)
plot(x, zeros(len(x)))
show()


# 1.1 Newton's method
def newton(f3, x0, tol = 1e-9, nmax = 100):
    # Newton's method for optimization, starting at x0
    # f3 is a function that given x returns the vector
    # (f(x), f'(x), f''(x)), for some f
    x = x0
    f3x = f3(x)
    n = 0
    while ((abs(f3x[1]) > tol) and (n < nmax)):
        x = x - f3x[1]/f3x[2]
        f3x = f3(x)
        n = n + 1
    if (n == nmax):
        print "newton failed to converge"
    else:
        return(x)

## 1.2 Golden section method
def gsection(ftn, xl, xr, xm, tol = 1e-9):
    # applies the golden-section algorithm to maximise ftn
    # we assume that ftn is a function of a single variable
    # and that x.l < x.m < x.r and ftn(x.l), ftn(x.r) <= ftn(x.m)
    #
    # the algorithm iteratively refines x.l, x.r, and x.m and terminates
    # when x.r - x.l <= tol, then returns x.m
    # golden ratio plus one
    gr1 = 1 + (1 + math.sqrt(5))/2
#   
    # successively refine x.l, x.r, and x.m
    fl = ftn(xl)
    fr = ftn(xr)
    fm = ftn(xm)
    while ((xr - xl) > tol):
        if ((xr - xm) > (xm - xl)):
            y = xm + (xr - xm)/gr1
            fy = ftn(y)
            if (fy >= fm):
                xl = xm
                fl = fm
                xm = y
                fm = fy
            else:
                xr = y
                fr = fy
        else:
            y = xm - (xm - xl)/gr1
            fy = ftn(y)
            if (fy >= fm):
                xr = xm
                fr = fm
                xm = y
                fm = fy
            else:
                xl = y
                fl = fy
    return(xm)

## -----------------------------------------------------
## 1.3 'optimize.fmin' in scipy.optimize as optimize
## -----------------------------------------------------

# ------------------------
# Maximize function: f1
# ------------------------

print " -----------------------------------"
print " Newton results "
print " -----------------------------------"
print str(newton(f1, 0.25))
print str(newton(f1, 0.5))
print str(newton(f1, 0.75))
print str(newton(f1, 1.75))
print " "
print " -----------------------------------"
print " Golden section results "
print " -----------------------------------"
print str(gsection(f1simple, 0.1, 0.25, 1.3))
print str(gsection(f1simple, 0.25, 0.5, 1.7))
print str(gsection(f1simple, 0.6, 0.75, 1.8))
print str(gsection(f1simple, 0.0, 2.75, 5.0))
print " "
print " -----------------------------------"
print " optimize.fmin "
print " -----------------------------------"
print str(optimize.fmin(f1simpleNeg, 0.25))
print str(optimize.fmin(f1simpleNeg, 0.5))
print str(optimize.fmin(f1simpleNeg, 0.75))
print str(optimize.fmin(f1simpleNeg, 1.75))


# -----------------------------------------------------------------
# 2 Multivariate optimization
# -----------------------------------------------------------------

# Here we want to optimize the following functions: f3, f4

# -------------------------------------------------
# Function f3 
# -------------------------------------------------
def f3simple(x):
    a = x[0]**2/2.0 - x[1]**2/4.0
    b = 2*x[0] - exp(x[1])
    f = sin(a)*cos(b)
    return(f)

def f3simpleNeg(x):
    a = x[0]**2/2.0 - x[1]**2/4.0
    b = 2*x[0] - exp(x[1])
    f = -sin(a)*cos(b)
    return(f)


def f3(x):
    a = x[0]**2/2.0 - x[1]**2/4.0
    b = 2*x[0] - exp(x[1])
    f = sin(a)*cos(b)
    f1 = cos(a)*cos(b)*x[0] - sin(a)*sin(b)*2
    f2 = -cos(a)*cos(b)*x[1]/2 + sin(a)*sin(b)*exp(x[1])
    f11 = -sin(a)*cos(b)*(4 + x[0]**2) + cos(a)*cos(b) - cos(a)*sin(b)*4*x[0]
    f12 = sin(a)*cos(b)*(x[0]*x[1]/2.0 + 2*exp(x[1])) + cos(a)*sin(b)*(x[0]*exp(x[1]) + x[1])
    f22 = -sin(a)*cos(b)*(x[1]**2/4.0 + exp(2*x[1])) - cos(a)*cos(b)/2.0 - cos(a)*sin(b)*x[1]*exp(x[1]) + sin(a)*sin(b)*exp(x[1])
    return (f, array([f1, f2]), array([[f11, f12], [f12, f22]])) # Function f3 returns: f(x), f'(x), and f''(x)

## Plot function f3
fig2 = figure()
ax = gca(projection='3d')
X = arange(-3, 3, .1)
Y = arange(-3, 3, .1)
X, Y = meshgrid(X, Y)

Z = zeros((len(X),len(Y)),float)
for i in range(len(X)):
    for j in range(len(Y)):
        Z[i][j] = f3simple([X[i][j],Y[i][j]])
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.jet,
        linewidth=0, antialiased=False)
show()

## -----------------------------------------------------
## 2.2 Newton
## -----------------------------------------------------
def newtonMult(f3, x0, tol = 1e-9, nmax = 100):
    # Newton's method for optimisation, starting at x0
    # f3 is a function that given x returns the list
    # {f(x), grad f(x), Hessian f(x)}, for some f
    x = x0
    f3x = f3(x)
    n = 0
    while ((max(abs(f3x[1])) > tol) and (n < nmax)):
        x = x - linalg.solve(f3x[2], f3x[1])
        f3x = f3(x)
        n = n + 1
    if (n == nmax):
        print "newton failed to converge"
    else:
        return(x)

## -----------------------------------------------------
## 2.3 'fmin_tnc' in scipy.optimize.tnc
## -----------------------------------------------------

## -----------------------------------------------------
## Maximize
## -----------------------------------------------------

## f3
for x0 in arange(1.4, 1.6, 0.1):
    for y0 in arange(0.4, 0.7, 0.1):
        print "Newton: f3        " +str([x0,y0]) + ' --> ' + str(newtonMult(f3, array([x0,y0])))  # This algorithm requires f(x), f'(x), and f''(x)
        print "optimize.fmin: f3 " +str([x0,y0]) + ' --> ' + str(optimize.fmin(f3simpleNeg, array([x0,y0])))        
        print " ----------------------------------------- "

   


