# Homework 3
Submit this homework via Dropbox on Thursday, 11.55pm.
I need two files:

  * R-scripts are submitted in one file called: ``Homework3.R``
  * Python-scripts are submitted in one file called: ``Homework3.py``

I need to be able to quickly run these scripts on my computer.

I will based your homework grade on my grading of 2 randomly selected homework exercises. So please make sure that you complete every homework 100% as you might otherwise end up with zero points.

-------------------------------------------------------------------------------
## Exercise 1

Write the following program in **Python** first and then translate it into **R**.
Write a program that generates all odd numbers from $1$ to $n$. Set n in the beginning of the program and use a while loop to compute the numbers. (Make sure that if n is an even number, the largest generated odd number is $n-1$.) 

-------------------------------------------------------------------------------
## Exercise 2

You are given the following program:
```
a = [1, 3, 5, 7, 11]
b = [13, 17]
c = a + b
print c
b[0] = -1
d = [e+1 for e in a]
print d
d.append(b[0] + 1)
d.append(b[-1] + 1)
print d[-2:]
``` 
Explain what is printed by each print statement then translate it into **R**.

-------------------------------------------------------------------------------
## Exercise 3

The following code is supposed to compute the sum $latex s =
\sum_{k=1}^{M}\frac{1}{k}$:
```
s = 0; k = 1; M = 100
while k < M:
    s += 1/k
print s
```
This program does not work correctly. What are the three errors? (If you try to run the program, nothing will happen on the screen. Type Ctrl-C, i.e., hold down the Control (Ctrl) key and then type the c key, to stop a program.) Write a correct program.
There are two basic ways to find errors in a program: 
  1. read the program carefully and think about the consequences of each statement, and 
  2. print out intermediate results and compare with hand calcula-tions. 

First, try method (1) and find as many errors as you can. Then, try method (2) for $latex M = 3$ and compare the evolution of $latex s$ with your own hand calculations.
Translate it into **R**.
  
-------------------------------------------------------------------------------
## Exercise 4

Rewrite the corrected version of the program in Exercise 3 using a ``for`` loop over $k$ values instead of a ``while`` loop. Then write the same program in **R**.

-------------------------------------------------------------------------------
## Exercise 5

We define the following nested list:
``q = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h']]``

Index this list to extract:
 1. the letter a; 
 2. the list ['d', 'e', 'f'];
 3. the last element h; 
 4. the ``d`` element. 
 5. Explain why ``q[-1][-2]`` has the
value g. 

-------------------------------------------------------------------------------
## Exercise 6

Read chapter 3 in our **R** book Jones, Maillardet, and Robinson (2009) and
then go to section 3.9 and do exercise 9b. This program implements the Lotka-Volterra model for a "predator-prey" system. Plot the population of the 2 species over time into a graph.
Then implement the identical program in **Python** and produce a plot.

