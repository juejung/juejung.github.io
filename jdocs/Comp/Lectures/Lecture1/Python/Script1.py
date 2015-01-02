# -*- coding: utf-8 -*-
"""
# =====================================================================
#
# Scriptfile Lecture 1
# -------------------------
# Computational Economics
# (c) Juergen Jung, 2012
#
# =====================================================================

"""
import math
from pylab import *
from numpy import *
from scipy import *

# 1 --------------
x=2
y=3
print x + y
print x**y
print math.sqrt(x)

# 2 --------------
x = [1,3,4,9]
y = [9.2, 0.3, 3.2, 2.8]
year  = arange(2000,2003,1)         # arange(from, to, stepsize)
somev = linspace(2000,2003,10)      # linspace(from, to, nr. of steps)
names = ["Tom", "Dick", "Harry", "Patrick"]  
print "x[0]= " + str(x[0])
print "x[1]= " + str(x[1])
print "x[2]= " + str(x[2])
print "names[1]= " + str(names[1])
print "names[3]= " + str(names[3])


# 3 --------------
# Element-by-element operations
x1 = array([1,3,4,9])
x2 = array([2,5,6,3])
print "x1+x2= " + str(x1+x2)
print "x1*x2= " + str(x1*x2)


# 4 ---------------
a = array([[2,3],[4,5]])
b = array([[2,6],[1,3]])

print "a*b= " + str(a*b)
print "a-b= " + str(a-b)


# 5 --------------
a = zeros((3,5),float)
b = ones((4,3),float)
c = identity(3)

print "a= " + str(a) 
print "b= " + str(b)
print "c= " + str(c)
