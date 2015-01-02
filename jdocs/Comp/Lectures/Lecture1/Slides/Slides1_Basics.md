# 1 A brief introduction to R and Python

We use **R** and **Python** for a number of reasons:
 * They are both open source and therefore free
 * They are platform independent, that is, this software runs on Windows or
   Linux PC's as well as Apple computers
 * Both programming languages have a large user base and are still growing in
   popularity. You will therefore be able to find a lot of material online in
   case you run into trouble and need expert help and/or good sources
 * A recent [survey](http://www.r-bloggers.com/surveys-continue-to-rank-r-1-for-data-mining/) ranked them number one and two in data mining applications - translation: knowing these languages will help you on the job market

## 1.1 R
You first have to install R and Python. You can find the download page for R here: [http://cran.r-project.org/](http://cran.r-project.org/) I recommend you first install R for your system. Then download the integrated development environment (IDE) [R-Studio](http://rstudio.org/). These two programs together provide a very nice work environment for R that will allow you to be more productive. Downloading the Windows, Mac, or Linux version is straightforward. I could get it to run on all 3 platforms in about 10 minutes.

## 1.2 Python

Next you have to download Python. If you are running Linux or Apple, some version of Python is already installed. However, these basic Python versions miss some of the important scientific packages that you will still have to install. The most important ones are ```numpy```, ```scipy```, and ```matplotlib```. A recent package called ```pylab``` combines them all. If you "google" these packages you should be able to find them on the internet. They need to be installed.

I also recommend that you install an IDE for Python. One that is very amenable for scientific computation is called Spyder. You can download it from here: [http://code.google.com/p/spyderlib/](http://code.google.com/p/spyderlib/). Spyder is part of most Linux repositories and can easily be installed from there. On the website you also find the program for the Mac OS system.

I personally work on Windows and Linux and I run all programs used in this class on both platforms.
I sometimes have sporadic access to a Mac and found that R and R-Studio work without any problems.
The get the full scientific Python distribution on the Mac might be a bit tricky though. So let's look at how to install Python on the three platforms.

* If you run Windows, then the easiest way to install Python and Spyder and all sorts of other useful packages for scientific computing is to install Python XY from [http://code.google.com/p/pythonxy/](http://code.google.com/p/pythonxy/). This is a simple one click installation process that installs everything! Python XY is the program we use on the lab computers.

* If you run Linux, I will assume that you already know what you are doing. Look for the scientific packages in the Linux repositories. They are easy to find and any package management software will be able to install them including all dependencies. 

* If you are working on a Mac a good option might be the product suite of Enthought that seems to combine the most important scientific packages in Python for the Mac. Go to their [website](http://www.enthought.com/products/edudownload.php) and look for the free academic license. You can get it by supplying your towson email address. Since I don't work with a Mac, I cannot report any first hand experience with it. 


-------------------------------------------------------------------------------
# 2 First steps in R and Python

-------------------------------------------------------------------------------
## 2.1 Simple calculations


-------------------------------------------------------------------------------
### 2.1.1 Calculations in **R**


After installation, open **R-Studio** and **Spyder** and try some of the following. In **R-Studio** type the following into the command line:



```r
x = 2
y = 3
x + y
```

```
## [1] 5
```



Then try the following:

Operation    |   Expression
---------    |   ----------
Subtraction: |   `x - y` 
Division:    |   `x / y` 
Multiplication: | `x * y`  
Power:       |   `x ^ y`
Square root: |   `sqrt(x)`

-------------------------------------------------------------------------------
### 2.1.2 Calculations in **Python**

Next open **Spyder** and try a similar thing in **Python**. Note that the power function is not ``^`` but ``**``. Also in Python we need to import the Math module in order to use certain math functions like ``sqrt()`` etc. 

```python
import math
x=2
y=3
print x + y
print x**y
print math.sqrt(x)
```
```
5
8
1.41421356237
```


-------------------------------------------------------------------------------
## 2.2 Script files

Before we go on, let's save all our commands in a so called Script file. These are basically text files that contain all commands in one big "laundry list" that we can then execute all at once.
In order to open such a script file in R-Studio simply click on ``File`` $latex \rightarrow$ ``New`` and choose "R Script". Copy/paste the above commands into this script file and save it under a name of your choosing. Note that the file has the extension .R which indicates that it is an R script file. 
You can then edit this file at will and add commands etc. If you want to run or execute the script file simply click the ``Source`` button on top of your editor window. You can also execute the script file line by line. Simply put the cursor into the line you'd like to execute and type ``CTRL+Enter`` or click on the ``Run`` icon on top of your editor window.

In order to do the same in **Python**, click on File $latex \rightarrow$ New and copy paste your Python code from above into this file. Give it a name and save it somewhere. You'll see that this file has extension .py which indicates that it is a Python script file.

In order to run it simply click on the green button with the "running man symbol" on top of your editor window. If you'd like to execute just one line, mark the line and click on the "running man symbol" to the right of the first green button.

-------------------------------------------------------------------------------
### 2.2.1 Homework and script files

For the remainder of the class I highly recommend that you always use script files. When you submit your homework you are always required to submit 2 script files per homework, one in **R** and one in **Python**. This will help me to quickly run your code and evaluate your results.

-------------------------------------------------------------------------------
### 2.2.2 Comparison summary between **R** and **Python**

You can find a quick comparison sheet that points to the differences in **R** and **Python** [here](./RvsNumPy.html). [This](./RvsNumPy.pdf) is the pdf version of the same thing.
This will come in handy when you translate **R** into **Python** code or vice
versa. You will be required to this often on the homeworks.



-------------------------------------------------------------------------------
## 2.3 Vectors and matrices

-------------------------------------------------------------------------------
### 2.3.1 Vectors and matrices in **R**

A vector is a list of numbers that we can do "math" with. The numbers in the vector are indexed, so that we can access them.
Note that vector indexing in **R** starts with 1 not with zero. So R counts the first element in a vector as element 1, the second as element 2, etc. So if we try to recall an element at the "zero" position, then R will throw an error. 
Here are some examples. Vectors ``x`` ``y`` ``year`` and ``names`` are assigned as follows


```r
# You can document your script files using the ``#`` symbol. This works
# for R and Python and allows you to add commentary to your codes.

x = c(1, 3, 4, 9)
y = c(9.2, 0.3, 3.2, 2.8)
year = seq(2000, 2003, by = 1)  # seq(from, to, by = stepsize)
somev = seq(2000, 2003, length = 10)  # seq(from, to, length = nr. of steps)
names = c("Tom", "Dick", "Harry", "Patrick")

x[0]
```

```
## numeric(0)
```

```r
# X[0] # this will cause an error, so I comment it out!
x[1]
```

```
## [1] 1
```

```r

# If we'd like nicer output, we can use the 'R print command'
cat("x[1]= ", x[1], "\n")
```

```
## x[1]=  1 
```

```r
cat("x[2]= ", x[2], "\n")
```

```
## x[2]=  3 
```

```r
cat("names[1]= ", names[1], "\n")
```

```
## names[1]=  Tom 
```

```r
cat("names[3]= ", names[3], "\n")
```

```
## names[3]=  Harry 
```



Note the difference in simply writing ```x[1]``` vs. ```cat("x[1]= ", x[1], "\n")```. The second combined the string ```"x[1]= "``` with the number saved at position x[1]. The last command ```"\n"``` adds a new line to the output.

-------------------------------------------------------------------------------
### 2.3.2 Vectors and matrices in **Python**

In **Python** we first need to import some important packages so that Python understands basic numerical procedures and definitions, like vectors and matrices. Also, note the difference in syntax and the fact that Python starts numbering the elements with 0 and not 1! So if you want to access the first element in a vector "x" you'd need to type: "x[0]":

```python
from pylab import *
 #from numpy import *
 #from scipy import *

x = [1,3,4,9]
y = [9.2, 0.3, 3.2, 2.8]
 # Note that if you like a vector: 2000,2001,2002,2003 you need to write 
 # the arange command with the upper limit+1
year  = arange(2000,2004,1)         # arange(from, to, stepsize)
somev = linspace(2000,2003,10)      # linspace(from, to, nr. of steps)
names = ["Tom", "Dick", "Harry", "Patrick"]  
print "year= " + str(year)
print "x[0]= " + str(x[0])
print "x[1]= " + str(x[1])
print "x[2]= " + str(x[2])
print "names[1]= " + str(names[1])
print "names[3]= " + str(names[3])
```
```
year= [2000 2001 2002 2003]
x[0]= 1
x[1]= 3
x[2]= 4
names[1]= Dick
names[3]= Patrick
```

Note, that in **Python** we used the ```print``` command and combined a string ```"a= "``` together with another string ```str(a)``` (**str** translates a number into a string, i.e. a word) and then prints the combined "word".

-------------------------------------------------------------------------------
## 2.4 Doing math with vectors and matrices

-------------------------------------------------------------------------------
### 2.4.1 Math in **R**

In **R** we can add, subtract, multiply, and divide vectors element-by-element. Again define two vectors as


```r
x1 = c(1, 3, 4, 9)
x2 = c(2, 5, 6, 3)
#
x1 + x2
```

```
## [1]  3  8 10 12
```

```r
x1 - x2
```

```
## [1] -1 -2 -2  6
```

```r
x1 * x2
```

```
## [1]  2 15 24 27
```

```r
x1/x2
```

```
## [1] 0.5000 0.6000 0.6667 3.0000
```




Matrices are "two dimensional" vectors. In **R** we define a matrix as



```r
a = rbind(c(2, 3), c(4, 5))
b = rbind(c(2, 6), c(1, 3))
a
```

```
##      [,1] [,2]
## [1,]    2    3
## [2,]    4    5
```

```r
b
```

```
##      [,1] [,2]
## [1,]    2    6
## [2,]    1    3
```

```r
a * b
```

```
##      [,1] [,2]
## [1,]    4   18
## [2,]    4   15
```

```r
a - b
```

```
##      [,1] [,2]
## [1,]    0   -3
## [2,]    3    2
```



If you want to generate matrices filled with either zeros or ones of a particular size in **R** you can use the following:


```r
matrix(0, 3, 5)  # makes a 3x5 matrix of zeros
```

```
##      [,1] [,2] [,3] [,4] [,5]
## [1,]    0    0    0    0    0
## [2,]    0    0    0    0    0
## [3,]    0    0    0    0    0
```

```r
matrix(1, 4, 3)  # makes a 4x3 matrix filled with ones
```

```
##      [,1] [,2] [,3]
## [1,]    1    1    1
## [2,]    1    1    1
## [3,]    1    1    1
## [4,]    1    1    1
```

```r
diag(1, 3)  # Identity matrix (=matrix with 1 in main diagonal)
```

```
##      [,1] [,2] [,3]
## [1,]    1    0    0
## [2,]    0    1    0
## [3,]    0    0    1
```




-------------------------------------------------------------------------------
### 2.4.2 Math in **Python**

In **Python** we need to let the interpreter know that we want to work with a vector and not with a list. The command **array** from the **numpy** package does just that. When we import the **pylab** package, **numpy** is imported as part of it.

```python
from pylab import *
 # Element-by-element operations
x1 = array([1,3,4,9])
x2 = array([2,5,6,3])
print "x1= " + str(x1)
print "x2= " + str(x2)
print " ---------------- "
print "x1+x2= " + str(x1+x2)
print "x1*x2= " + str(x1*x2)
```
```
x1= [1 3 4 9]
x2= [2 5 6 3]
 ---------------- 
x1+x2= [ 3  8 10 12]
x1*x2= [ 2 15 24 27]
```


Matrices are "two dimensional" vectors. In **Python** we write

```python
from pylab import *
a = array([[2,3],[4,5]])
b = array([[2,6],[1,3]])

print "a= " + str(a)
print "b= " + str(b)
print " ---------------- "
print "a*b= " + str(a*b)
print "a-b= " + str(a-b)
```
```
a= [[2 3]
 [4 5]]
b= [[2 6]
 [1 3]]
 ---------------- 
a*b= [[ 4 18]
 [ 4 15]]
a-b= [[ 0 -3]
 [ 3  2]]
```


If you want to generate matrices filled with either zeros or ones of a particular size in **Python** you can use the following:


```python
from pylab import *
a = zeros((3,5),float)
b = ones((4,3),float)
c = identity(3)

print "a= " + str(a) 
print " ---------------- "
print "b= " + str(b)
print " ---------------- "
print "c= " + str(c)
```
```
a= [[ 0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.]]
 ---------------- 
b= [[ 1.  1.  1.]
 [ 1.  1.  1.]
 [ 1.  1.  1.]
 [ 1.  1.  1.]]
 ---------------- 
c= [[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]
```


-------------------------------------------------------------------------------
# In class exercises

 1. Generate a vector with entries from 1 to 20, stepsize 0.5
 2. Divide the first 10 entries by 5
 3. Replace the last entry with the value from the first entry
 4. Sort the vector from largest to smallest element
 
