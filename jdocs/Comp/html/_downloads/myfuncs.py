# -*- coding: utf-8 -*-
# Functions for homework 5
# ------------------------------------------------------------------------------

import numpy as np
import math as m

#------------------------------------------------------------------------------
# Exercise 1
#------------------------------------------------------------------------------
def f_fahrenheit_to_celsius(f):
    """Converts Fahrenheit into Celsius."""
    return (5.0/9.0)*(f-32.0) # the conversion equation

def f_celsius_to_fahrenheit(c):
    """Converts Celsius into Fahrenheit."""
    return c*(9.0/5.0)+32.0 # the conversion equation

#------------------------------------------------------------------------------
# Exercise 2
#------------------------------------------------------------------------------
def f_factorial(n):
    """Calculates the factorial of input integer number n."""
    if n<0:
        print('Negative input not allowed')
        return
    if n==0 | n==1:
        return 1
    else:
        f = 1 # variable to store factorial
        for i in range(1, n+1):
            f = f*i
        return f # return value

#------------------------------------------------------------------------------
# Exercise 3
#------------------------------------------------------------------------------
# Loop version
def f_vector_norm(xv):
    """Calculates the lenght of a vector or the vector norm."""
    jsum = 0
    for x in xv:
        jsum = jsum + x**2

    return np.sqrt(jsum)


# No loop version
def f_vector_norm_B(xv):
    """Calculates the lenght of a vector or the vector norm."""
    return np.sqrt(np.sum(xv**2))


#------------------------------------------------------------------------------
# Exercise 4
#------------------------------------------------------------------------------
def f_comp_func(x):
    """Returns the values of a composite function."""
    if x < -1:
        return x**2
    elif (x >= -1) & (x < 0):
        return np.abs(x)
    elif (x >= 0) & (x < 0.5):
        return -1
    elif (x >= 0.5) & (x < 2):
        return x**2
    else:
        return np.sqrt(x)

#------------------------------------------------------------------------------
# Exercise 5
#------------------------------------------------------------------------------
def f_path_length(xv, yv):
    """Calculates the length of the path between points (x0, y0) to (xn, yn).
    Requires the input of two vectors: xv, yv"""

    L = 0
    i = 1
    while i < len(xv): #cycle through the arrays
        # Calculate the distance of each part of path
        L = L + m.sqrt(((xv[i]-xv[i-1])**2) + ((yv[i]-yv[i-1])**2))
        i += 1  # update the counter variable
    return L    # return the path length value

#------------------------------------------------------------------------------
# Exercise 6
#------------------------------------------------------------------------------
class Student(object):
    def __init__(self, firstname = 'J', lastname = 'J', gender = 'na', \
                 status= 'freshman', gpa = 0):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.status = status
        self.gpa = gpa

    def showMyself(self):
        print('--------------------------------------')
        print('First name: {}'.format(self.firstname))
        print('Last name:  {}'.format(self.lastname))
        print('Gender:     {}'.format(self.gender))
        print('Status:     {}'.format(self.status))
        print('GPA:        {}'.format(self.gpa))
        print('--------------------------------------')

    def study_time(self, studytime = 0.0):
        self.gpa = self.gpa + m.log(studytime/60)
        # Check whether it's too large
        if self.gpa > 4:
            self.gpa = 4

        return(self.gpa)


