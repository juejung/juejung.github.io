# Homework 11

rm(list = ls())  # Remove almost everything in the memory
library(matlab)

cat("-------------- START ----------------")
setwd("C:/Dropbox/Towson/Teaching/3_ComputationalEconomics/Lectures/Lecture5/Homework/R")
source("./myfuncs.R")

#------------------------------------------------------------------------------
#Exercise 1
#------------------------------------------------------------------------------

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

# Define function of capital K
func = function(K) {
    s = - K + N_y*((beta*(1-tau_K)*(1+(alpha*A*K^(alpha-1)) - delta)* 
        ((1-tau_L)*((1-alpha)*A*K^alpha) + t_y) - t_o)/((1+beta)*(1-tau_K)*(1 + (alpha*A*K^(alpha-1)) - delta))) 
    
    return(s)
}


# Plot the function
Kmin = 0.0001
Kmax = 1.0
Kv = seq(Kmin, Kmax, by=(Kmax - Kmin)/200.0)
fK = array(0,c(length(Kv))) # define column vector

for (i in seq(1,length(Kv),by=1)){
    fK[i] = func(Kv[i])  
}

plot(Kv, fK)
lines(Kv, array(0,c(length(Kv))))
title('Function: f(K)=0')

# -----------------------------------------------------------------------------
# Method 1: Root finding
# -----------------------------------------------------------------------------

# Use built in 'uniroot'
cat(" \n")
cat(" -------------- Fsolve ------------\n")
Kstar = uniroot(func, lower=.01, upper=2)$root # starting from K = 2

Ystar = A*Kstar^alpha*L^(1-alpha)
qstar = alpha*A*Kstar^(alpha-1)
Rstar = 1 + qstar - delta
wstar = (1-alpha)*A*Kstar^alpha

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
cat(" -------------------------------------\n")
cat(" Root finding \n")
cat(" -------------------------------------\n")
cat("K* = " , Kstar,"\n")
cat("Y* = " , Ystar,"\n")
cat("q* = " , qstar,"\n")
cat("R* = " , Rstar,"\n")
cat("w* = " , wstar,"\n")
cat(" -------------------------------------\n")
cat("ARC = " , ARC,"\n")

# -----------------------------------------------------------------------------
# Method 2: Gauss-Seidl 
# -----------------------------------------------------------------------------

# Guess capital stock
glamda  = 0.5   # updating parameter
Kold    = 0.4
jerror  = 100
iter    = 1
while ((iter<200) || (jerror>0.001)){
    #    
    # Solve for prices using expressions for w(K) and q(K)
    q = alpha*A*Kold^(alpha-1) 
    w = (1-alpha)*A*Kold^alpha 
    R = 1 + q - delta
    Knew = N_y* (beta*(1-tau_K)*R*((1-tau_L)*w + t_y) - t_o)/((1+beta)*(1-tau_K)*R) 
    iter = iter +1
    
    # Update capital stock
    Kold    = glamda*Knew + (1-glamda)*Kold
    jerror  = abs(Kold-Knew)/Kold
}

# Print results
Kstar = Knew
Ystar = A*Kstar^alpha*L^(1-alpha)

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

cat(" -------------------------------------\n")
cat(" Gauss-Seidl \n")
cat(" -------------------------------------\n")
cat("Nr. of iterations = " ,iter,"\n")
cat("K* = " , Kstar,"\n")
cat("Y* = " , Ystar,"\n")
cat("q* = " , q,"\n")
cat("R* = " , R,"\n")
cat("w* = " , w,"\n")
cat(" -------------------------------------\n")
cat("ARC = " ,ARC,"\n")

#------------------------------------------------------------------------------
#Exercise 2
#------------------------------------------------------------------------------

# Set parameter values
tau_L   = 0.25 # increase labor tax

# Use built in 'fsolve'
cat(" \n")
cat(" -------------- Fsolve ------------\n")
Kstar2 = uniroot(func, lower=.0001, upper=2)$root # starting from K = 2

Ystar2 = A*Kstar^alpha*L^(1-alpha)

