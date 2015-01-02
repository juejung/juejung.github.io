# Homework 7: Random numbers

Submit this homework in class on Tuesday.
I need two files:

  * R-scripts are submitted in one file called: ``Homework7.R``
  * Python-scripts are submitted in one file called: ``Homework7.py``

I need to be able to quickly run these scripts on my computer.

I will based your homework grade on my grading of 2 randomly selected homework exercises. So please make sure that you complete every homework 100% as you might otherwise end up with zero points.

Implement all exercises in **R** and **Python**!


## Exercise 1
-------------------------------------------------------------------------------

Flip a coin N times.  Make a program that simulates flipping a coin N times. Print out "tail" or "head" for each flip and let the program count the number of heads. 
Hint: In **Python** use r = random.random() and define ``head`` as r <= 0.5 or draw an integer among {1, 2} with r = random.randint(1,2) and define head when r is 1.
Hint: In **R** use r = runif(1) which draws a random number from the [0,1] interval and define ``head`` as r<=0.5.

## Exercise 2
-------------------------------------------------------------------------------

Compute a probability.  What is the probability of getting a number between 0.5 and 0.6 when drawing uniformly distributed random numbers from the interval [0, 1]? 

To answer this question empirically, let a program draw N such random numbers using Python's standard random module. Count how many of them, M , fall in the interval (0.5, 0.6), and compute the probability as M/N . 

Hint: Run the program four times with N = 100.  The tricky part is to count how many of the 100 random numbers fall in the intervall (0.5, 0.6).
Run the program again for N = 1000 and see whether the relative frequency changes a lot. Finally run the program with N = 10,000.

## Exercise 3
-------------------------------------------------------------------------------

Probabilities of rolling dice. You throw a die a thousand times. How many times does the number 6 come up?

Hint: In **R** use sample(1:6, size=1000, replace=TRUE) to draw integer random numbers between 1 and 6. In **Python** use  r = random.randint(1,6) to generate the random numbers.

## Exercise 5
-------------------------------------------------------------------------------

Decide if a dice game is fair.  
Somebody suggests the following game. You pay 1 unit of money and are allowed to throw four dice. If the sum of the eyes on the dice is less than 9, you win 10 units of money, otherwise you lose your investment.  Should you play this game? Answer the question by making a program that simulates the game 1000 times. Count how many times, out of the 1000, you would win this game in which case you'd win 10 bucks. Compare these winnings to your investment of 1000 dollars. Do you come out ahead?



