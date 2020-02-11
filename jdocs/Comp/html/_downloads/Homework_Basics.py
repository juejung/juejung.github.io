# Homework 1: Basic steps in Python
# ==============================================================================
import math as m
print("-------------------------")
print("Start")
print("-------------------------")
print()
# -----------------------------------------------------------------------------
# Exercise 1
# -----------------------------------------------------------------------------
print("EXERCISE 1")
print("-------------------------")
listA = [1,2,3,4,5,6,7,8,7,6,5,4,3,2,1]
listB = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
print(listA[2])
print(listB[4:8])
result = listB[7] + listA[2]
print("The 8th element is:", result)
print()

# -----------------------------------------------------------------------------
# Exercise 2
# -----------------------------------------------------------------------------
print("EXERCISE 2")
print("-------------------------")
r = 5
initialA = 1000
n = 3
finalA = initialA *  (1 + r/100) ** n
print("After three years you will have ${:4.3f}".format(finalA))
print()

# -----------------------------------------------------------------------------
# Exercise 3
# -----------------------------------------------------------------------------
print("EXERCISE 3")
print("-------------------------")
import math as m
h = 5.0 # height
b = 2.0 # base
r = 1.5 # radius
#
area_parallelogram = h*b
print("The area of the parallelogram is {:.3f}".format(area_parallelogram))
#
area_square = b**2
print("The area of the square is {:.3f}".format(area_square))
#
area_circle = m.pi*r**2
print ("The area of the circle is {:.3f}".format(area_circle))
#
volume_cone = 1.0/3*m.pi*r**2*h
print("The volume of the cone is {:.3f}".format(volume_cone))
print()

# -----------------------------------------------------------------------------
# Exercise 4
# -----------------------------------------------------------------------------
print("EXERCISE 4")
print("-------------------------")
import math as m
x = m.pi/4
val = (m.sin(x))**2 + (m.cos(x) ) **2
print("The value of variable var = {}".format(val))

v0 = 3 #m/s
t = 1 #s
a = 2 #m/s**2
s = v0*t + 0.5 * a*t**2
print("The values of s is = {}".format(s))

# The next code chunk verifies these equations:
# (a+b)2(a−b)2==a2+2ab+b2a2−2ab+b2
# Code:
a = 3
b = 5
a2 = a**2
b2 = b**2
eq1_sum = a2 + 2*a*b + b2
eq2_sum = a2 - 2*a*b + b2
eq1_pow = (a + b)**2
eq2_pow = (a - b)**2
print("First equation: {:.3f} = {:.3f}".format(eq2_sum, eq2_sum))
print("Second equation: {:.3f} = {:.3f}".format(eq2_pow, eq2_pow))
print()

# -----------------------------------------------------------------------------
# Exercise 5
# -----------------------------------------------------------------------------
print("EXERCISE 5")
print("-------------------------")
import math as m

print('First set of variables:')
a = 2; b = 1; c = 2
r = b**2 - 4*a*c
if r < 0:
    print("There are no real roots.")
else:
    q = m.sqrt(r)
    x1 = (-b + q)/(2*a)
    x2 = (-b - q)/(2*a)
    print("The real roots of the quadratic equation are: {} and {}".format(x1, x2))

print()
print('Second set of variables:')
a = 2; b = 5; c = 1
r = b**2 - 4*a*c
if r < 0:
    print("There are no real roots.")
else:
    q = m.sqrt(r)
    x1 = (-b + q)/(2*a)
    x2 = (-b - q)/(2*a)
    print("The real roots of the quadratic equation are: {:.4f} and {:.4f}".format(x1, x2))

print()
print("-----   END!   -----")
