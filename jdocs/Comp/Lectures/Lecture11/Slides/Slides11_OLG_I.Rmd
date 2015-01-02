% Econ I Module
% Juergen Jung
% Towson University, 2012

# A simple OLG model

* OLG stands for overlapping generations
* This model allows for young and old agents
* We start with
    * Preferences
    * Technology
    * Government
    * Equilibrium
    
--------------------------------------------------------------------------------
# Preferences

* Agents live for 2 periods: young and old
* There are $latex  N_y$ young households and $latex  N_o$ old households 
* They value consumption when young $latex c_y$ and consumption when old $latex c_o$
* Their preferences are given via utility functions: $latex u_t(c_t)$
* Agents discount time with factor $latex \beta$
* Their life-time utility is:

$$latex V(c_y, c_o) = u(c_y) + \beta \times u(c_o) $$

--------------------------------------------------------------------------------
# Technology

* Firms produce output $latex Y$ using input capital $latex K$ and labor $latex L$:

$$latex Y= F(K,L) = A \times K^{\alpha} \times L^{(1-\alpha)} $$

* Firms maximize profits:

$$latex max_{\left\{K,L\right\}} F(K,L) - wL - qK $$

* $latex w$ are wages and $latex q$ is the factor price of capital


--------------------------------------------------------------------------------
# Government

* The government collects taxes on labor $latex \tau_L$ and capital $latex \tau_K$
* The government pays for gov't consumption $latex G$ and transfers to households 
$T_y$ and $latex T_o$

$$latex G + T_y + T_o =  \tau_L \times wL + \tau_K \times RK $$


--------------------------------------------------------------------------------
# Household problem

* HHs maximize $latex V(c_y,c_o)$ subject to their budget constraint in each period
$$ c_y + s = (1-\tau_L) w   + t_y $$
$$ c_o     = (1-\tau_K) Rs + t_o  $$

--------------------------------------------------------------------------------
# Equilibrium definition

* Given sequences of 
    * prices $latex \left\{w_t, R_t \right\}$ 
    * government policies $latex \left\{\tau_K, \tau_{L} \right\}$
and equilibrium is defined as an allocation of:
* sequences of $latex \left\{c_{y,t},c_{o,t},s_t\right\}$ so that
    * the HH max problem is solved
    * the firm maximization problem is solved, so that:
        * $latex q = F_K$
        * $latex w = F_L$
        * $latex R = (1 + q - \delta)$ is the after tax interest rate
    * the gov't budget constraint clears
    * Markets clear:
        * $latex K=S = N_y * s^*$
        * $latex ARC: C + S +G = Y - (1-\delta) K$

--------------------------------------------------------------------------------
# Functional forms and solutions

* Preferences are given as: $latex u(c_y) = log(c_y)$ and $latex u(c_o)=log(c_o)$
* We can either set up a Lagrangian with two constraints or simply substitute
consumption out of the utilities using the BC. 
* We follow the second approach, since the form of the utility functions 
guarantees interior solutions
* Therefor we don't have to worry about corner solutions a la Kuhn-Tucker

--------------------------------------------------------------------------------
# Substitute the budget set into preferences

$$latex max_s log( (1-\tau_L)w + t_y - s)  + \beta  log( (1-\tau_K)R  s + t_o) $$

* This is now a function in 1 choice variable $latex s$ 
* Derive this function w.r.t. $latex s$ 

$$latex \frac{\partial V}{\partial s}: \frac{1}{ (1-\tau_L)w + t_y - s} =
\frac{\beta (1-\tau_K)R}{(1-\tau_K)R  s + t_o}$$

--------------------------------------------------------------------------------
# Solve for optimal household savings: $latex s^*$ 

$$latex s^* = \frac{\beta (1-\tau_K)R ((1-\tau_L)w + t_y) - t_o}{(1+\beta)(1-\tau_K)R} $$ 

* In equilibrium household savings equals the capital stock: $latex S = K$
* Aggregate capital stock is therefore: $latex K = S = N_y \times s^*$

--------------------------------------------------------------------------------
# Solution

