# -*- coding: utf-8 -*-
"""
# =====================================================================
#
# Scriptfile Lecture 10
# -------------------------
# Computational Economics
# (c) Juergen Jung, 2012
#
# =====================================================================

"""
import math
from pylab import *
import scipy.optimize as optimize


# -------------------------------------------
# Cake eating: constrained optimization
# -------------------------------------------

close('all')  # close all open figure


print("-------------- START ----------------")

# -----------------------------------------------------------------------------------
# 1. Analytical solution
# -----------------------------------------------------------------------------------
T = 9
beta = 0.9
kv = zeros(T+1,float)
cv = zeros(T+1,float)
uv = zeros(T+1,float)
kv[0] = 100                            # k0
cv[0] = (1.0-beta)/(1.0-beta**(T+1)) * kv[0]  # c0
uv[0] = log(cv[0])

for i in range(1,T+1):
    print "i=" + str(i)
    cv[i] = beta * cv[i-1]
    kv[i] = kv[i-1] - cv[i-1]
    uv[i] = beta**(i-1)*log(cv[i])  # period utility with discounting

sum(uv)  # total utility

print "cv= " +str(cv)
print "kv= " +str(kv)

fig1 = figure()
subplot(2,1,1)
plot(cv)
ylabel("c_t")
xlabel("Period t")
title("Consumption")

subplot(2,1,2)
plot(kv)
title("Cake size")
ylabel("k_t")
xlabel("Period t")
show()

# -----------------------------------------------------------------------------------
# 2. Numerical solution
# -----------------------------------------------------------------------------------
def func1(cv):
    T = len(cv)
    uv= zeros(T,float)
    for i in range(T):
        beta = 0.9
        uv[i] = (beta**i) * log(cv[i])  # period utility with discounting
    return (-sum(uv))


# The constraint
def eqn1(cv):
    k0 = 100
    z1=sum(cv) - k0
    return array([z1])

# Call the optimizer with some starting values for the consumption vector
T = 10
x0 =ones(T,float)*0.1
coptv= optimize.fmin_slsqp(func1, x0, f_eqcons = eqn1)  #, f_eqcons = eqn1


# Plot analytical and numerical solution
fig2 = figure()
plot(arange(0,T), cv, 'b-', arange(0,T), coptv, 'r--')
title("Optimal consumption")
xlabel("Period t")
ylabel("c_t")
# Create a legend 
legend(('analytical', 'numerical'),'lower right', shadow=True) 
print ('Analytic solution cv =' + str(cv))
print ('Numeric soluntion cv =' + str())