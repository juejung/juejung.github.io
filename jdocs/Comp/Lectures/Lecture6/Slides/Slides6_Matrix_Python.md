# Scientific programming
--------------------------------------------------------------------------------

# 1 Vector manipulation


A vector of order $latex n>0$ is a set of ordered numbers. 
$$latex a = \left[ \begin{array}{c} 4 \\ 3 \end{array} \right], \: 
e_{1} = \left[ \begin{array}{c} 1 \\ 0 \\ 0 \end{array} \right], \: ... $$

These are column vectors. Row vectors are transposed column vectors, that is
$$latex a'=[4 \: 3], \: e'_{1}=[1 \: 0 \: 0], \: ...$$

## 1.1 Transposing vectors

In **Python** vectors are formed as column vectors by default. We can simply transpose vectors using the transpose function ```t()``` as follows:

```python
from pylab import *

a = array([4,3])      # column vector
aprime = a.transpose()   # row vector
print "a= " + str(a)
print "a'= " + str(aprime)
```
```
a= [4 3]
a'= [4 3]
```


## 1.2 Length of vectors

A vector (at least a two dimensional one) has a convenient geometric representation. It is an arrow, where the two coordinates indicate the direction and length of this arrow. Vector $$latex a = \left[ \begin{array}{c} 4 \\ 3 \end{array} \right]$$ points to the upper right (i.e. 4 over, 3 up). The length of a vector can be calculated using the Pythagoras theorem for the triangle. The length of vector $$latex a = \left[ \begin{array}{c} a_1 \\ a_2 \end{array} \right]$$ where $latex a_1$ and $latex a_2$ are simply numbers, can be calculated as $$latex \|a\| = \sqrt{a_1^2 + a_2^2}.$$
For our example, the vector norm for $$latex a = \left[ \begin{array}{c} 4 \\ 3 \end{array} \right] \text{ is } \rightarrow \|a\| = \sqrt{4^2 + 3^2} = 5.$$
In **Python** we can simply define a vector and calculate its norm (or length) as

```python
from pylab import *
a     = array([4,3])
norma = math.sqrt(sum(a**2))
print "norm(a) = " + str(norma)
print "norm(a) = " + str(norm(a))  # built in norm() command
```
```
norm(a) = 5.0
norm(a) = 5.0
```


## 1.3 Adding two vectors

Adding vectors is simple. We just add all numbers of two vectors 'element-by-element'. So that  $$a + b = \left[ \begin{array}{c} a_1  + b_1 \\ a_2+b_2 \end{array} \right].$$ In **Python** this is done with
```python
from pylab import *
a = array([4,3])
b = array([12,5])
print "a= " + str(a)
print "b= " + str(b)
print "a+b=" + str(a+b)  # adding up vectors element-by-element
```
```
a= [4 3]
b= [12  5]
a+b=[16  8]
```


## 1.4 Multiplication of vectors

A vector can be multiplied by a number (we call it a scalar denoted as $latex \lambda$ to distinguish it from vectors and the numbers that it contains). The scalar is multiplied with all numbers of the vector. If we multiply the vector with $latex \lambda > 1$ then the arrow that the vector symbolizes is becoming longer. If we multiply the vector with $latex 0 < \lambda < 1$ the arrow gets shorter. If we multiply the vector with a negative number $latex \lambda < 0$ then the arrow changes direction. More formally this is $$latex \lambda * a =  \left[ \begin{array}{c} \lambda *a_1 \\ \lambda *a_2 \end{array} \right].$$

In **Python** it's simply

```python
from pylab import *
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
```
```
a=[4 3]
anorm=5.0
b=[20 15]
bnorm=25.0
c=[ 2.   1.5]
cnorm=2.5
d=[-12  -9]
dnorm=15.0
```


When multiplying two vectors we form a so called 'inner product' as follows:
$$latex a*b = \sum_{i=1}^{n}a_i*b_i.$$ 

The following example shows this with numbers: 

$$latex a = \left[ \begin{array}{c} 4 \\ 3 \end{array} \right] \text{ and }  b = \left[ \begin{array}{c} 12 \\ 5 \end{array} \right]$$ 

then 

$$latex ax*b = 4*12 + 3*5.$$ In **Python** the inner product is simply:

```python
from pylab import *
a = array([4,3])
b = array([12,5])
print "a= " + str(a)
print "b= " + str(b)
print "a*b =" + str(sum(a*b))  # inner product
```
```
a= [4 3]
b= [12  5]
a*b =63
```


--------------------------------------------------------------------------------
# 2 Matrix manipulation

Matrices are "two dimensional" vectors. In **Python** we define a matrix as

```python
from pylab import *
A = array([[2,3],[4,5]])
B = array([[2,6],[1,3]])
print "A=" + str(A)
print "B=" + str(B)
```
```
A=[[2 3]
 [4 5]]
B=[[2 6]
 [1 3]]
```

## 2.1 Transposing matrices

Transposing matrices requires again the ``t()`` command. It writes each column as row of a new matrix. So that the transpose of matrix $latex A$ in the above example becomes:

```python
from pylab import *
A = array([[2,3],[4,5]])
B = array([[2,6],[1,3]])
Atrans = A.transpose()
print "A=" + str(A)
print "A'=" + str(Atrans)
```
```
A=[[2 3]
 [4 5]]
A'=[[2 4]
 [3 5]]
```


If we transpose the transpose of matrix A, we get the original matrix A back.

## 2.2 Adding matrices

When adding two matrices $latex A$ and $latex B$ we simply add all the elements of each matrix 'element-by-element'. Note that the dimensions (i.e. the number of rows and columns) of the two matrices have to be identical. So if matrix $latex A$ has dimension $latex m \times n$, that is $latex m$ rows and $latex n$ columns, then matrix $latex B$ needs to be of dimensions $latex m \times n$ as well.

```python
from pylab import *
A = array([[2,3],[4,5]])
B = array([[2,6],[1,3]])
C =  A+B
print "A=" + str(A)
print "B=" + str(B)
print "C=" + str(C)
```
```
A=[[2 3]
 [4 5]]
B=[[2 6]
 [1 3]]
C=[[4 9]
 [5 8]]
```


## 2.3 Multiplying matrices

When multiplying two matrices $latex A$ and $latex B$ we need to make sure that the number of columns of matrix $latex A$ is equal the number of rows of matrix $latex B$. So if $latex A$ has dimension $latex m \times n$ then $latex B$ needs to have dimension $latex n \times r$ since matrix multiplication implies that we form the 'inner product' of each row of $latex A$ with each column of $latex B$. This results in a new matrix of dimension $latex m \times r$.
Here is an example. Given matrices 
$$latex  A = \left[ \begin{array}{ccc} 12 & 3 &6 \\ 9 &-1 & -4 \end{array} \right] \text{ and }
    B = \left[ \begin{array}{cc} 7 & 8  \\ -2 &0 \\ 1 & 11 \end{array} \right] $$ 
    
the product of $latex A$ $latex (2 \times 3)$ and $latex B$ of dimension $latex (3 \times 2)$ is a matrix $latex C$ with dimension $latex (2 \times 2)$:
    
$$latex  AB = \left[ \begin{array}{cc} 12*7+3*(-2)+6*1 & 12*8+3*0+6*11 \\ 
                                  9*7+(-1)*(-2)+(-4)*1 & 9*8+(-1)*0+(-4)*11 \end{array} \right].$$
                                  
In **Python** matrix multiplication is achieved using the command ``dot()``.                                   
```python
from pylab import *
A = array([[12,3,6],[3,-1,-4]])
B = array([[7,8],[-2,0],[1,11]])
C = dot(A,B) # matrix multiplication

print "A=" + str(A)
print "B=" + str(B)
print "C=" + str(C)
```
```
A=[[12  3  6]
 [ 3 -1 -4]]
B=[[ 7  8]
 [-2  0]
 [ 1 11]]
C=[[ 84 162]
 [ 19 -20]]
```


## 2.4 Multiplying a matrix with a vector

Vectors are simply $latex n \times 1$ or $latex 1 \times n$ dimensional matrices so that the same rules as above apply for multiplying a matrix with a vector.

```python
from pylab import *
A = array([[12,3,6],[3,-1,-4]])
b = array([7,-2,1])
C = dot(A,b) # matrix multiplied by vector: (m x n) x (n x 1) = (m x 1) 
print "A=" + str(A)
print "b=" + str(b)
print "C=" + str(C)
```
```
A=[[12  3  6]
 [ 3 -1 -4]]
b=[ 7 -2  1]
C=[84 19]
```


## 2.5 Indexing and accessing elements of a matrix


```python
from pylab import *
A = array([[11,12,13,14],[21,22,23,24],[31,32,33,34]])
print "A=" + str(A)
print "A[1,2]=" + str(A[1,2])   # Element row 2, column 3 (remember Python starts indexing at 0!!)
print "A[0,:]=" + str(A[0,:])   # First row
print "A[:,0]=" + str(A[:,0])   # First column
print "A[1:,:]=" + str(A[1:,])   # All, except first row

print "remove column 2"
print "A.take([0,2,3],axis=1) =" + str(A.take([0,2,3],axis=1))  # Remove column 2 (or take column 1, 3, and 4)
A[:,0] = 99 # Fill first column with 99
print "A=" + str(A)
print "(A>90).choose(A,90)=" +str((A>90).choose(A,90)) # Replace all elements > 99 with number 90

```
```
A=[[11 12 13 14]
 [21 22 23 24]
 [31 32 33 34]]
A[1,2]=23
A[0,:]=[11 12 13 14]
A[:,0]=[11 21 31]
A[1:,:]=[[21 22 23 24]
 [31 32 33 34]]
remove column 2
A.take([0,2,3],axis=1) =[[11 13 14]
 [21 23 24]
 [31 33 34]]
A=[[99 12 13 14]
 [99 22 23 24]
 [99 32 33 34]]
(A>90).choose(A,90)=[[90 12 13 14]
 [90 22 23 24]
 [90 32 33 34]]
```



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    