* Given parameter $latex \beta$, gov't policies $latex \tau_K, \tau_L, t_y, t_o$
* Measures of young and old agents $latex N_y, N_o$ we can now solve for a steady
  state equilibrium
* The solution is represented by the following equation system
* We will try to reduce the equation system into as few equations as possible,
  ideally into one non-linear equation that we can then solve with a ``Newton
  Algorithm``

--------------------------------------------------------------------------------
# Equation system

* For starters we assume that government is completely exogenous.
* Assume $latex L=1$ we have the following unknowns: $latex K,Y,R,w,q$ and the following
equation. 
* A solution exists if the number of unknowns is equal to the number of
equations:

$$latex K=N_y s^* = N_y \frac{\beta (1-\tau_K)R ((1-\tau_L)w + t_y) - t_o}{(1+\beta)(1-\tau_K)R} $$ 

$$latex \alpha*Y/K = q $$

$$latex (1-\alpha)*Y/L = w $$

$$latex F(K,L) = A \times K^{\alpha} \times L^{(1-\alpha)} $$

$$latex R = (1 + q - \delta) $$ 

--------------------------------------------------------------------------------
# Method 1: Substituting everything 

* Note that $latex L=1$
* Substitute $latex Y$ out and get $latex q(K)$ and $latex w(K)$.
* Use $latex q(K)$ in $latex R$ and get $latex R(K)$

$$latex w = (1-\alpha)*A \times K^{\alpha} $$

$$latex R = 1 + (\alpha* A \times K^{\alpha-1}) - \delta $$

* Plug $latex w(K)$ and $latex R(K)$ into $latex K$-equation

* We now have one equation in $latex K$ only

--------------------------------------------------------------------------------
# One equation in K

$$latex K= N_y \frac{\beta (1-\tau_K)(1 + (\alpha* A \times K^{\alpha-1}) - \delta) 
((1-\tau_L)((1-\alpha)*A \times K^{\alpha}) 
+ t_y) - t_o}{(1+\beta)(1-\tau_K)(1 + (\alpha* A \times K^{\alpha-1}) - \delta)} $$ 

* Model parameters: $latex N_y=N_o=1$, $latex \alpha=0.3$, $latex A=1$, $latex \beta = 0.9$, $latex \delta=0.1$
* We assumed that government was exogenous, so here are some government
  parameters: $latex \tau_L=0.2$, $latex \tau_K=0.15$, $latex T_y=T_o=t_y=t_o=0$
* Solve for $latex K^*$ and then back out $latex q^*(K^*),w^*(K^*),R^*(K^*), Y^*(K^*)$ which are all functions of $latex K^*$

--------------------------------------------------------------------------------
# Aggregate resource constraint (ARC)

* Aggregate consumption is:
$$latex C = N_y*c_y + N_o*c_o $$

* Aggregate government consumption is:
$$latex G  =  \tau_L \times wL + \tau_K \times RK - N_y*t_y - N_o*t_o $$

* The aggregate resource constraint (or goods market clearing condition) is:
$$ C + N_y*s + G = Y + (1-\delta)K $$


--------------------------------------------------------------------------------
# Python Program 1 

```
import math
from pylab import *
from scipy.optimize import fsolve

# -----------------------------------------------------------------------------
# Root finding 
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
    ((1-tau_L)*((1-alpha)*A*K**alpha) + t_y) - t_o)/((1+beta)*(1-tau_K)*
    (1 + (alpha*A*K**(alpha-1)) - delta))) 

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


## Use built in 'fsolve'
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


```

--------------------------------------------------------------------------------
# Method 2

* Instead of substituting and solving for one equation in one unknown we can
  use the so called **Gauss-Seidl** method
  1. For this method we start with a guess for capital $latex K_{old}$
  2. We then solve for prices $latex w,R,q$
  3. We then solve for optimal household savings $latex s^*$
  4. We then aggregate over all households and get the new capital stock $latex K_{new}$
  5. We then update capital $latex K_{old} = \lambda * K_{new} + (1-\lambda) * K_{old}$ and repeat from point 1 ($latex \lambda$ is an updating parameter)

--------------------------------------------------------------------------------
# Python Program 2

```
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
```
