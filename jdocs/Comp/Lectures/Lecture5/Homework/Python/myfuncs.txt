# -*- coding: utf-8 -*-
"""
Created on Sun Oct 07 12:20:25 2012

@author: JJung
"""
#Functions for homework 5
from pylab import * 

#------------------------------------------------------------------------------
# Exercise 1
#------------------------------------------------------------------------------
def f_celsius(f):
    c = (5.0/9.0)*(f-32.0) # the conversion equation
    return c # return the value
    
def f_fahrenheit(c):    
    f = c*(9.0/5.0)+32.0 # the conversion equation
    return f # return the value
    
#------------------------------------------------------------------------------
# Exercise 2
#------------------------------------------------------------------------------
def f_pathlength(xv,yv):
    # requires the input of two vectors: xv, yv
    L = 0
    i = 1
    while i < len(xv): #cycle through the arrays
        L = L+ math.sqrt(((xv[i]-xv[i-1])**2)+((yv[i]-yv[i-1])**2)) #calculate the distance of each part of path
        i= i+1  # the update for the loop
    return L    # return the value
    
#------------------------------------------------------------------------------
# Exercise 3
#------------------------------------------------------------------------------
def f_factorial(n):
    f=1 #variable to store factorial
    if n==0: f=1  
    elif n==1: f=1
    elif n>1:
        for i in range(1,n+1):
            f=f*i
    return f # return value
    
#------------------------------------------------------------------------------
#Exercise 4
#------------------------------------------------------------------------------
def f_vecnorm(xv):
    return math.sqrt(sum(xv**2)) # returns the square root of the sum of squared elements
    
#------------------------------------------------------------------------------  
# Exercise 5 
#------------------------------------------------------------------------------
# h(x,n)=1+x+x^2+x^3+...+x^n # the equation for reference
def f_geomseries(x,n):
    s = 0.0
    for i in range(n+1):
        s=s+x**i  # adds up the series as in the formula
    return s    
    