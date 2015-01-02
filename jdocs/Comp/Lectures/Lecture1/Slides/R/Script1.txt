# =====================================================================
#
# Scriptfile Lecture 1
# -------------------------
# Computational Economics
# (c) Juergen Jung, 2012
#
# =====================================================================

#-------------------------------------------------------------------------------
# Author: Juergen JUng
# Date  : 22 July 2012
#-------------------------------------------------------------------------------
rm(list=ls()) # Remove almost everything in the memory


# 1 -----------------------
x=2
y=3
x + y

# 2 -----------------------
# You can document your script files using the "#" symbol. This works for R and Python and allows you to add commentary to your codes.
x = c(1,3,4,9)
y = c(9.2, 0.3, 3.2, 2.8)
year  = seq(2000, 2003, by=1)         # seq(from, to, by = stepsize)
somev = seq(2000, 2003, length=10)    # seq(from, to, length = nr. of steps)
names = c("Tom", "Dick", "Harry", "Patrick")
#
#X[0]  # this will cause an error, so I comment it out!
cat("x[1]= ", x[1], "\n")
cat("x[2]= ", x[2], "\n")
cat("names[1]= ", names[1], "\n")
cat("names[3]= ", names[3], "\n")


# 3 -----------------------
x1 = c(1,3,4,9)
x2 = c(2,5,6,3)
#
x1+x2
x1-x2
x1*x2
x1/x2


# 4 -----------------------
a = rbind(c(2,3),c(4,5))
b = rbind(c(2,6),c(1,3))
a*b
a-b

# 5 -----------------------
a = matrix(0,3,5)  # makes a 3x5 matrix of zeros
b = matrix(1,4,3)  # makes a 4x3 matrix filled with ones
c = diag(1,3)      # Identity matrix (=matrix with 1 in main diagonal)
a
b
c

