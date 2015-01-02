# -----------------------------------------------------------------------------
# Exercise 1
# -----------------------------------------------------------------------------

# If we want to use the array command, we need to import it first
from pylab import *

v1 = array([1,2,3,4,5,6,7,8,7,6,5,4,3,2,1]) # vector in array form
print "v1= " + str(v1)

v2 = array([1,2,2,3,3,3,4,4,4,4,5,5,5,5]) # vector in array form
print "v2= " + str(v2)

m1 = array([[0,1,1],[1,0,1],[1,1,0]]) # matrix in multi-dimensional array form
print "m1= " + str(m1)

m2 = array([[0,2,3],[0,5,0],[7,0,0]]) # matrix in multi-dimensional array form
print "m2= " + str(m2)



# -----------------------------------------------------------------------------
# Exercise 2
# -----------------------------------------------------------------------------
final_amount=0
p=5.0 #interest rate in percent
initial_amount=1000.00 #initial amount given in Euros
n=3
final_amount=initial_amount*(1.0+p/100.0)**n
print 'The final amount is', final_amount



# -----------------------------------------------------------------------------
# Exercise 3
# -----------------------------------------------------------------------------
from math import pi
h = 5.0 # height
b = 2.0 # base
r = 1.5 # radius
#
area_parallelogram = h*b
print "The area of the parallelogram is %.3f" % area_parallelogram
#
area_square = b**2
print "The area of the square is %g" % area_square
#
area_circle = pi*r**2
print "The area of the circle is %.3f" % area_circle
#
volume_cone = 1.0/3*pi*r**2*h
print 'The volume of the cone is %.3f' % volume_cone

# -----------------------------------------------------------------------------
# Exercise 4
# -----------------------------------------------------------------------------

# -------------------------------
# [4.1]
# -------------------------------
from math import pi, sin, cos
x = pi/4.0
val_1 = sin(x)**2 + cos(x)**2
print val_1

# -------------------------------
# [4.2]
# -------------------------------
v0 = 3.0
t = 1
a = 2
s = v0*t + 1.0/2.0 * a*t**2 # Note: float(1/2) does also produce 0.0 which is incorrect.

print "s= " +str(s)     # Don't forget to transform out s into string for printing

# -------------------------------
# [4.3]
# -------------------------------
a=3.0
b=5.0
a2 = a**2
b2 = b**2
eq1_sum = a2 + 2*a*b + b2  # Don't forget times: *
eq2_sum = a2 - 2*a*b + b2
eq1_pow = (a + b)**2
eq2_pow = (a - b)**2
print 'First equation:', eq2_sum % eq2_pow
print 'Second equation:', eq1_sum % eq1_pow

# And do it again for
a=3.0
b=3.0

# Or you use vector evaluations
a=array([3.0, 3.0])
b=array([5.0, 3.0])
a2 = a**2
b2 = b**2
eq1_sum = a2 + 2*a*b + b2  # had to put * in between 2, a, and b
eq2_sum = a2 - 2*a*b + b2
eq1_pow = (a + b)**2
eq2_pow = (a - b)**2

print "eq1_sum == eq1_pow: " + str(eq1_sum == eq1_pow)
print "eq2_sum == eq2_pow: " + str(eq2_sum == eq2_pow)

# -----------------------------------------------------------------------------
# Exercise 5
# -----------------------------------------------------------------------------

a=2; b=1; c=2
from math import sqrt
q=complex(0,sqrt(15))   # q=sqrt(b*b - 4*a*c) which becomes q=sqrt(-15) = 0 + sqrt(15)*i

x_1 = (-b + q)/(2*a)   # added parentheses for precedence
x_2 = (-b - q)/(2*a)
print "a*x_1^2 + b*x_1 + c= ", a*x_1**2 + b * x_1 + c
print "a*x_2^2 + b*x_2 + c= ", a*x_2**2 + b * x_2 + c
