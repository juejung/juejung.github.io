# Homework 9: Optimization 

Submit this homework in class on Tuesday.
I need two files:

  * R-scripts are submitted in one file called: ``Homework9.R``
  * Python-scripts are submitted in one file called: ``Homework9.py``

I need to be able to quickly run these scripts on my computer.

I will based your homework grade on my grading of 2 randomly selected homework exercises. So please make sure that you complete every homework 100% as you might otherwise end up with zero points.

Implement all exercises in **R** and **Python**!


## Exercise 1
-------------------------------------------------------------------------------

Read chapter 12 in your **R** book. 
Use the golden-section search algorithm to find all of the local maxima of the function 
\[ f(n) = \left\{ 
            \begin{array}{l l}
                0 & \quad \text{if $x=0$} \\
                |x|log(|x|/2)e^{-|x|} & \quad \text{otherwise} \\
            \end{array}
         \right.
\]
within the interval [-10, 10].  Hint: plotting the function first will give you a good idea where to look.

## Exercise 2
-------------------------------------------------------------------------------
Write a version of function ``golden section`` from class that plots intermediate results. That is, plot the function being optimised, then at each step draw a vertical line at the positions xl , xr , xm, and y (with the line at y in a different colour). Apply this new golden section algorithm to the function in exercise 1.


## Exercise 3
-------------------------------------------------------------------------------

Find the allocation of capital $K$ and labor $L$ that maximizes the following profit function of a represenatative firm:

$$ max_{\{K,L\}} A(K^{0.33} + L^{0.67}) - wL - rK,$$

where  the wage rate is $w = 1.84$ and the cost of capital is $r=0.75$ and $A=4$.

  1. Plot the function assuming values for $K \in[0,10]$ and $L \in [0,10]$.
  2. Find $K^*$ and $L^*$ that maximize profits