# Print results
cat(" -------------------------------------\n")
cat(" Root finding \n")
cat(" -------------------------------------\n")
cat("When tau_L=0.25\n")
cat("K* = " , Kstar2,"\n") #K*=0.1369683
cat("Y* = " , Ystar2,"\n") #Y*=0.566245

# -----------------------------------------------------------------------------
# Method 2: Gauss-Seidl 
# -----------------------------------------------------------------------------

# Guess capital stock
glamda  = 0.5   # updating parameter
Kold    = 0.4
jerror  = 100
iter    = 1
while ((iter<200) || (jerror>0.001)){
    #    
    # Solve for prices using expressions for w(K) and q(K)
    q = alpha*A*Kold^(alpha-1) 
    w = (1-alpha)*A*Kold^alpha 
    R = 1 + q - delta
    Knew = N_y* (beta*(1-tau_K)*R*((1-tau_L)*w + t_y) - t_o)/((1+beta)*(1-tau_K)*R) 
    iter = iter +1
    
    # Update capital stock
    Kold    = glamda*Knew + (1-glamda)*Kold
    jerror  = abs(Kold-Knew)/Kold
}

# Print results
Kstar2g = Knew
Ystar2g = A*Kstar^alpha*L^(1-alpha)

cat(" -------------------------------------\n")
cat(" Gauss-Seidl \n")
cat(" -------------------------------------\n")
cat("When tau_L=0.25\n")
cat("Nr. of iterations = " ,iter,"\n")
cat("K* = " , Kstar2g,"\n") 
cat("Y* = " , Ystar2g,"\n") 

#------------------------------------------------------------------------------
#Exercise 3
#------------------------------------------------------------------------------

# Set parameter values
tau_Lv   = seq(0.20,0.35, by=0.01)
Kstarv=zeros(1,length(tau_Lv))
Ystarv=Kstarv

for (i in (1:length(tau_Lv))) {
    tau_L=tau_Lv[i]
    
    Kstarv[i] = uniroot(func, lower=.0001, upper=3)$root  # starting from K = 2
    Ystarv[i] = A*Kstarv[i]^alpha*L^(1-alpha)
}
     
     
par(mfrow = c(2, 2))
     
plot(tau_Lv,Kstarv, type="b", main="Uniroot: Tax Rate vs Optimal Capital Stock",xlab="Tax Rate",ylab="Optimal Capital Stock")
plot(tau_Lv,Ystarv, type="b", main="Uniroot: Tax Rate vs Optimal Output",xlab="Tax Rate",ylab="Optimal Output")
     
     
# -----------------------
# Method 2: Gauss-Seidl 
# -----------------------

Kstarv=zeros(1,length(tau_Lv))
Ystarv=Kstarv

for (i in (1:length(tau_Lv))) {
    tau_L=tau_Lv[i]
         
    # Guess capital stock
    glamda  = 0.5   # updating parameter
    Kold    = 0.4
    jerror  = 100
    iter    = 1
    while ((iter<200) || (jerror>0.001)){
        #    
        # Solve for prices using expressions for w(K) and q(K)
        q = alpha*A*Kold^(alpha-1) 
        w = (1-alpha)*A*Kold^alpha 
        R = 1 + q - delta
        Knew = N_y* (beta*(1-tau_K)*R*((1-tau_L)*w + t_y) - t_o)/((1+beta)*(1-tau_K)*R) 
        iter = iter +1
        
        # Update capital stock
        Kold    = glamda*Knew + (1-glamda)*Kold
        jerror  = abs(Kold-Knew)/Kold
    }
    
    Kstarv[i] = Knew
    Ystarv[i] = A*Kstarv[i]^alpha*L^(1-alpha)
}

plot(tau_Lv,Kstarv, type="b", main="GaussS: Tax Rate vs Optimal Capital Stock",xlab="Tax Rate",ylab="Optimal Capital Stock")
plot(tau_Lv,Ystarv, type="b", main="GaussS: Tax Rate vs Optimal Output",xlab="Tax Rate",ylab="Optimal Output")




