# Homework 9
#
#------------------------------------------------------------------------------
# -*- coding: utf-8 -*-

# Exercise 1
#------------------------------------------------------------------------------
import numpy as np
from scipy.optimize import fmin
import matplotlib.pyplot as plt
plt.close('all')  # close all open figure

# Function definitions
# -----------------------------------------------------------------------------
def f1(x):
    if x ==0:
        return 0
    else:
        return np.abs(x)*np.log(np.abs(x)/2)*np.exp(-np.abs(x))

def f_Profit(K):
    # This global statement means that L is defined outside of the function
    global L
    w = 1.84
    r = 0.75
    A = 4
    # Return negative value, because we'd like to maximize profits
    return - (A*(K**0.33 * L**0.67) - w*L - r*K)

def gsection(ftn, xl, xm, xr, tol = 1e-9):
    # applies the golden-section algorithm to maximise ftn
    # we assume that ftn is a function of a single variable
    # and that x.l < x.m < x.r and ftn(x.l), ftn(x.r) <= ftn(x.m)
    #
    # the algorithm iteratively refines x.l, x.r, and x.m and
    # terminates when x.r - x.l <= tol, then returns x.m
    # golden ratio plus one
    gr1 = 1 + (1 + np.sqrt(5))/2
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

# Exercise 1:
# -----------------------------------------------------------------------------

xv = np.linspace(-10,10,200)
yv = np.zeros(200)

for i, x in enumerate(xv):
    yv[i] = f1(x)


fig, ax = plt.subplots()
ax.plot(xv, yv, 'k-')
# Create a title with a red, bold/italic font
ax.set_title('Function 1')
plt.show()


xl = -1
xm = 0.5
xr = 1
sol =gsection(f1, xl, xm, xr)
print('first max = {}'.format(sol))

xl = -5
xm = -3
xr = -2
sol =gsection(f1, xl, xm, xr)
print('second max = {}'.format(sol))

xl = 2
xm = 4
xr = 5
sol = gsection(f1, xl, xm, xr)
print('third max = {}'.format(sol))
print('----------------------------')



# Exercise 2:
# -----------------------------------------------------------------------------
Lv = np.arange(1.0, 5.0, 0.5)
Kstarv = np.zeros(len(Lv))

# Some starting guess
K0 = 0.5
for i,l in enumerate(Lv):
    L = l  # This is the global variable that will now change within the profit function
    sol = fmin(f_Profit, K0)
    Kstarv[i] = sol[0]
    print('Solution for L = {} is Kstar = {}'.format(l, sol[0]))

# fig, ax = plt.subplots()
# ax.plot(Lv, Kstarv, 'k-')
# # Create a title with a red, bold/italic font
# ax.set_title('Optimal Capital Input')
# plt.show()


# Exercise 3:
# -----------------------------------------------------------------------------

def f_PlotInterimResults(ftn, xl, xm, xr):
    xv = np.linspace(-5,5,100)
    yv = np.zeros(len(xv))
    for i,x in enumerate(xv):
        yv[i] = ftn(x)

    fig, ax = plt.subplots()
    ax.plot(xv,yv, 'k-')
    ymin = np.min(yv)
    ymax = np.max(yv)

    ax.vlines(xl, ymin, ymax, color ='b')
    ax.vlines(xr, ymin, ymax, color ='r')
    ax.vlines(xm, ymin, ymax, color ='g')

    # Create a title with a red, bold/italic font
    ax.set_title('Golden Section Algorithm')
    plt.show()

def gsection(ftn, xl, xm, xr, tol = 1e-9):
    # applies the golden-section algorithm to maximise ftn
    # we assume that ftn is a function of a single variable
    # and that x.l < x.m < x.r and ftn(x.l), ftn(x.r) <= ftn(x.m)
    #
    # the algorithm iteratively refines x.l, x.r, and x.m and
    # terminates when x.r - x.l <= tol, then returns x.m
    # golden ratio plus one
    gr1 = 1 + (1 + np.sqrt(5))/2
    #
    # successively refine x.l, x.r, and x.m
    fl = ftn(xl)
    fr = ftn(xr)
    fm = ftn(xm)
    iter = 0
    while ((xr - xl) > tol and iter<100):
        if iter < 5:
            # Only stop to plot for the first 5 iterations
            f_PlotInterimResults(ftn, xl, xm, xr)

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
        iter += 1
    return(xm)

# Now call this
xl = -5
xm = -3
xr = -2
sol =gsection(f1, xl, xm, xr)
print(sol)


