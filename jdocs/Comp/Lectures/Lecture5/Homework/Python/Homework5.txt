# Homework 5

import time                     # Imports system time module to time your script
from pylab import *             # Imports numpy, scipy, and matplotlib etc.
import math 
import myfuncs as mf
tic = time.clock()              # Start timer
close('all')  # close all open figures

#------------------------------------------------------------------------------
# Exercise 1
#------------------------------------------------------------------------------
#print 'Enter a temperature in Fahrenheit: '
#F=float(raw_input()) #grabs the user input for the conversion
F = 45.0
c=mf.f_celsius(F) #converts the value
print 'The temperature is: ', c,' degrees Celsius' # prints the final value

#print 'Enter a temperature in Celsius: '
#c=float(raw_input()) #grabs the user input for the conversion
c = 34.0
F=mf.f_fahrenheit(c) #converts the value
print 'The temperature is: ', F,' degrees Fahrenheit' # prints the final value

#------------------------------------------------------------------------------
# Exercise 2
#------------------------------------------------------------------------------
xv=array([1,2,1,1]) # preset the given arrays
yv=array([1,1,2,1])
print 'The path length is: ', str(mf.f_pathlength(xv,yv))  #prints final result

#------------------------------------------------------------------------------
# Exercise 3
#------------------------------------------------------------------------------
print 'The factorial of 6 is: ' + str(math.factorial(6)) # built-in factorial for comparison
print 'The factorial of 6 is: ' + str(mf.f_factorial(6))  

#------------------------------------------------------------------------------
# Exercise 4
#------------------------------------------------------------------------------
a=array([3,5,23,45,12]) # given array/vector
print 'The length of the given vector is: ' + str(mf.f_vecnorm(a)) #prints final result

#------------------------------------------------------------------------------
# Exercise 5
#------------------------------------------------------------------------------
#x=1 #for the test of the function
x=0.70 #the given values to use for the problem
n=8
print 'The sum of the geomentric series is: ' + str(mf.f_geomseries(x,n))  