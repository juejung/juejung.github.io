# Root finding

# 1 First steps
```python
import math
from pylab import *
from scipy.optimize import fsolve
close('all')  # close all open figure
```
```

```

## 1.1 Define example function

Define am example function for which we calculate the root, i.e. find x so that f(x) = 0

```python
def func(x):
    s = log(x) - exp(-x)  # function: f(x)
    return s
```
```

```


Define the same function  but this time we return the functional value and the first derivate of the function (i.e. the gradient).

```python
def func1(x):
    s = log(x) - exp(-x)  # function: f(x)
    sp= 1.0/x + exp(-x)      # derivative of function: f'(x)
    return array([s,sp])    
```
```

```


## 1.2 Plot the function

```python
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
```
```
Traceback (most recent call last):
  File "<string>", line 3, in <module>
NameError: name 'arange' is not defined
```


-------------------------------------------------------------------------------
# 2 Newton-Raphson

## 2.1 The method

We start with an initial guess $latex x_0$. The tangent line through the initial guess can be defined as:

$$latex f'(x_0)=\frac{f(x_0)-y}{x_0-x}$$
This line crosses the x-axis at point $latex x_1$ so that
$$latex f'(x_0)=\frac{f(x_0)-0}{x_0-x_1}$$ 
which we can solve for $latex x_1$ as:
$$latex x_1 = x_0 - \frac{f(x_0)}{f'(x_0)}.$$
We can repeat this successively using the iterative procedure:
$$latex  \boxed{x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}}$$

## 2.2 Define the Newton-Raphson algorithm

```python
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
```
```

```



## 2.3 Calculate the root of the function calling 'newtonraphson'

```python
newtonraphson(func1, 2)
```
```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
NameError: name 'newtonraphson' is not defined
```


-------------------------------------------------------------------------------
# 3 Secant method

## 3.1 Define the secant method

In this case we start with two starting values $latex x_0$ and $latex x_1$ and put a line through the functional values $latex f(x_0)$ and $latex f(x_1)$. The advantage of this method is that we do not have to calculate the first derivative of the function.The line through $latex f(x_0)$ and $latex f(x_1)$ is expressed as:
$$latex \frac{y-f(x_1)}{x-x_1} = \frac{f(x_0)-f(x_1)}{x_0-x_1}.$$

The point $latex x_2$ where this line crosses the x-axis can be found using:
$$latex \frac{0-f(x_1)}{x_2-x_1} = \frac{f(x_0)-f(x_1)}{x_0-x_1},$$
which results in
$$latex x_2 = x_1 - f(x_1)\frac{x_0-x_1}{f(x_0)-f(x_1)}.$$

The iterative procedure can be written as:
$$latex \boxed{x_{n+1} = x_n - f(x_n)\frac{x_{n-1}-x_n}{f(x_{n-1})-f(x_n)}}$$

Note that if $latex x_0$ and $latex x_1$ are close together then:
$$f'(x_n) \approx f(x_1)\frac{f(x_n)-f(x_{n-1})}{x_n-x_{n-1}}.$$


## 3.2 The algorithm of the secant method

```python
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
```
```

```


## 3.3 Calculate the root of the function calling 'secant'

```python
secant(func, 1,2)
```
```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
NameError: name 'secant' is not defined
```


-------------------------------------------------------------------------------
# 4 Bisection

## 4.1 Define the bisection method

The bisection method is the most robust method, but it is slow. We start with two values $latex x_l < x_r$ which bracket the root of the function. It therefore must hold that $latex f(x_l) f(x_r) < 0$. The algorithm then repeatedly brackets around the root in the following systematic way:

 1. if $latex x_r - x_l \le \epsilon$ then stop
 2. calculate midpoint: $latex x_m = (x_l+x_r)/2$
 3. if $latex f(x_m)==0$ stop
 4. if $latex f(x_l) f(x_r) < 0$ then set $latex x_r = x_m$ otherwise $latex x_l=x_m$
 5. go back to step 1


## 4.2 The algorithm of the bisection method

```python
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

```
```

```


## 4.3 Calculate the root of the function calling 'bisection'
```python
bisection(func, 1,2)
```
```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
NameError: name 'bisection' is not defined
```


# 5 Using built in unit-root function

```python
print " "
print " -------------- Fsolve ------------"
result = fsolve(func, 2) # starting from x = 2
print result
```
```
 
 -------------- Fsolve ------------
Traceback (most recent call last):
  File "<string>", line 3, in <module>
NameError: name 'fsolve' is not defined
```


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
 