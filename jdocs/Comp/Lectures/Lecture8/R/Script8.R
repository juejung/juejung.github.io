# -------------------------------------------
# Root finding
# -------------------------------------------

rm(list=ls()) # Remove almost everything in the memor

# Define am example function for which we calculate the root, i.e. find x so that f(x) = 0
func = function(x) {
   fx = log(x) - exp(-x)   # function: f(x)
   return (fx)               # return function value
}

# Define am example function for which we calculate the root, i.e. find x so that f(x) = 0
func1 = function(x) {
   fx = log(x) - exp(-x)   # function: f(x)
   dfx= 1/x + exp(-x)      # derivative of function: f'(x)
   return (c(fx, dfx))     # return function value and value of derivative
}

# Plot the function
xmin = 1
xmax = 6
x  = seq(xmin, xmax, (xmax - xmin)/200)
fx = c() # define column vector
for (i in 1:length(x)) {
   fx[i] = func1(x[i])[1]
}
plot(x, fx, type = "l", xlab = "x", ylab = "f(x)",
     main = "zero f(x) = 0", col = "blue", lwd = 2)
lines(c(xmin, xmax), c(0, 0), col = "blue")

# 2 Newton-Raphson

newtonraphson = function(ftn, x0, tol = 1e-9, max.iter = 100) {
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
   while ((abs(fx[1]) > tol) && (iter < max.iter)) {
      x = x - fx[1]/fx[2]
      fx = ftn(x)
      iter =  iter + 1
      cat("At iteration", iter, "value of x is:", x, "\n")
   }
   
   # output depends on success of algorithm
   if (abs(fx[1]) > tol) {
      cat("Algorithm failed to converge\n")
      return(NULL)
   } else {
      cat("Algorithm converged\n")
      return(x)
   }
}



# Calculate the root of the function calling 'newtonraphson'
newtonraphson(func1, 2)


# 3 Secant method
secant = function(ftn, x0, x1, tol = 1e-9, max.iter = 100) {
   # Secant algorithm for solving ftn(x) == 0
   # we assume that ftn is a function of a single variable that returns
   # the function value
   #
   # x0 and x1 are the initial guesses around the root
   # the algorithm terminates when the function value is within distance
   # tol of 0, or the number of iterations exceeds max.iter
   
   # initialize
   fx0 = ftn(x0)
   fx1 = ftn(x1)
   iter =  0
   
   # continue iterating until stopping conditions are met
   while ((abs(fx1) > tol) && (iter < max.iter)) {
      x  = x1 - fx1 * (x1-x0)/(fx1 - fx0) 
      fx0 = ftn(x1)
      fx1 = ftn(x)
      x0  = x1
      x1  = x
      
      iter =  iter + 1
      cat("At iteration", iter, "value of x is:", x, "\n")
   }
   
   # output depends on success of algorithm
   if (abs(fx1) > tol) {
      cat("Algorithm failed to converge\n")
      return(NULL)
   } else {
      cat("Algorithm converged\n")
      return(x)
   }
}

# Calculate the root of the function calling 'secant'
secant(func, 1,2)

# 4 Bisection
# program spuRs/resources/scripts/bisection.r
# loadable spuRs function

bisection = function(ftn, x.l, x.r, tol = 1e-9) {
   # applies the bisection algorithm to find x such that ftn(x) == 0
   # we assume that ftn is a function of a single variable
   #
   # x.l and x.r must bracket the fixed point, that is
   # x.l < x.r and ftn(x.l) * ftn(x.r) < 0
   #
   # the algorithm iteratively refines x.l and x.r and terminates when
   # x.r - x.l <= tol
   
   # check inputs
   if (x.l >= x.r) {
      cat("error: x.l >= x.r \n")
      return(NULL)
   } 
   f.l = ftn(x.l)
   f.r = ftn(x.r)
   if (f.l == 0) {
      return(x.l)
   } else if (f.r == 0) {
      return(x.r)
   } else if (f.l * f.r > 0) {
      cat("error: ftn(x.l) * ftn(x.r) > 0 \n")
      return(NULL)
   }
   
   # successively refine x.l and x.r
   n = 0
   while ((x.r - x.l) > tol) {
      x.m = (x.l + x.r)/2
      f.m = ftn(x.m)
      if (f.m == 0) {
         return(x.m)
      } else if (f.l * f.m < 0) {
         x.r = x.m
         f.r = f.m
      } else {
         x.l = x.m
         f.l = f.m
      }
      n = n + 1
      cat("at iteration", n, "the root lies between", x.l, "and", x.r, "\n")
   }
   
   # return (approximate) root
   return((x.l + x.r)/2)
}

# Calculate the root of the function calling 'bisection'
bisection(func, 1,2)

# 5 Using built in unit-root function
uniroot(func,lower = 0, upper = 2)