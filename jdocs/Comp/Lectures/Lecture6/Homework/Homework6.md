# Homework 6: Vectors and matrices

Submit this homework in class on Tuesday.
I need two files:

  * R-scripts are submitted in one file called: ``Homework6.R``
  * Python-scripts are submitted in one file called: ``Homework6.py``

I need to be able to quickly run these scripts on my computer.

I will based your homework grade on my grading of 2 randomly selected homework exercises. So please make sure that you complete every homework 100% as you might otherwise end up with zero points.

Implement all exercises in **R** and **Python**!


## Exercise 1
-------------------------------------------------------------------------------

The aim is to fill two vector arrays ``xv`` and ``yv`` with ``x`` and ``f(x)`` values, respectively, where 

$$latex f(x) = \frac{1}{\sigma \sqrt{2 \pi}}  e^{- \frac{1}{2} \left( \frac{x- \mu}{\sigma} \right) ^2} $$

is the density of the standard normal distribution, that is a normal density with mean $\mu=0$ and standard deviation $\sigma = 1$. Let the ``xv`` values be uniformly spaced in $latex xv = [-4, 4]$ with a small enough grid so that the function plot is not too bumpy. A gridspace of $latex 0.01$ is probably sufficient. Write a loop to fill in the values for $latex xv$ and $latex yv=f(xv)$. Then plot(xv,yv)


## Exercise 2
-------------------------------------------------------------------------------

Vectorize the code in Exercise 1 by creating the ``xv`` values using the linspace function and by evaluating ``yv = f(xv)`` for a vector array argument. So here you do not use a loop! Then plot(xv,yv)


## Exercise 3
-------------------------------------------------------------------------------

In **Python** Create a vector array ``wv`` with values 0, 0.1, 0.2, . . ., 3. Write print statements to print w[:], w[:-2], w[::5], w[2:-2:6]. Try to understandwhich elements of the array are printed using these commands.

In **R** define the identical vector ``wv``. Then write print statements, using ``cat()``, that results in similar outputs as the previous **Python** code.

## Exercise 4
-------------------------------------------------------------------------------

Make a plot of the function $y(t) = v_0 t - 0.5gt^2$ for $v_0 = 10, g = 9.81$, and $t \in [0, 2v_0/g]$. The label on the x axis should be 'time (s)' and the label on the y axis should be 'height (m)'.

