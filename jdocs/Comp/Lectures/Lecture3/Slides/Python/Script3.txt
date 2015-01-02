#!/usr/bin/env python

# Here we want to call our two Python functions that are saved in myfunctions.py
# We can import these functions as follows:

import time                     # Imports system time module to time your script
from pylab import *             # Imports numpy, scipy, and matplotlib etc.


tic = time.clock()              # Start timer
# -----------------------------------------------------------------------------
close('all')  # close all open figures
# ------------------------------------------------------------------------------

# Basic programming

# --------------------------------------------------
# 1 Branching
# --------------------------------------------------
x = random(1)  # draw a random number between 0 and 1
if (x > 0.5):
    print("Number x="+str(x)+" is greater than 0.5")
else:
    print("Number x="+str(x) +" is smaller than or equal to 0.5")


x = random(1)
y = random(1)

if (x > y):
    print("X is greater than Y")
elif (x==y):
    print("X is equal to Y")
elif (x < y):
    print("X is smaller than Y")


# --------------------------------------------------
# 2 For loops
# --------------------------------------------------

## Loop 1
# --------------------------
xv = arange(1, 9, 2)
sumx = 0

for x in xv:
    sumx = sumx + x  # adds up the elements in vector xv
    print("X =" + str(x))
    print("sum(x) = " + str(sumx))

# or simply
print("sum(xv)= " + str(sum(xv)))

## Loop 2
# --------------------------
n = 6
n_fac = 1

for i in range(1,n+1):
    print("i = ", i)
    n_fac = n_fac * i

print("The factorial of " + str(n) + " is: " + str(n_fac))

## Loop 3
# --------------------------
xv = linspace(1,9, 20)

for i in range(len(xv)):
    print("i= ", i)
    print("xv[i]= ", xv[i])


yv = sqrt(xv)
fig1 = figure()

plot(xv,yv, "o", xv,xv, ":")
ylim(0,9)
title("Simple plot of two vectors")
show()


# --------------------------------------------------
# 3 While loop
# --------------------------------------------------

## While loop 1
# -------------------------
x = 0
y = 0
while (x < 10):
    y = y + x
    print("X= " +  str(x) + " and Y= " + str(y))
    x = x + 1


## While loop 2
# -------------------------
r           = 0.11  # annual interest rate
period      = 1/12  # time between repayments in years (i.e. monthly repayments)
debt_initial= 1000  # initial debt
payments    = 12    # amount repaid each period

mytime = 0
debt = debt_initial
while (debt> 0):
    mytime = mytime + period
    debt = debt*(1 + r*period) - payments

print("Loan will be repaid in: "+ str(mytime) + " years.")

# -----------------------------------------------------------------------------
toc = time.clock()              # Stop timer
print "Time passed: " + str(toc - tic)


# -----------------------------------------------------------------------------
# Exercises

# Exercise:
xv = arange(-5,5,0.1)
yv = xv*0
for i in range(len(xv)):
    if (xv[i]<1):
        yv[i] = xv[i]**2
    elif (xv[i]>=1):
        yv[i] = log(xv[i])

plot(xv,yv,'o')