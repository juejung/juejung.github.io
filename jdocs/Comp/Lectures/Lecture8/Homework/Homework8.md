# Homework 8: Root finding

Submit this homework in class on Tuesday.
I need two files:

  * R-scripts are submitted in one file called: ``Homework8.R``
  * Python-scripts are submitted in one file called: ``Homework8.py``

I need to be able to quickly run these scripts on my computer.

I will based your homework grade on my grading of 2 randomly selected homework exercises. So please make sure that you complete every homework 100% as you might otherwise end up with zero points.

Implement all exercises in **R** and **Python**!


## Exercise 1
-------------------------------------------------------------------------------

Read chapter 10 in your **R** book. Then implement exercise 5, in section 10.6. This exercise asks you to use the **R** code below to calculate the roots of the following functions using $x_0$ as starting value for the root search algorithm:
  1. $cos(x) - x$ using $x_0 = 1, 3, 6$
  2. $log(x) - exp(-x)$ using $x_0 = 2$
  3. $x^3 - x - 3$ using $x_0 = 0$
  4. $x^3 - 7x^2 + 14x - 8$ using $x_0 = 1.1, 1.2, . . . , 1.9$
  5. $log(x) \times exp(-x)$ using $x_0 = 2$

```
newtonraphson_show <- function(ftn, x0, xmin = x0-1, xmax = x0+1) {
    # applies Newton-Raphson to find x such that ftn(x)[1] == 0
    # x0 is the starting point
    # subsequent iterations are plotted in the range [xmin, xmax]

    # plot the function
    x <- seq(xmin, xmax, (xmax - xmin)/200)
    fx <- c()
    for (i in 1:length(x)) {
        fx[i] <- ftn(x[i])[1]
    }
    plot(x, fx, type = "l", xlab = "x", ylab = "f(x)",
    main = "zero f(x) = 0", col = "blue", lwd = 2)
    lines(c(xmin, xmax), c(0, 0), col = "blue")
    # do first iteration
    xold <- x0
    f.xold <- ftn(xold)
    xnew <- xold - f.xold[1]/f.xold[2]
    lines(c(xold, xold, xnew), c(0, f.xold[1], 0), col = "red")
    # continue iterating while user types "y"
    cat("last x value", xnew, " ")
    continue <- readline("continue (y or n)? ") == "y"
    while (continue) {
        xold <- xnew;
        f.xold <- ftn(xold)
        xnew <- xold - f.xold[1]/f.xold[2]
        lines(c(xold, xold, xnew), c(0, f.xold[1], 0), col = "red")
        cat("last x value", xnew, " ")
        continue <- readline("continue (y or n)? ") == "y"
    }
    return(xnew)
}
```

## Exercise 2
-------------------------------------------------------------------------------

How do we know $\pi = 3.1415926$ (to 7 decimal places)? One way of finding $\pi$ is to solve sin(x) = 0. By definition the solutions to sin(x) = 0 are $k \times \pi$ for $k = 0, \pm 1, \pm 2, \dots$, so the root closest to 3 should be $\pi$.
  1. Use a root-finding algorithm, such as the Newton-Raphson algorithm, to find the root of sin(x) near 3. How close can you get to $\pi$? (You may use the function sin(x) provided by R.) 
  2. The function sin(x) is transcendental, which means that it cannot be written as a rational function of x. Instead we have to write it as an infinite sum: 

 $$  sin(x) = \sum_{k=0}^{\infty} {(-1) k \frac{x^{2k+1}}{(2k + 1)!}} $$
 
 (This is the infinite order Taylor expansion of sin(x) about 0.) In practice, to calculate sin(x) numerically we have to truncate this sum, so any numerical calculation of sin(x) is an approximation. In particular the function ``sin(x)`` provided by R is only an approximation of sin(x) (though a very good one). Put 
  
  $$ f_n(x)= \sum_{k=0}^{n}{(-1) k \frac{x^{2k+1}}{(2k + 1)!}} $$

  Write a function in R to calculate $f_n(x)$. Plot $f_n(x)$ over the range [0, 7] for a number of values of n, and verify that it looks like sin(x) for large n.
  3. Choose a large value of n, then find an approximation to $\pi$  by solving $f_n(x) = 0$ near 3. Can you get an approximation that is correct up to 6 decimal places? Can you think of a better way of calculating $\pi$?


## Exercise 3
-------------------------------------------------------------------------------

The bisection method can be generalised to deal with the case $f(xl)f(xr) > 0$, by broadening the bracket. That is, we reduce xl and/or increase xr , and try again. A reasonable choice for broadening the bracket is to double the width of the interval [xl,xr], that is (in pseudo-code):
```
m = (xl + xr )/2
w = xr - xl
xl = m - w
xr = m + w
```
Incorporate bracket broadening into the function bisection given in the lecture. Note that broadening is not guaranteed to find xl and xr such that $f(xl)f(xr)<= 0$, so you should include a limit on the number of times it can be tried.  Use your modified function to find a root of 

$$f(x) = (x - 1)^3 - 2x^2 + 10 - sin(x),$$

starting with xl = 1 and xr = 2.  
