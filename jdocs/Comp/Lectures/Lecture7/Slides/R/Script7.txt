# -------------------------------------------
# 1 Random numbers
# -------------------------------------------

rm(list=ls()) # Remove almost everything in the memor
set.seed(100) # To always get the same random numbers on each run (makes results reproducible)


# Uniform distributed random numbers
u   = runif(10000)
hist(u)


# Normally distributed random numbers
z   = rnorm(10000)  # draws 10,000 standard normally distributed random numbers
hist(z, breaks = seq(-5,5,0.2), freq = F)
phi = function(x) exp(-x^2/2)/sqrt(2*pi)  # density function of standard normal
x   = seq(-5,5,0.1)
lines(x,phi(x))

## For instance, if you want to simulate from a standard normal distribution, you can simulate from a standard uniform and transform it using the quantile function of the normal distribution.
N   = 10000
z   = qnorm(runif(N))
hist(z, breaks = seq(-5,5,0.2), freq = F)


## Two normally distributed random variables
z1   = rnorm(10000, mean=1, sd=1)
z2   = rnorm(10000, mean=1, sd=2)

par(mfrow = c(2, 1))        # Set up plotting in 3rows and 2 columns, plotting along rows first.
  
hist(z1)     
hist(z2)


# T-distributed random variable
par(mfrow = c(1, 1))
t   = rt(10000,20)
hist(t)

# distribution      R name
# ----------------------------
# Beta	            Beta	    
# Binomial	        binom	    
# Cauchy	          cauchy	    
# Chisquare	        Chisquare	
# Exponential	      exp	        
# F	                f	        
# Gamma	            gamma	    
# Geometric	        geom	    
# Hypergeom.	        hyper	    
# Logistic	        logis	 	 
# Lognormal	        lnorm
# Negative Binomial 	nbinom
# Normal	            norm
# Poisson	            pois
# Student t 	        t
# Uniform	            unif
# Tukey	            tukey
# Weibull	          weib
# Wilcoxon	        wilcox	 

# -----------------------------------------------------------------------------
a = 20 # lower bound uniform distribution
b = 60 # upper bound uniform distribution
n = 400 # sample size
runs = 10000
xmeanv = zeros(1,runs)

for (i in 1:runs) {
    xv = a + (b-a) * runif(n) # draws the sample of size n
    xmeanv[i] = mean(xv) 
}

hist(xmeanv,30)

