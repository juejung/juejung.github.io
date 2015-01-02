#-------------------------------------------------------------------------------
# Author: Juergen JUng
# Date  : 22 July 2012
#-------------------------------------------------------------------------------
print("-------------- START ----------------")
rm(list=ls()) # Remove almost everything in the memory
setwd("C:/Dropbox/Towson/Teaching/3_ComputationalEconomics/Lectures/Lecture2/R")
print(paste("My current working directory is:",getwd()),quote=FALSE)        #Printing the current R working directory
# ------------------------------------------------------------------------------
tic()          # Start timer
# ------------------------------------------------------------------------------

# Basic programming techniques

# --------------------------------------------------
# 1 Branching
# --------------------------------------------------
x = runif(1)  # draw a random number between 0 and 1
if (x > 0.5) {
  cat("Number x=",x, " is greater than 0.5 \n")
} else {
  cat("Number x=",x, " is smaller than or equal to 0.5 \n")
}

x = runif(1)
y = runif(1)

if (x > y) {
  cat("X is greater than Y \n")
} else if (x==y) {
  cat("X is equal to Y \n")
} else if (x<y) {
  cat("X is smaller than Y \n")
}

# --------------------------------------------------
# 2 For loops
# --------------------------------------------------

## Loop 1
# --------------------------
xv = seq(1,9, by = 2)
sumx = 0

for (x in xv) {
  sumx = sumx + x  # adds up the elements in vector xv
  cat("X =", x, "\n")
  cat("sum(x) = ", sumx, "\n")
}
# or simply
sum(xv)

## Loop 2
# --------------------------
n = 6
n_fac = 1

for (i in 1:n) {
  cat("i = ", i, "\n")
  n_fac = n_fac * i
  cat("n_fac = ", n_fac, "\n")
}
cat("The factorial of ", n, " is: ", n_fac, "\n")

## Loop 3
# --------------------------
xv = seq(1,9, length = 20)

for (i in 1:length(xv)) {
  cat("i= ", i, "\n")
  cat("xv[i]= ", xv[i], "\n")
  cat("sqrt(xv[i])= ", sqrt(xv[i]), "\n")
}

yv = sqrt(xv)
plot(yv, ylim=c(0,9))
lines(xv)
title("Simple plot of two vectors")

# --------------------------------------------------
# 3 While loop
# --------------------------------------------------

## While loop 1
# -------------------------
x = 0
y = 0
while (x < 10) {
  y = y + x
  cat("X= ", x, " and Y= ", y, "\n")
  x = x + 1
}

## While loop 2
# -------------------------
r           = 0.11  # annual interest rate
period      = 1/12  # time between repayments in years (i.e. monthly repayments)
debt_initial= 1000  # initial debt
payments    = 12    # amount repaid each period

mytime = 0
debt = debt_initial
while (debt> 0) {
  mytime = mytime + period
  debt = debt*(1 + r*period) - payments
}
cat("Loan will be repaid in: ", mytime, " years. \n")

# ------------------------------------------------------------------------------
print("-------------- FINISH ---------------")
toc()       # Stop timer
# ------------------------------------------------------------------------------
