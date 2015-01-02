# -------------------------------------------
# 1 Vectors
# -------------------------------------------

# 1.1 Transpose of vectors
a = c(4,3)      # column vector
aprime = t(a)   # row vector
a
aprime

# 1.2 Length of vectors

a = c(4,3)
sqrt(sum(a^2))

# 1.3 Adding two vectors

a = c(4,3)
b = c(12,5)
a+b  # adding up vectors element-by-element


# 1.4 Multiplication of vectors

a = c(4,3)
b = 5*a
sqrt(sum(b^2)) # norm of longer vector
c = 0.5*a
sqrt(sum(c^2)) # norm of shorter vector
d = -3*a       # vector changes direction
sqrt(sum(d^2))

# Inner product
a = c(4,3)
b = c(12,5)
sum(a*b)  # inner product


# -------------------------------------------
# 2 Matrix manipulation
# -------------------------------------------

A = cbind(c(2,3),c(4,5))
B = cbind(c(2,6),c(1,3))

# 2.1 Transposing matrices

A = cbind(c(2,3),c(4,5))
Atrans = t(A)
A
Atrans


# 2.2 Adding matrices

A = cbind(c(2,3),c(4,5))
B = cbind(c(2,6),c(1,3))
C =  A+B
A
B
C


# 2.3 Multiplying matrices

A = cbind(c(12,3),c(3,-1),c(6,-4))
B = cbind(c(7,-2,1),c(8,0,11))
C = A %*% B # matrix multiplication

A
B
C
  

# 2.4 Multiplying a matrix with a vector

A = cbind(c(12,3),c(3,-1),c(6,-4))
b = c(7,-2,1)
C = A %*% b # matrix multiplied by vector: (m x n) x (n x 1) = (m x 1) 
A
b
C


# 2.5 Indexing and accessing elements of a matrix

A = rbind(c(11,12,13,14),c(21,22,23,24),c(31,32,33,34))
A
A[2,3]  # Element row 2, column 3
A[1,]   # First row
A[,1]   # First column
A[-1,]  # All, except first row
A[-2,-3]# All, except row 2 and column 3
A[,-2]  # Remove column 2
A[,1] = 99 # Fill first column with 99
A
A[A>90]=90 # Replace all elements > 99 with number 90
A



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    