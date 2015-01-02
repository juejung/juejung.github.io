# -*- coding: utf-8 -*-
"""
# =============================================================================
#
# Scriptfile Lecture 11
# -------------------------
# Computational Economics
# (c) Juergen Jung, 2012
#
# =============================================================================

"""
import math
from pylab import *
from scipy.optimize import fsolve

# -----------------------------------------------------------------------------
# Root finding vs. Gauss-Seidl 
# -----------------------------------------------------------------------------

close('all')  # close all open figure

# Set parameter values
N_y     = 1.0
N_o     = 1.0
alpha   = 0.3
A       = 1
beta    = 0.9
delta   = 0.0
tau_L   = 0.2
tau_K   = 0.15
t_y     = 0.0
t_o     = 0.0
#
L       = 1


# -----------------------------------------------------------------------------
# Method 1: Root finding
# -----------------------------------------------------------------------------
# Define function of capital K
def func(K):
    s = - K + N_y*((beta*(1-tau_K)*(1+(alpha*A*K**(alpha-1)) - delta)* \
    ((1-tau_L)*((1-alpha)*A*K**alpha) + t_y) - t_o)/((1+beta)*(1-tau_K)*(1 + (alpha*A*K**(alpha-1)) - delta))) 

    return s


# Plot the function
Kmin = 0.0001
Kmax = 1.0
Kv = arange(Kmin, Kmax, (Kmax - Kmin)/200.0)
fK = zeros(len(Kv),float) # define column vector

for i in range(len(Kv)):
    fK[i] = func(Kv[i])
    
#print "fK=" +str(fK)

fig1 = figure()
plot(Kv, fK)
plot(Kv, zeros(len(Kv)))
show()


# Use built in 'fsolve'
print " "
print " -------------- Fsolve ------------"
Kstar = fsolve(func, 2) # starting from K = 2

Ystar = A*Kstar**alpha*L**(1-alpha)
qstar = alpha*A*Kstar**(alpha-1)
Rstar = 1 + qstar - delta
wstar = (1-alpha)*A*Kstar**alpha
#
# ------------------------------------
# Back out solutions for the rest of the Economy

# Household values
sstar = Kstar/N_y
cystar= (1-tau_L)*wstar + t_y - sstar
costar= (1-tau_K)*Rstar*sstar + t_o
Gstar = N_y*tau_L*wstar + N_o*tau_K*Rstar*sstar  # residual gov't consumption, thrown in the ocean

# Aggregate consumption
Cstar = N_y*cystar + N_o*costar

# Check the goods market condition or Aggregate resource constraint
ARC = Ystar - delta*Kstar - Cstar - Gstar


# Print results
print " -------------------------------------"
print " Root finding "
print " -------------------------------------"
print "K* = " + str(Kstar)
print "Y* = " + str(Ystar)
print "q* = " + str(qstar)
print "R* = " + str(Rstar)
print "w* = " + str(wstar)
print " -------------------------------------"
print "ARC = " + str(ARC)

# -----------------------------------------------------------------------------
# Method 2: Gauss-Seidl 
# -----------------------------------------------------------------------------

# Guess capital stock
glamda  = 0.5   # updating parameter
Kold    = 0.4
jerror  = 100
iter    = 1
while (iter<200) or (jerror>0.001):
    #    
    # Solve for prices using expressions for w(K) and q(K)
    q = alpha*A*Kold**(alpha-1) 
    w = (1-alpha)*A*Kold**alpha 
    R = 1 + q - delta
    Knew = N_y* (beta*(1-tau_K)*R*((1-tau_L)*w + t_y) - t_o)/((1+beta)*(1-tau_K)*R) 
    iter = iter +1
    # Update capital stock
    Kold    = glamda*Knew + (1-glamda)*Kold
    jerror  = abs(Kold-Knew)/Kold

# Print results
Kstar = Knew
Ystar = A*Kstar**alpha*L**(1-alpha)

# ------------------------------------
# Back out solutions for the rest of the Economy

# Household values
sstar = Kstar/N_y
cystar= (1-tau_L)*wstar + t_y - sstar
costar= (1-tau_K)*Rstar*sstar + t_o
Gstar = N_y*tau_L*wstar + N_o*tau_K*Rstar*sstar  # residual gov't consumption, thrown in the ocean

# Aggregate consumption
Cstar = N_y*cystar + N_o*costar

# Check the goods market condition or Aggregate resource constraint
ARC = Ystar - delta*Kstar - Cstar - Gstar

print " -------------------------------------"
print " Gauss-Seidl "
print " -------------------------------------"
print "Nr. of iterations = " +str(iter)
print "K* = " + str(Kstar)
print "Y* = " + str(Ystar)
print "q* = " + str(q)
print "R* = " + str(R)
print "w* = " + str(w)
print " -------------------------------------"
print "ARC = " + str(ARC)