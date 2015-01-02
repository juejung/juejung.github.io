#-------------------------------------------------------------------------------
# Author: Juergen JUng
# Date  : 22 July 2012
#-------------------------------------------------------------------------------
rm(list=ls()) # Remove almost everything in the memory

print("-------------- START ----------------")
setwd("C:/Dropbox/Towson/Teaching/3_ComputationalEconomics/Lectures/Lecture5/R")

print(paste("Today is",format(Sys.time(), "%a %b %d %X %Y")),quote=FALSE)   #Printing today's date & current time
print(paste("My current working directory is:",getwd()),quote=FALSE)        #Printing the current R working directory

tic()          # Start timer
# ------------------------------------------------------------------------------

# --------------------------------------------
# 1 Use simple user defined functions
# --------------------------------------------

source("./myFunctions.R")

hw1(2.6,4.0)
hw2(2.5,5.6)


# --------------------------------------------
# 2 Advanced Graphing using loops and functions
# --------------------------------------------

## 2.1 Graphing functions with two input arguments z = f(x,y)

library("lattice")

x = seq(1, 10, by=1)
y = seq(1, 10, by=1)
n = length(x)

f = matrix(0,n,n)   # Define matrix size nxn with zero entries
for (i in 1:n) {
   for (j in 1:n) {
      f[i,j] = sin(y[j]*x[i])
   }
}

# This plots the 3-dimensional function
wireframe(f)

## 2.2 Same thing but different function.
g = function(x, y) {(1 + y * 2) ^ (-x / y) * (1 + y * 1) ^ (x / y)}

myRange = seq(0.01, 1, len = 20)
grid = expand.grid(x = myRange , y = myRange)
grid$z = g(grid$x, grid$y)
print(wireframe(z ~ x * y, grid))


# -----------------------------------------------------------------------------
toc()       # Stop timer

