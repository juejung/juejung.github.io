# Scientific programming
--------------------------------------------------------------------------------

# 1 Vector manipulation


A vector of order $latex n>0$ is a set of ordered numbers. 
$$latex a = \left[ \begin{array}{c} 4 \\ 3 \end{array} \right], \: 
e_{1} = \left[ \begin{array}{c} 1 \\ 0 \\ 0 \end{array} \right], \: ... $$

These are column vectors. Row vectors are transposed column vectors, that is
$$latex a'=[4 \: 3], \: e'_{1}=[1 \: 0 \: 0], \: ...$$

## 1.1 Transposing vectors

In **R** vectors are formed as column vectors by default. We can simply transpose vectors using the transpose function ```t()``` as follows:


```r
a = c(4, 3)  # column vector
aprime = t(a)  # row vector
a
```

```
## [1] 4 3
```

```r
aprime
```

```
##      [,1] [,2]
## [1,]    4    3
```




## 1.2 Length of vectors

A vector (at least a two dimensional one) has a convenient geometric representation. It is an arrow, where the two coordinates indicate the direction and length of this arrow. Vector 

$$latex a = \left[ \begin{array}{c} 4 \\ 3 \end{array} \right]$$ 

points to the upper right (i.e. 4 over, 3 up). The length of a vector can be calculated using the Pythagoras theorem for the triangle. The length of vector 

$$latex a = \left[ \begin{array}{c} a_1 \\ a_2 \end{array} \right]$$ 

where $latex a_1$ and $latex a_2$ are simply numbers, can be calculated as 

$$latex \|a\| = \sqrt{a_1^2 + a_2^2}.$$
For our example, the vector norm for 
$$latex a = \left[ \begin{array}{c} 4 \\ 3 \end{array} \right] \text{ is } \rightarrow \|a\| = \sqrt{4^2 + 3^2} = 5.$$
In **R** we can simply define a vector and calculate its norm (or length) as



```r
a = c(4, 3)
sqrt(sum(a^2))
```

```
## [1] 5
```




## 1.3 Adding two vectors

Adding vectors is simple. We just add all numbers of two vectors 'element-by-element'. So that

$$latex a + b = \left[ \begin{array}{c} a_1  + b_1 \\ a_2+b_2 \end{array} \right].$$ 

In **R** this is done with


```r
a = c(4, 3)
b = c(12, 5)
a + b  # adding up vectors element-by-element
```

```
## [1] 16  8
```




## 1.4 Multiplication of vectors

A vector can be multiplied by a number (we call it a scalar denoted as $latex \lambda$ to distinguish it from vectors and the numbers that it contains). The scalar is multiplied with all numbers of the vector. If we multiply the vector with $latex \lambda > 1$ then the arrow that the vector symbolizes is becoming longer. If we multiply the vector with $latex 0 < \lambda < 1$ the arrow gets shorter. If we multiply the vector with a negative number $latex \lambda < 0$ then the arrow changes direction. More formally this is 

$$latex \lambda * a =  \left[ \begin{array}{c} \lambda *a_1 \\ \lambda *a_2 \end{array} \right].$$

In **R** it's simply



```r
a = c(4, 3)
b = 5 * a
sqrt(sum(b^2))  # norm of longer vector
```

```
## [1] 25
```

```r
c = 0.5 * a
sqrt(sum(c^2))  # norm of shorter vector
```

```
## [1] 2.5
```

```r
d = -3 * a  # vector changes direction
sqrt(sum(d^2))
```

```
## [1] 15
```




When multiplying two vectors we form a so called 'inner product' as follows:

$$latex a*b = \sum_{i=1}^{n}a_i*b_i.$$ 

The following example shows this with numbers: 

$$latex a = \left[ \begin{array}{c} 4 \\ 3 \end{array} \right] \text{ and }  b = \left[ \begin{array}{c} 12 \\ 5 \end{array} \right]$$ 

then 

$$latex ax*b = 4*12 + 3*5.$$ 

In **R** the inner product is simply:


```r
a = c(4, 3)
b = c(12, 5)
sum(a * b)  # inner product
```

```
## [1] 63
```




---------------------------------------------
# 2 Matrix manipulation

Matrices are "two dimensional" vectors. In **R** we define a matrix as



```r
A = cbind(c(2, 3), c(4, 5))
B = cbind(c(2, 6), c(1, 3))
```



## 2.1 Transposing matrices

Transposing matrices requires again the ``t()`` command. It writes each column as row of a new matrix. So that the transpose of matrix $latex A$ in the above example becomes:



```r
A = cbind(c(2, 3), c(4, 5))
Atrans = t(A)
A
```

```
##      [,1] [,2]
## [1,]    2    4
## [2,]    3    5
```

```r
Atrans
```

```
##      [,1] [,2]
## [1,]    2    3
## [2,]    4    5
```




If we transpose the transpose of matrix A, we get the original matrix A back.

## 2.2 Adding matrices

