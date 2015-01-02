
# Random numbers

# 1 Uniformly distributed random numbers
```
import math
from pylab import *
import random

close('all')  # close all open figure
seed([100])   # To always get the same random numbers on each run (makes results reproducible)
N = 30        # number of classes (i.e. bins or bars) in histogram

u   = uniform(0,1,(10000,)) # Uniform distributed random numbers

fig1 = figure()
prob, bins, patches = hist(u, bins=N, align='mid' )
ylabel('Number of obs')
title('Histogram of uniform random variable')
show()
```

# 2 Normally distributed random numbers
```python
def phi(x):
    s = exp(-x**2/2)/math.sqrt(2*math.pi)  # density function of standard normal
    return s
    
z   = normal(0,1,(10000,))  # draws 10,000 standard normally distributed random numbers

fig2 = figure()
prob, bins, patches = hist(z, normed=1,bins=N, align='mid' )
ylabel('Number of obs')
title('Histogram of normal random variable')
# Plot the N(0,1) density function into the histogram 
x   = arange(-5,5,0.1)
plot(x,phi(x))
show()
```
```
Traceback (most recent call last):
  File "<string>", line 5, in <module>
NameError: name 'normal' is not defined
```


## 2.1 Two normally distributed random variables
```python
z1   = normal(0,1,(10000,))
z2   = normal(0,2,(10000,))

fig3 = figure()
subplot(211)
prob, bins, patches = hist(z1, bins=N, align='mid' )
ylabel('Number of obs')
title('Histogram of N(0,1) random variable')
subplot(212)    
prob, bins, patches = hist(z2, bins=N, align='mid' )
ylabel('Number of obs')
title('Histogram of N(0,2) random variable')
show()
```
```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
NameError: name 'normal' is not defined
```


# 3 T-distributed random variable

```python
def student_tvariate(df): # df is the number of degrees of freedom 
    if df < 2 or int(df) != df: 
        raise ValueError, 'student_tvariate: df must be a integer > 1' 
    x = random.gauss(0, 1) 
    y = random.gammavariate(df/2.0, 2) 
    return x / (math.sqrt(y/df))

t = zeros((10000),float)
for i in range(10000):
    t[i]   = student_tvariate(20)

fig4 = figure()
prob, bins, patches = hist(t, bins=N, align='mid' )
ylabel('Number of obs')
title('Histogram of T(dof=20) random variable')
show()
```
```
Traceback (most recent call last):
  File "<string>", line 8, in <module>
NameError: name 'zeros' is not defined
```





    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
