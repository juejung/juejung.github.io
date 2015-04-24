# Homework_Root.py
# ------------------------------------------------------------------------------
import numpy as np
import math as m
import matplotlib.pyplot as plt

print('--------------------------------------------------------------------')
print('Problem 1')
print('--------------------------------------------------------------------')

# Define the functions returning the function value fx at x and the value of the
# first derivative d_fx at x.
def f1(x):
    fx = np.log(x) - np.exp(-x)
    d_fx = 1/x + np.exp(-x)
    return np.array([fx, d_fx])

def f2(x):
    fx = (x**3) - x - 3
    d_fx = 3*x**2 - 1
    return np.array([fx, d_fx])

def f3(x):
    fx = (x**3) - (7)*(x**2) + 14*x - 8
    d_fx = 3*x**2 - 14*x + 14
    return np.array([fx, d_fx])

def f4(x):
    fx = np.log(x) * np.exp(-x)
    d_fx =  (np.exp(-x))/x - (np.log(x) * np.exp(-x))
    return np.array([fx, d_fx])

# Newton Raphson from the lecture notes)
def newtonraphson(ftn, x0, tol = 1e-9, maxiter = 100):
    # Newton_Raphson algorithm for solving ftn(x)[1] == 0
    # we assume that ftn is a function of a single
    # variable that returns the function value and
    # the first derivative as a vector of length 2
    #
    # x0 is the initial guess at the root
    # the algorithm terminates when the function
    # value is within distance tol of 0, or the
    # number of iterations exceeds maxiter
    x = x0
    fx = ftn(x)
    jiter =  0

    # Continue iterating until stopping conditions are met
    while ((abs(fx[0]) > tol) and (jiter < maxiter)):
        x = x - fx[0]/fx[1]
        fx = ftn(x)
        jiter =  jiter + 1
        print("At iteration: {} the value of x is {}:" \
          .format(jiter, x))
    # Output depends on success of algorithm
    if (abs(fx[0]) > tol):
        print("Algorithm failed to converge")
        return(0)
    else:
        print("fx = ", fx[0])
        print("Algorithm converged")
        return(x)
#end

# Call the newton raphson algorithm
newtonraphson(f1, 2)
print("--------------------------")
newtonraphson(f2, 0)
print("--------------------------")

# solve function f3 using different starting values x0 each time
x = 1
for i in range(9):
    newtonraphson(f3, x)
    x = x + .1
    print("-----------------------------")

# Solve last function f4 for the root
newtonraphson(f4, 2)

print('--------------------------------------------------------------------')
print('Problem 2')
print('--------------------------------------------------------------------')

def bisection(ftn, xl, xr, tol = 1e-9):
    # applies the bisection algorithm to find x
    # such that ftn(x) == 0
    # we assume that ftn is a function of a single variable
    #
    # x.l and x.r must bracket the fixed point, that is
    # x.l < x.r and ftn(x.l) * ftn(x.r) < 0
    #
    # the algorithm iteratively refines
    # x.l and x.r and terminates when
    # x.r - x.l <= tol

    # check inputs
    if (xl >= xr):
        print("error: xl >= xr")
        return None

    fl = ftn(xl)
    fr = ftn(xr)

    if (fl == 0):
        return(xl)
    elif (fr == 0):
        return(xr)
    elif (fl * fr > 0):
        print("bisection error: ftn(xl) * ftn(xr) > 0")
        return None

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
        print("at iteration: {} the root lies between {} and {}" \
            .format(n, xl, xr))

    # Return (approximate) root
    return ((xl + xr)/2.0)
#end

# Define the sin-function and its first derivative
def f5(x):
    fx = np.sin(x)
    d_dx = np.cos(x)
    return np.array([fx, d_dx])

# Call the root finding algorithm with a starting value of x0 = 3
newtonraphson(f5, 3)

# Define the sin-function using an 'infinite' sum
def f_mySin(x):
    n = 20
    fn = 0
    for k in range(n):
        fn += (-1)**k * x**(2*k+1) / m.factorial(2 * k + 1)
    return fn

# Calculate the sin-function using an 'infinite' sum
xv = np.linspace(0, 7, 200)
yv = np.linspace(0, 7, 200)
for i, x  in enumerate(xv):
    yv[i] = f_mySin(x)

## Plot sin function to check whether everything is OK
#fig, ax = plt.subplots()
#ax.plot(xv, yv, label='sin(x)')
#ax.set_title('sin(x)')
#plt.show()

# Calculate the root of this sine-function using x0=3
bisection(f_mySin, 3, 3.5)

print('--------------------------------------------------------------------')
print('Problem 3')
print('--------------------------------------------------------------------')

def bisectionExpandable(ftn, xl, xr, tol = 1e-9):
    # applies the bisection algorithm to find x
    # such that ftn(x) == 0
    # we assume that ftn is a function of a single variable
    #
    # x.l and x.r must bracket the fixed point, that is
    # x.l < x.r and ftn(x.l) * ftn(x.r) < 0
    #
    # the algorithm iteratively refines
    # x.l and x.r and terminates when
    # x.r - x.l <= tol

    # check inputs
    if (xl >= xr):
        print("error: xl >= xr")
        return None

    fl = ftn(xl)
    fr = ftn(xr)

    if (fl == 0):
        return(xl)
    elif (fr == 0):
        return(xr)
    elif (fl * fr > 0):
        # Catch the case where the root is NOT inside the starting brackets
        count = 0
        while (fl * fr > 0)  and count < 10:
            # Print statement telling user how often brackets get widened
            print('{} adjustment of  brackets'.format(count+1))
            m = (xl + xr )/2  # find midpoint
            w = xr - xl  # find range between left and right bracket
            xl = m - w  # expand the left bracket
            xr = m + w  # expand the right bracket
            fl = ftn(xl) # calculate starting function values again at left
            fr = ftn(xr) # calculate starting function values again at right
            # Increment loop counter so that expanding doesn run forever
            count += 1

    # Now that root is inside brackets, successively refine x.l and x.r
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
        print("at iteration: {} the root lies between {} and {}" \
            .format(n, xl, xr))
    # Return (approximate) root
    return (xl + xr)/2.0



# Define the function (it actually has multiple roots).
# Check the graph
def f_6(x):
    y = ((x-1)**3) - (2*(x**2)) + 10 - np.sin(x)
    return y

# Plot function to check whether is has a root
xv = np.linspace(-1.1, 4, 200)
yv = np.zeros(len(xv))
flatv = np.zeros(len(xv))
for i, x  in enumerate(xv):
    yv[i] = f_6(x)

fig, ax = plt.subplots()
ax.plot(xv, flatv, 'r', xv, yv)
ax.set_title('((x-1)**3) - (2*(x**2)) + 10 - np.sin(x))')
plt.show()

# Call the bisection with xl = 1 and xr = 2
# Try with standard bisection first, which obviously doesn't work
xl = 1
xr = 2
bisection(f_6, xl, xr)

# Now use the expandable version to find root1
xl = 1
xr = 2
bisectionExpandable(f_6, xl, xr)

# Now use the expandable version and different starting vals to find root2
xl = 2
xr = 3
bisectionExpandable(f_6, xl, xr)


# Now use the expandable version and different starting vals to find root3
xl = 3
xr = 4
bisectionExpandable(f_6, xl, xr)
