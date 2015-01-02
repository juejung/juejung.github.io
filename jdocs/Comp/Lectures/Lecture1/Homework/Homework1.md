# Homework 1
Submit this homework via Dropbox on Thursday, September 6 at 11:00 am.
I need two files: 
 * R-scripts are submitted in one file called: ```Homework1.R```
 * Python-scripts are submitted in one file called: ```Homework1.py```
Simply put these two files into the Homework1 Dropbox folder. It will sync and I will then be able to access it. I need to be able to quickly run these scripts on my computer, so make sure that they run through and don't throw any errors.

I will base your homework grade on my grading of 2 randomly selected homework exercises. So please make sure that you complete every homework 100% as you might otherwise end up with zero points.

-------------------------------------------------------------------------------
## Exercise 1:
From Jones, Maillardet, and Robinson (2009): Chapter 2, Exercise 2 (a,b,c,d). Provide both R and Python scripts.

Give R expressions that return the following matrices and vectors
 1.  (1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1)
 2.  (1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5)
 3.  $$ 
             \left( \begin{array}{ccc}
            0 & 1 & 1 \\
            1 & 0 & 1 \\
            1 & 1 & 0 \end{array} \right) 
        $$
 4.     $$
             \left( \begin{array}{ccc}
            0 & 2 & 3 \\
            0 & 5 & 0 \\
            7 & 0 & 0 \end{array} \right) 
        $$

-------------------------------------------------------------------------------------
## Exercise 2: 
From Langtangen ( 2011): Chapter 1, Exercise 1.6. Provide both R and Python scripts.

Compute the growth of money in a bank. Let $p$ be a bank's interest rate in percent per year. An initial amount $A$ has then grown to 
$$ A(1+\frac{p}{100})^n $$
after $n$ years. Make a program for computing how much money 1,000 euros have grown to after three years with $5\%$ interest rate.

-------------------------------------------------------------------------------------
## Exercise 3:
From Langtangen ( 2011): Chapter 1, Exercise 1.8. Translate this program into R-code.

Type the following program in your editor and execute it. If your program does not work, check that you have copied the code correctly.

``` 
from math import pi
h = 5.0 # height
b = 2.0 # base
r = 1.5 # radius
#
area_parallelogram = h*b
print "The area of the parallelogram is %.3f" % area_parallelogram
#
area_square = b**2
print "The area of the square is %g" % area_square
#
area_circle = pi*r**2
print "The area of the circle is %.3f" % area_circle
#
volume_cone = 1.0/3*pi*r**2*h
print 'The volume of the cone is %.3f' % volume_cone
```

-------------------------------------------------------------------------------------
## Exercise 4:
From Langtangen ( 2011): Chapter 1, Exercise 1.9. First correct the Python program. Then implement the same program in R.

Type these short programs in your editor and execute them. When they do not work, identify and correct the erroneous statements.

 * The following code checks whether $latex sin(x)^2  + cos(x)^2 = 1 $ ?
  
```
from math import sin, cos
x = pi/4
1_val = sin^2(x) + cos^2(x)
print 1_VAL
```

 * Work with the expressions for movement with constant acceleration: 1.8 Exercise 45

```
v0 = 3 m/s
t = 1 s
a = 2 m/s**2
s = v0*t + 1/2 a*t**2
print s
```


 * The next code chunk verifies these equations:
  $$latex 
    \begin{eqnarray*}
    (a + b)^2 &=& a^2 + 2ab + b^2 \\
    (a - b)^2 &=& a^2 - 2ab + b^2 
    \end{eqnarray*}  
  $$
  
```
a = 3,3 b = 5,3
a2 = a**2
b2 = b**2
eq1_sum = a2 + 2ab + b2
eq2_sum = a2 - 2ab + b2
eq1_pow = (a + b)**2
eq2_pow = (a - b)**2
print 'First equation: %h = %' % (eq2_sum, eq2_sum)
print 'Second equation: %h = %' % (eq2_pow, eq2_pow)
```

-------------------------------------------------------------------------------
## Exercise 5:
From Langtangen ( 2011): Chapter 1, Exercise 1.18 First correct the Python program. Then implement the same program in R.

Find errors in the coding of a formula. Given a quadratic equation,
$$latex ax^2 + bx + c = 0, $$
the two roots are:
$$latex x_1 = \frac{-b + \sqrt{b^2 - 4ac}}{2a},  x_2 = \frac{-b - \sqrt{b^2 - 4ac}}{2a} $$


What are the problems with the following program?

```
a = 2; b = 1; c = 2
from math import sqrt
q = sqrt(b*b - 4*a*c)
x1 = (-b + q)/2*a
x2 = (-b - q)/2*a
print x1, x2
```

Hint: Compute all terms in the math expression above with the aid of a calculator, and compare with the corresponding intermediate results computed in the program (you need to add some ``print`` statements to see the result of ``q``, ``-b+q``, and ``2*a``).



