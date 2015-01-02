# -------------------------------------------
# Optimization
# -------------------------------------------
# Define am example function for which we calculate the root, i.e. find x so that f(x) = 0

require(graphics)

rm(list=ls()) # Remove almost everything in the memor

# 1 Univariate functions

# Here we want to optimize a univariate function: f1
f1 = function(x) {
   # gamma(2,3) density
   if (x < 0) return(c(0, 0, 0))
   if (x == 0) return(c(0, 0, NaN))
   y = exp(-2*x)
   return(c(4*x^2*y, 8*x*(1-x)*y, 8*(1-2*x^2)*y))
}

f1simple = function(x) {
   # gamma(2,3) density
   if (x < 0) return(c(0))
   if (x == 0) return(c(NaN))
   y = exp(-2*x)
   return(4*x^2*y)
}

f1simpleNeg = function(x) {
   # gamma(2,3) density
   if (x < 0) return(c(0))
   if (x == 0) return(c(NaN))
   y = exp(-2*x)
   return(-(4*x^2*y))
}

# Plot the function
xmin = 0
xmax = 6
x  = seq(xmin, xmax, (xmax - xmin)/200)
fx = c() # define column vector
for (i in 1:length(x)) {
   fx[i] = f1(x[i])[1]
}
plot(x, fx, type = "l", xlab = "x", ylab = "f(x)",
     main = "zero f(x) = 0", col = "blue", lwd = 2)
lines(c(xmin, xmax), c(0, 0), col = "blue")


## 1.1 Newton's method
newton = function(f3, x0, tol = 1e-9, n.max = 100) {
   # Newton's method for optimisation, starting at x0
   # f3 is a function that given x returns the vector
   # (f(x), f'(x), f''(x)), for some f
   
   x = x0
   f3.x = f3(x)
   n = 0
   while ((abs(f3.x[2]) > tol) & (n < n.max)) {
      x = x - f3.x[2]/f3.x[3]
      f3.x = f3(x)
      n = n + 1
   }
   if (n == n.max) {
      cat('newton failed to converge\n')
   } else {
      return(x)
   }
}

## 1.2 Golden section method
gsection = function(ftn, x.l, x.r, x.m, tol = 1e-9) {
   # applies the golden-section algorithm to maximise ftn
   # we assume that ftn is a function of a single variable
   # and that x.l < x.m < x.r and ftn(x.l), ftn(x.r) <= ftn(x.m)
   #
   # the algorithm iteratively refines x.l, x.r, and x.m and terminates
   # when x.r - x.l <= tol, then returns x.m
   
   # golden ratio plus one
   gr1 = 1 + (1 + sqrt(5))/2
   
   # successively refine x.l, x.r, and x.m
   f.l = ftn(x.l)
   f.r = ftn(x.r)
   f.m = ftn(x.m)
   while ((x.r - x.l) > tol) {
      if ((x.r - x.m) > (x.m - x.l)) {
         y = x.m + (x.r - x.m)/gr1
         f.y = ftn(y)
         if (f.y >= f.m) {
            x.l = x.m
            f.l = f.m
            x.m = y
            f.m = f.y
         } else {
            x.r = y
            f.r = f.y
         }
      } else {
         y = x.m - (x.m - x.l)/gr1
         f.y = ftn(y)
         if (f.y >= f.m) {
            x.r = x.m
            f.r = f.m
            x.m = y
            f.m = f.y
         } else {
            x.l = y
            f.l = f.y
         }
      }
   }
   return(x.m)
}

## 1.3 Built in 'optimize' function


# ------------------------
# Maximize function: f1
# ------------------------

newton(f1, 0.25)
newton(f1, 0.50)
newton(f1, 0.75)
newton(f1, 1.75)

gsection(f1simple, 0.1, 0.25, 1.3)
gsection(f1simple, 0.25, 0.5, 1.7)
gsection(f1simple, 0.6, 0.75, 1.8)
gsection(f1simple, 0.0, 2.75, 5.0)

optimize(f1simple, c(0.1,  1.3), maximum = TRUE)
optimize(f1simple, c(0.25, 1.7), maximum = TRUE)
optimize(f1simple, c(0.6,  1.8), maximum = TRUE)
optimize(f1simple, c(0.0,  5.0), maximum = TRUE)


