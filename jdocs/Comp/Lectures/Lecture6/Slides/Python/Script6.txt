# -*- coding: utf-8 -*-
"""
# =====================================================================
#
# Scriptfile Lecture 6
# -------------------------
# Computational Economics
# (c) Juergen Jung, 2012
#
# =====================================================================

"""
import math
from pylab import *

# -------------------------------------------
# 1 Vectors
# -------------------------------------------

# 1.1 Transpose of vectors
a = array([4,3])      # column vector
aprime = a.transpose()   # row vector
print "a= " + str(a)
print "a'= " + str(aprime)


# 1.2 Length of vectors
a     = array([4,3])
norma = math.sqrt(sum(a**2))
print "norm(a) = " + str(norma)
print "norm(a) = " + str(norm(a))  # built in norm() command


# 1.3 Adding two vectors
a = array([4,3])
b = array([12,5])
print "a= " + str(a)
print "b= " + str(b)
print "a+b=" + str(a+b)  # adding up vectors element-by-element


# 1.4 Multiplication of vectors
a = array([4,3])
anorm  = math.sqrt(sum(a**2)) # norm of vector a
print "a=" + str(a)
print "anorm=" + str(anorm)
b = 5*a
bnorm = math.sqrt(sum(b**2)) # norm of longer vector
print "b=" + str(b)
print "bnorm=" + str(bnorm)
c = 0.5*a
cnorm = math.sqrt(sum(c**2)) # norm of shorter vector
print "c=" + str(c)
print "cnorm=" + str(cnorm)
d = -3*a       # vector changes direction
dnorm = math.sqrt(sum(d**2))
print "d=" + str(d)
print "dnorm=" + str(dnorm)

# Inner product
a = array([4,3])
b = array([12,5])
print "a= " + str(a)
print "b= " + str(b)
print "a*b =" + str(sum(a*b))  # inner product


# -------------------------------------------
# 2 Matrix manipulation
# -------------------------------------------
print " --------------------------------------------"
A = array([[2,3],[4,5]])
B = array([[2,6],[1,3]])

# 2.1 Transposing matrices
Atrans = A.transpose()
print "A=" + str(A)
print "A'=" + str(Atrans)


# 2.2 Adding matrices
A = array([[2,3],[4,5]])
B = array([[2,6],[1,3]])
C =  A+B
print "A=" + str(A)
print "B=" + str(B)
print "C=" + str(C)


# 2.3 Multiplying matrices
A = array([[12,3,6],[3,-1,-4]])
B = array([[7,8],[-2,0],[1,11]])
C = dot(A,B) # matrix multiplication

print "A=" + str(A)
print "B=" + str(B)
print "C=" + str(C)
  

# 2.4 Multiplying a matrix with a vector
A = array([[12,3,6],[3,-1,-4]])
b = array([7,-2,1])
C = dot(A,b) # matrix multiplied by vector: (m x n) x (n x 1) = (m x 1) 
print "A=" + str(A)
print "b=" + str(b)
print "C=" + str(C)


# 2.5 Indexing and accessing elements of a matrix
print " -------------------------------- "
A = array([[11,12,13,14],[21,22,23,24],[31,32,33,34]])
print "A=" + str(A)
print "A[1,2]=" + str(A[1,2])   # Element row 2, column 3 (remember Python starts indexing at 0!!)
print "A[0,:]=" + str(A[0,:])   # First row
print "A[:,0]=" + str(A[:,0])   # First column
print "A[1:,:]=" + str(A[1:,])   # All, except first row

print "removecol 2 =" + str(A.take([0,2,3],axis=1))  # Remove column 2 (or take column 1, 3, and 4)
A[:,0] = 99 # Fill first column with 99
print "A=" + str(A)
print "(A>90).choose(A,90)=" +str((A>90).choose(A,90)) # Replace all elements > 99 with number 90




    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
 