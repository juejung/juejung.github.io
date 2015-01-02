# Homework 5

rm(list = ls())  # Remove almost everything in the memory
library(matlab)

cat("-------------- START ----------------")
setwd("C:/Dropbox/Towson/Teaching/3_ComputationalEconomics/Lectures/Lecture5/Homework/R")
source("./myfuncs.R")

# -----------------------------------------------------------------------------
# Exercise 1
# -----------------------------------------------------------------------------
# cat('Enter a temperature in Fahrenheit: ')
# F=scan(n=1)     # read input
F = 45
cat('\nThe temperature is: ', f_celsius(F),' degrees Celsius')

# cat('Enter a temperature in Celsius: ')
# c=scan(n=1)     # read input
c = 34
cat('\nThe temperature is: ', f_fahrenheit(c),' degrees Fahrenheit')

# -----------------------------------------------------------------------------
# Exercise 2
# -----------------------------------------------------------------------------
xv=c(1,2,1,1) 
yv=c(1,1,2,1)
l=f_pathlength(xv,yv)   # calculates the length
cat('\nThe length of the path is: ', l) 

# -----------------------------------------------------------------------------
# Exercise 3
# -----------------------------------------------------------------------------
cat('\nThe built-in factorial of 6 is: ', factorial(6)) # the built-in function
cat('\nThe created function f_factorial(6): ', f_factorial(6)) 

# -----------------------------------------------------------------------------
# Exercise 4
# -----------------------------------------------------------------------------
av =c(3,5,23,45,12) #the given vector
cat('\nThe length of vector a is: ', f_vecnorm(av)) 

# -----------------------------------------------------------------------------
#Exercise 5
# -----------------------------------------------------------------------------
x = 0.70 #the given values
n = 8
cat('\nThe sum of the geometric series is: ', f_geomseries(x,n)) 
