
# Functions

# 1 Use simple user defined functions


A function in ***R*** can be defined as follows:



```r
# File 1: myFunctions.R
hw1 = function(r1, r2) {
    s = sin(r1 + r2)
    return(s)
}

hw2 = function(r1, r2) {
    s = sin(r1 + r2)
    cat("Hello, World! sin(", r1, "+", r2, ") = ", s)
}
```



We save this file as ```myFunctions.R``` in some directory, preferably the one you are working in. In order to use these two simple functions we have to first import them. The command to import the functions is ```source("functionPath/functionName.R")``` where functionPath is the path to where your function script is stored and functionName.R is the script file that contains the function definition. In our example the command to load the user defined functions ```hw1``` and ```hw2``` is ```source("./myFunctions.R")``` as can be seen in this simple example script.



```r
# File 2: Lecture5.R
setwd("C:/Dropbox/Towson/Teaching/3_ComputationalEconomics/Lectures/Lecture5/R")
source("./myFunctions.R")  # Here we load the function from our function file myFunctions.R

# Now we are ready to call on the above defined user functions.

hw1(2.6, 4)
```

```
## [1] 0.3115
```

```r

hw2(2.5, 5.6)
```

```
## Hello, World! sin( 2.5 + 5.6 ) =  0.9699
```




In Python we can write the following to define a simple function. We start with two simple function definitions and save them in a file called myFunctions.py

```
# File 1: myFunctions.py
import math

def hw1(r1, r2):
    s = math.sin(r1 + r2)
    return s

def hw2(r1, r2):
    s = math.sin(r1 + r2)
    print 'Hello, World! sin(%g+%g)=%g' % (r1, r2, s)
```
In a separate Python script we can now import this previous file containing our functions with the ```import``` command. We save this new Python script as Lecture5.py

```
# File 2: Lecture5.py
import myFunctions as mfunc
   
# Now we call these functions with function arguments
print mfunc.hw1(2.6,4.0)
mfunc.hw2(2.5,5.6)
```
```
0.311541363513
Hello, World! sin(2.5+5.6)=0.96989
```


# 2 Advanced Graphing using loops and functions


## 2.1 Graphing functions with two input arguments z = f(x,y)



```r
library("lattice")

x = seq(1, 10, by = 1)
y = seq(1, 10, by = 1)
n = length(x)

f = matrix(0, n, n)  # Define matrix size nxn with zero entries
for (i in 1:n) {
    for (j in 1:n) {
        f[i, j] = sin(y[j] * x[i])
    }
}

# This plots the 3-dimensional function
wireframe(f)
```

![plot of chunk R3](figure/R3.png) 



## 2.2 Same thing but different function

This time we define the function first: $$latex g = f(x, y)=(1 + y * 2) ^ {(-x / y)} * (1 + y * 1) ^ {(x / y)} $$
We then span a grid over x and y and evaluate the function g at each combination of (x,y) using the ```expand.grid``` command.



```r
g = function(x, y) {
    (1 + y * 2)^(-x/y) * (1 + y * 1)^(x/y)
}

myRange = seq(0.01, 1, len = 20)
grid = expand.grid(x = myRange, y = myRange)
grid$z = g(grid$x, grid$y)
print(wireframe(z ~ x * y, grid))
```

![plot of chunk R4](figure/R4.png) 


The corresponding scripts for Python follow next.

```python
from mpl_toolkits.mplot3d import Axes3D

X = arange(1, 11, 1)
Y = arange(1, 11, 1)

X, Y = meshgrid(X, Y)
xn, yn = X.shape

f =    zeros((xn,xn),float)   # Define matrix size nxn with zero entries
for i in range(xn):
    for j in range(yn):
        #print i,j
        f[i,j] = sin(X[i,j]*Y[i,j])
        
fig1=figure()
ax = Axes3D(fig1)
ax.plot_wireframe(X, Y, f, rstride=2, cstride=2)
show()
```
```

```


In **Python** we define the function using the ```def``` command. The grid space between (x,y) is created using the ```meshgrid``` command. The function ```g``` is then evaluated at every point (x,y) over the grid. The ```ax.plot_wireframe``` command produces the picture.

```python
def g(x, y):
    res=(1 + y * 2) ** (-x / y) * (1 + y * 1) ** (x / y)
    return res

X = linspace(0.01, 1, 20)
X, Y = meshgrid(X, X)
xn, yn = X.shape

f =    zeros((xn,xn),float)   # Define matrix size nxn with zero entries
for i in range(xn):
    for j in range(yn):
        f[i,j] = g(X[i,j], Y[i,j])

fig2=figure()
ax = Axes3D(fig2)
ax.plot_wireframe(X, Y, f, rstride=2, cstride=2)
show()
```
```

```
