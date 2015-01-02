
# Basic programming techniques

# 1 Branching

The ```if``` command can be used to check whether a certain condition is true. If it is true, then we can assign a certain chain of commands for this eventuality. If the condition is wrong, we can branch off our program into another direction and assign different commands. So we can basically branch our program into two (or more) seperate directions.
Here is a simple example. We first draw some random number between 0 and 1 using the ```random()``` command. We then check whether the number is smaller or larger than 0.5. For each eventuality we can then assign a string of commands to be executed.

In Python it is very important to get the "indentation" right. So all the commands that we want to be executed after the if statement need to "indented" by 4 spaces (just his the tab key once). Python does not use the curley brackets ```{}``` that R uses in the if-statements and for- loops.

```python
from pylab import *             # Imports numpy, scipy, and matplotlib etc.
x = random(1)  # draw a random number between 0 and 1
if (x > 0.5):
    print("Number x="+str(x)+" is greater than 0.5")
else:
    print("Number x="+str(x) +" is smaller than or equal to 0.5")
```
```
Number x=[ 0.59409555] is greater than 0.5
```


We next branch the program into 3 seperate directions depending on 3 mutually exclusive conditions.


```python
from pylab import *             # Imports numpy, scipy, and matplotlib etc.
x = random(1)
y = random(1)

if (x > y):
    print("X is greater than Y")
elif (x==y):
    print("X is equal to Y")
elif (x < y):
    print("X is smaller than Y")
```
```
X is greater than Y
```



# 2 For loops

If we want to do repeated tasks we use loops insteady of copy/pasting the same series of commands.


## Loop 1
Here is a simple first example. We first assign a vector with values 1, 3, 5, 7, and 9 as values. We then "loop" through all the values of this vector and print them. In addition, we add up all the values of this vector one by one. The command ```for (x in xv)``` assigns ```x``` equal to each value of ```xv``` one by one and we can then use ```x``` itself in each iteration. With this we can step through all the values of our vector and assign certain operations to each value.


```python
from pylab import *             # Imports numpy, scipy, and matplotlib etc.
xv = arange(1, 9, 2)
sumx = 0

for x in xv:
    sumx = sumx + x  # adds up the elements in vector xv
    print("X =" + str(x))
    print("sum(x) = " + str(sumx))

# or simply
print("sum(xv)= " + str(sum(xv)))
```
```
X =1
sum(x) = 1
X =3
sum(x) = 4
X =5
sum(x) = 9
X =7
sum(x) = 16
sum(xv)= 16
```

The same operation can be done much simpler, of course, using the ```sum(xv)``` command. 


## Loop 2

Here is another example. We write a loop that calculates the factorial of a number: $latex 3!$. Remember that 
$$3! = 1 * 2 * 3$$.
In order to make this happen we write a loop that sets i = 1, 2, and 3 and multiplies it with the product of the previous round. The variable ```n_fac``` stores the product from each round.

```python
from pylab import *             # Imports numpy, scipy, and matplotlib etc.
n = 6
n_fac = 1

for i in range(n):
    print("i = ", i)
    n_fac = n_fac * i

print("The factorial of " + str(n) + " is: " + str(n_fac))
```
```
('i = ', 0)
('i = ', 1)
('i = ', 2)
('i = ', 3)
('i = ', 4)
('i = ', 5)
The factorial of 6 is: 0
```



## Loop 3

Finally, here is an example where we loop through the values of a vector again. In each round we reach the value of the vector and print it. 

```python
from pylab import *             # Imports numpy, scipy, and matplotlib etc.
xv = linspace(1,9, 20)
print("xv="+str(xv))
```
```
xv=[ 1.          1.42105263  1.84210526  2.26315789  2.68421053  3.10526316
  3.52631579  3.94736842  4.36842105  4.78947368  5.21052632  5.63157895
  6.05263158  6.47368421  6.89473684  7.31578947  7.73684211  8.15789474
  8.57894737  9.        ]
```


We now start the loop and pick each value of this vector one-by-one. The command ```length``` tells us how many arguments are in vector ```xv``` and then lets the loop run from 1 to the totoal number of arguments in ```xv```.

```python
from pylab import *             # Imports numpy, scipy, and matplotlib etc.
xv = linspace(1,9, 20)
for i in range(len(xv)):
    print "i= " +str(i)
    print "xv[i]= " + str(xv[i])
```
```
i= 0
xv[i]= 1.0
i= 1
xv[i]= 1.42105263158
i= 2
xv[i]= 1.84210526316
i= 3
xv[i]= 2.26315789474
i= 4
xv[i]= 2.68421052632
i= 5
xv[i]= 3.10526315789
i= 6
xv[i]= 3.52631578947
i= 7
xv[i]= 3.94736842105
i= 8
xv[i]= 4.36842105263
i= 9
xv[i]= 4.78947368421
i= 10
xv[i]= 5.21052631579
i= 11
xv[i]= 5.63157894737
i= 12
xv[i]= 6.05263157895
i= 13
xv[i]= 6.47368421053
i= 14
xv[i]= 6.89473684211
i= 15
xv[i]= 7.31578947368
i= 16
xv[i]= 7.73684210526
i= 17
xv[i]= 8.15789473684
i= 18
xv[i]= 8.57894736842
i= 19
xv[i]= 9.0
```


We next plot the 2 vectors using the ```plot``` command.

```python
from pylab import *             # Imports numpy, scipy, and matplotlib etc.
#xv = linspace(1,9, 20)
yv = sqrt(xv)
fig1 = figure()

plot(xv,yv, "o", xv,xv, ":")
ylim(0,9)
title("Simple plot of two vectors")
show()
```
```
Traceback (most recent call last):
  File "<string>", line 3, in <module>
NameError: name 'xv' is not defined
```


# 3 While loop

The while loop runs and keeps repeating to do something until a certain stopping condition is met.

## While loop 1

In the first example we let the iterations run as long as the value of variable x is smaller than 10. In every iteration we increase x by one unit, so that in effect the loop gets repeated 9 times.

```python
from pylab import *             # Imports numpy, scipy, and matplotlib etc.
x = 0
y = 0
while (x < 10):
    y = y + x
    print("X= " +  str(x) + " and Y= " + str(y))
    x = x + 1
```
```
X= 0 and Y= 0
X= 1 and Y= 1
X= 2 and Y= 3
X= 3 and Y= 6
X= 4 and Y= 10
X= 5 and Y= 15
X= 6 and Y= 21
X= 7 and Y= 28
X= 8 and Y= 36
X= 9 and Y= 45
```


Variable ```y``` calculates the cumulative sum of all numbers from 1 to 9, so that $latex y = 0+1+2+...+9$.

## While loop 2

In this last example we calculate how long it takes to repay a loan. The longer you wait to repay the loan, the more interest is accumulated and added to the outstanding debt. The key formula in this example is: $$latex debt_{tomorrow} = debt_{today}*(1 + interest rate) - payments_{today}$$


```python
from pylab import *             # Imports numpy, scipy, and matplotlib etc.
r           = 0.11  # annual interest rate
period      = 1./12  # time between repayments in years (i.e. monthly repayments)
debt_initial= 1000  # initial debt
payments    = 12    # amount repaid each period

mytime = 0
debt = debt_initial
while (debt> 0):
    mytime = mytime + period
    debt = debt*(1 + r*period) - payments

print("Loan will be repaid in: "+ str(mytime) + " years.")
```
```
Loan will be repaid in: 13.25 years.
```

