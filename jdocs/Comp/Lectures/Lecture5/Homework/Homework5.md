# Homework 5: Functions

Submit this homework in class on Tuesday.
I need two files:

  * R-scripts are submitted in one file called: ``Homework5.R``
  * Python-scripts are submitted in one file called: ``Homework5.py``

I need to be able to quickly run these scripts on my computer.

I will based your homework grade on my grading of 2 randomly selected homework exercises. So please make sure that you complete every homework 100% as you might otherwise end up with zero points.

Implement all exercises in **R** and **Python**!

-------------------------------------------------------------------------------
## Exercise 1


This exercise refers to Langtangen (2011) Chapter 3.  The formula for converting Fahrenheit degrees to Celsius reads:

$$C = \frac{5}{9} (F - 32) $$

Write a function C(F) that implements this formula. To verify the im-plementation of C(F), you can convert a Celsius temperature to Fahrenheit and then back to Celsius again using the F(C) function from Chap-ter 3.1.1 and the C(F) function implementing (3.7). That is, you can check that the boolean expression c == C(F($latex c $)) is True for any temper-ature c (you should, however, be careful with comparing real numbers
with ==, see Exercise 2.28).

-------------------------------------------------------------------------------
## Exercise 2


Some object is moving along a path in the plane. At n points of time we have recorded the corresponding (x, y) positions of the object:
$(x_0 , y_0), (x_1, y_2), ..., (x_{n-1}, y_{n-1})$. 
The total length L of the path from $(x_0, y_0)$ to $(x_{n-1}, y_{n-1})$ is the sum of all the individual line segments $(x_{i-1}, y_{i-1})$ to $(x_i, y_i)$, for $i = 1,..., n-1)$:

$$ L = \sum_{i=1}^{n-1} \sqrt{(x_i - x_{i-1})^2 + (y_i - y_{i-1})^2} $$

Make a function ``pathlength(x,y)`` for computing L according to the formula. The arguments x and y hold all the $x_0,...,x_{n-1}$ and $y_0,...,y_{n-1}$ coordinates, respectively. Test the function on a triangular path with the four points (1,1), (2,1), (1,2), and (1,1). 


-------------------------------------------------------------------------------
## Exercise 3


The factorial of n, written as n!, is defined as $n! = n(n - 1)(n - 2)···2\times 1$ with the special cases $1! = 1$, $0! = 1$. For example, 4! = 4 · 3 · 2 · 1 = 24, and 2! = 2 · 1 = 2. Write a function ``fact(n)`` that returns $n!$. Return 1 immediately if x is 1 or 0, otherwise use a loop to compute n!. 

Remark. In order to check your own program you can compare it to the built in ready-made factorial function by
```
from math import factorial
factorial(4)
24
```
-------------------------------------------------------------------------------
## Exercise 4


The (Euclidean) length of a vector $v = (a_0,a_1,\dots, a_k)$ is the square root of the sum of squares of its coordinates $\sqrt{a_0^2+a_1^2,\dots}$. Write a function that returns the length of a vector. Then test your function and calculate the length of vector: $a = [3,5,23,45,12]$.

-------------------------------------------------------------------------------
## Exercise 5


In Exercise 3.9.2 in our **R** book (Jones, Maillardet, and Robinson (2009)) you wrote a program to calculate h(x, n), the sum of a finite geometric series. Turn this program into a function that takes two arguments, ``x`` and ``n``, and returns ``h(x, n)``.  Make sure you deal with the case ``x = 1``.
Test your function for ``x=0.70`` and ``n=8``.