# -----------------------------------------------------------------
# 2 Multivariate optimization
# -----------------------------------------------------------------

# Here we want to optimize the following functions: f3, f4

# -------------------------------------------------
# Function f3 
# -------------------------------------------------
f3simple = function(x) {
   a = x[1]^2/2 - x[2]^2/4
   b = 2*x[1] - exp(x[2])
   f = sin(a)*cos(b)
   return(f)
}

f3simpleNeg = function(x) {
   a = x[1]^2/2 - x[2]^2/4
   b = 2*x[1] - exp(x[2])
   f = -(sin(a)*cos(b))
   return(f)
}

f3 = function(x) {
   a = x[1]^2/2 - x[2]^2/4
   b = 2*x[1] - exp(x[2])
   f = sin(a)*cos(b)
   f1 = cos(a)*cos(b)*x[1] - sin(a)*sin(b)*2
   f2 = -cos(a)*cos(b)*x[2]/2 + sin(a)*sin(b)*exp(x[2])
   f11 = -sin(a)*cos(b)*(4 + x[1]^2) + cos(a)*cos(b) -
      cos(a)*sin(b)*4*x[1]
   f12 = sin(a)*cos(b)*(x[1]*x[2]/2 + 2*exp(x[2])) +
      cos(a)*sin(b)*(x[1]*exp(x[2]) + x[2])
   f22 = -sin(a)*cos(b)*(x[2]^2/4 + exp(2*x[2])) - cos(a)*cos(b)/2 -
      cos(a)*sin(b)*x[2]*exp(x[2]) + sin(a)*sin(b)*exp(x[2])
   return(list(f, c(f1, f2), matrix(c(f11, f12, f12, f22), 2, 2)))
} # Function f3 returns: f(x), f'(x), and f''(x)

## Plot function f3
library("lattice")
x = c()
y = c()
z = c()
i = 1  ## Make data for wireframe command
for (x0 in seq(1, 10, 1)) {
   for (y0 in seq(1, 10, 1)) {
      x[i] = x0
      y[i] = y0
      z[i] =  f3simple(c(x[i],y[i]))
      i = i + 1  # data counter
   }
}
wireData = data.frame(x=x,y=y,z=z)
wireframe(z ~ x*y, main="3D Wireframe Plot: f3", xlab = "x", ylab = "y",
          data=wireData)


# -------------------------------------------------
# Function f4 
# -------------------------------------------------
f4simple = function(x) {   ## Rosenbrock Banana function
   a = x[1]^2/2-x[2]^2/4
   b = 2*x[1] - exp(x[2])
   f = sin(a)*cos(b)
   return(f)
}

f4simpleNeg = function(x) {   ## Rosenbrock Banana function
   a = x[1]^2/2-x[2]^2/4
   b = 2*x[1] - exp(x[2])
   f = -sin(a)*cos(b)
   return(f)
}

Dfx = deriv(z ~ sin(x^2/2 - y^2/4)*cos(2*x - exp(y)), c('x','y'), func=TRUE, hessian=TRUE)
f4 = function(x) {
   Dfx = Df(x[1], x[2])
   f = Dfx[1]
   gradf = attr(Dfx, 'gradient')[1,]
   hessf = attr(Dfx, 'hessian')[1,,]
   return(list(f, gradf, hessf))
}

## Plot function f4
x = c()
y = c()
z = c()
i = 1 ## Make data for wireframe command
for (x0 in seq(0, 3, .1)) {
   for (y0 in seq(0, 3, .1)) {
      x[i] = x0
      y[i] = y0
      z[i] =  f4simple(c(x[i],y[i]))
      i = i + 1  # data counter
   }
}
wireData = data.frame(x=x,y=y,z=z)
wireframe(z ~ x*y, main="3D Wireframe Plot: f4", xlab = "x", ylab = "y",
          data=wireData)



# ------------------------------------------------------
# Methods
# ------------------------------------------------------


