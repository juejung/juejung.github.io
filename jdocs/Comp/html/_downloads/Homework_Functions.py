# Homework 5
# ------------------------------------------------------------------------------
import time # Imports system time module to time your script
import numpy as np
import math as m
import matplotlib.pyplot as plt


# User written functions, script stored in same directory
import myfuncs as mf

# If you work with user written functions that are saved in separate script
# files you need to make sure that you are always using the latest version of
# the functions. When developing your programs I would recommend you always put
# these two lines on top of your codes to ensure that it always reloads the
# latest version of your function definitions. Once the functions are debugged
# and correct, you can comment the next two lines out.
import imp
imp.reload(mf)

tic = time.clock()              # Start timer
plt.close('all')  # close all open figures

#------------------------------------------------------------------------------
# Exercise 1
#------------------------------------------------------------------------------
print('-----------------------------------------')
print('Exercise 1')
print('-----------------------------------------')
#print 'Enter a temperature in Fahrenheit: '
#F=float(raw_input()) #grabs the user input for the conversion
F = 45.0
for F in range(60, 105, 5):
    c = mf.f_fahrenheit_to_celsius(F) # converts the value
    print('{:.3f} Fahrenheit equals {:.3f} degrees Celsius'.format(F, c))
    F1 = mf.f_celsius_to_fahrenheit(c) # converts the value back
    print('{:.3f} Celsius equals {:.3f} degrees Fahrenheit'.format(c, F))
    print(' ')

#------------------------------------------------------------------------------
# Exercise 2
#------------------------------------------------------------------------------
print('Exercise 2')
print('-----------------------------------------')
# Calculate factorial
print('The factorial of 6 is: {}'.format(mf.f_factorial(6)))
# Built-in factorial for comparison
print('The factorial of 6 is: {}'.format(m.factorial(6)))

#------------------------------------------------------------------------------
# Exercise 3
#------------------------------------------------------------------------------
print('-----------------------------------------')
print('Exercise 2')
print('-----------------------------------------')
av = np.array([3,5,23,45,12])
print('The length of the given vector is: {}'.format(mf.f_vector_norm(av)))


#------------------------------------------------------------------------------
# Exercise 4
#------------------------------------------------------------------------------
print('-----------------------------------------')
print('Exercise 4')
print('-----------------------------------------')
xv = np.linspace(-3, 5, 100)
yv = np.zeros(len(xv))
for i, x in enumerate(xv):
    yv[i] = mf.f_comp_func(x)

fig, ax = plt.subplots()
ax.plot(xv, yv, 'b.')
ax.set_title('Excercise 4')
plt.show()

#------------------------------------------------------------------------------
# Exercise 5
#------------------------------------------------------------------------------
print('-----------------------------------------')
print('Exercise 5')
print('-----------------------------------------')
xv = np.array([1,2,1,1]) # preset the given arrays
yv = np.array([1,1,2,1])
print('The path length is: {}'.format(mf.f_path_length(xv, yv)))