When adding two matrices $latex A$ and $latex B$ we simply add all the elements of each matrix 'element-by-element'. Note that the dimensions (i.e. the number of rows and columns) of the two matrices have to be identical. So if matrix $latex A$ has dimension $latex m \times n$, that is $latex m$ rows and $latex n$ columns, then matrix $latex B$ needs to be of dimensions $latex m \times n$ as well.



```r
A = cbind(c(2, 3), c(4, 5))
B = cbind(c(2, 6), c(1, 3))
C = A + B
A
```

```
##      [,1] [,2]
## [1,]    2    4
## [2,]    3    5
```

```r
B
```

```
##      [,1] [,2]
## [1,]    2    1
## [2,]    6    3
```

```r
C
```

```
##      [,1] [,2]
## [1,]    4    5
## [2,]    9    8
```




## 2.3 Multiplying matrices

When multiplying two matrices $latex A$ and $latex B$ we need to make sure that the number of columns of matrix $latex A$ is equal the number of rows of matrix $latex B$. So if $latex A$ has dimension $latex m \times n$ then $latex B$ needs to have dimension $latex n \times r$ since matrix multiplication implies that we form the 'inner product' of each row of $latex A$ with each column of $latex B$. This results in a new matrix of dimension $latex m \times r$.
Here is an example. Given matrices 
$$latex  A = \left[ \begin{array}{ccc} 12 & 3 &6 \\ 9 &-1 & -4 \end{array} \right] \text{ and }
    B = \left[ \begin{array}{cc} 7 & 8  \\ -2 &0 \\ 1 & 11 \end{array} \right]$$ 

the product of $latex A$ $latex (2 \times 3)$ and $latex B$ of dimension $latex (3 \times 2)$ is a matrix $latex C$ with dimension $latex (2 \times 2)$:
    
$$latex  AB = \left[ \begin{array}{cc} 12*7+3*(-2)+6*1 & 12*8+3*0+6*11 \\ 
                                  9*7+(-1)*(-2)+(-4)*1 & 9*8+(-1)*0+(-4)*11 \end{array} \right]. $$
                                  
In **R** matrix multiplication is achieved using the command ``%*%``.                                   


```r
A = cbind(c(12, 3), c(3, -1), c(6, -4))
B = cbind(c(7, -2, 1), c(8, 0, 11))
C = A %*% B  # matrix multiplication

A
```

```
##      [,1] [,2] [,3]
## [1,]   12    3    6
## [2,]    3   -1   -4
```

```r
B
```

```
##      [,1] [,2]
## [1,]    7    8
## [2,]   -2    0
## [3,]    1   11
```

```r
C
```

```
##      [,1] [,2]
## [1,]   84  162
## [2,]   19  -20
```




## 2.4 Multiplying a matrix with a vector

Vectors are simply $latex n \times 1$ or $latex 1 \times n$ dimensional matrices so that the same rules as above apply for multiplying a matrix with a vector.



```r
A = cbind(c(12, 3), c(3, -1), c(6, -4))
b = c(7, -2, 1)
C = A %*% b  # matrix multiplied by vector: (m x n) x (n x 1) = (m x 1)
A
```

```
##      [,1] [,2] [,3]
## [1,]   12    3    6
## [2,]    3   -1   -4
```

```r
b
```

```
## [1]  7 -2  1
```

```r
C
```

```
##      [,1]
## [1,]   84
## [2,]   19
```




## 2.5 Indexing and accessing elements of a matrix




```r
A = rbind(c(11, 12, 13, 14), c(21, 22, 23, 24), c(31, 32, 33, 34))
A
```

```
##      [,1] [,2] [,3] [,4]
## [1,]   11   12   13   14
## [2,]   21   22   23   24
## [3,]   31   32   33   34
```

```r
A[2, 3]  # Element row 2, column 3
```

```
## [1] 23
```

```r
A[1, ]  # First row
```

```
## [1] 11 12 13 14
```

```r
A[, 1]  # First column
```

```
## [1] 11 21 31
```

```r
A[-1, ]  # All, except first row
```

```
##      [,1] [,2] [,3] [,4]
## [1,]   21   22   23   24
## [2,]   31   32   33   34
```

```r
A[-2, -3]  # All, except row 2 and column 3
```

```
##      [,1] [,2] [,3]
## [1,]   11   12   14
## [2,]   31   32   34
```

```r
A[, -2]  # Remove column 2
```

```
##      [,1] [,2] [,3]
## [1,]   11   13   14
## [2,]   21   23   24
## [3,]   31   33   34
```

```r
A[, 1] = 99  # Fill first column with 99
A
```

```
##      [,1] [,2] [,3] [,4]
## [1,]   99   12   13   14
## [2,]   99   22   23   24
## [3,]   99   32   33   34
```

```r
A[A > 90] = 90  # Replace all elements > 99 with number 90
A
```

```
##      [,1] [,2] [,3] [,4]
## [1,]   90   12   13   14
## [2,]   90   22   23   24
## [3,]   90   32   33   34
```





    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