# ## -----------------------------------------------------
# ## 2.1 Steepest ascent
# ## -----------------------------------------------------
# ascent = function(f, grad.f, x0, tol = 1e-9, n.max = 100) {
#    # steepest ascent algorithm
#    # find a local max of f starting at x0
#    # function grad.f is the gradient of f
#    
#    x = x0
#    x.old = x
#    x = line.search(f, x, grad.f(x))
#    n = 1
#    while ((f(x) - f(x.old) > tol) & (n < n.max)) {
#       x.old = x
#       x = line.search(f, x, grad.f(x))
#       n = n + 1
#    }
#    return(x)
# }
# 
# line.search = function(f, x, y, tol = 1e-9, a.max = 2^5) {
#    # f is a real function that takes a vector of length d
#    # x and y are vectors of length d
#    # line.search uses gsection to find a >= 0 such that
#    #   g(a) = f(x + a*y) has a local maximum at a,
#    #   within a tolerance of tol
#    # if no local max is found then we use 0 or a.max for a
#    # the value returned is x + a*y
#    
#    if (sum(abs(y)) == 0) return(x) # g(a) constant
#    
#    g = function(a) return(f(x + a*y))
#    
#    # find a triple a.l < a.m < a.r such that
#    # g(a.l) <= g(a.m) and g(a.m) >= g(a.r)
#    # a.l
#    a.l = 0
#    g.l = g(a.l)
#    # a.m
#    a.m = 1
#    g.m = g(a.m)
#    while ((g.m < g.l) & (a.m > tol)) {
#       a.m = a.m/2
#       g.m = g(a.m)
#    }
#    # if a suitable a.m was not found then use 0 for a
#    if ((a.m <= tol) & (g.m < g.l)) return(x)
#    # a.r
#    a.r = 2*a.m
#    g.r = g(a.r)
#    while ((g.m < g.r) & (a.r < a.max)) {
#       a.m = a.r
#       g.m = g.r
#       a.r = 2*a.m
#       g.r = g(a.r)
#    }
#    # if a suitable a.r was not found then use a.max for a
#    if ((a.r >= a.max) & (g.m < g.r)) return(x + a.max*y)
#    
#    # apply golden-section algorithm to g to find a
#    a = gsection(g, a.l, a.r, a.m)
#    return(x + a*y)
# }

## -----------------------------------------------------
## 2.2 Newton
## -----------------------------------------------------
newtonMult = function(f3, x0, tol = 1e-9, n.max = 100) {
   # Newton's method for optimisation, starting at x0
   # f3 is a function that given x returns the list
   # {f(x), grad f(x), Hessian f(x)}, for some f
   
   x = x0
   f3.x = f3(x)
   n = 0
   while ((max(abs(f3.x[[2]])) > tol) & (n < n.max)) {
      x = x - solve(f3.x[[3]], f3.x[[2]])
      f3.x = f3(x)
      n = n + 1
   }
   if (n == n.max) {
      cat('newton failed to converge\n')
   } else {
      return(x)
   }
}

## -----------------------------------------------------
## 2.3 optim()
## -----------------------------------------------------

## -----------------------------------------------------
## Maximize
## -----------------------------------------------------

## f3
for (x0 in seq(1.4, 1.6, 0.1)) {
   for (y0 in seq(0.4, 0.6, 0.1)) {
      cat("Newton: f3", c(x0,y0), '-->', newtonMult(f3, c(x0,y0)), '\n') # This algorithm requires f(x), f'(x), and f''(x)
      cat("Optim:  f3", c(x0,y0), '-->', optim(c(x0,y0), f3simpleNeg)[[1]], '\n')
      cat(" ----------------------------------------- \n")
   }
}

cat(" ----------------------------------------- \n")
cat("  \n")
## f4
for (x0 in seq(0.0, 0.5, 0.1)) {
   for (y0 in seq(0.0, 0.5, 0.1)) {
      cat("Newton: f3", c(x0,y0), '-->', newtonMult(f3, c(x0,y0)), '\n') # This algorithm requires f(x), f'(x), and f''(x)
      cat("Optim:  f4", c(x0,y0), '-->', optim(c(x0,y0), f4simpleNeg)[[1]], '\n')
      cat(" ----------------------------------------- \n")
   }
}


