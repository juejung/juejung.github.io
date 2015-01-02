
# A Import data and standard statistics functionality in Python


# 1 Read in small data set from a comma separated (.csv) file

We use the ```csv.reader()``` command to read in the data file **Lecture_4_excel_a.csv**. This command is part of the library ```csv```. In addition we load some of the other libraries that we have used in the past.

```python
import time                     # Imports system time module to time your script
from pylab import *             # Imports numpy, scipy, and matplotlib etc.
from scipy import stats as st
import csv                      # Imports .csv file reader
close('all')  # close all open figures

# Read in small data from .csv file
# Filepath
filepath = '../'
# In windows you can also specify the absolute path to your data file
# filepath = 'C:/Dropbox/Towson/Teaching/3_ComputationalEconomics/Lectures/Lecture4/'

# ------------- Load data --------------------
data =[]  # Define empty list for data reading
for row in csv.reader(open(filepath+"Lecture_4_Excel_a.csv"), delimiter=','):
    data.append(row)    # read data row by row

# Let's have a look at it, it's a nested list
data

```
```

```


The data is currently saved in a  **list** called ```data```. Before we do any math-type operations with the data we want to extract the data from a **list** into an numerical **array**.

```python

# Split data into header and values
header      = data[0]        # first row contains headers of data
print header
groupNv     = []
groupv      = arange(1,6,1)  # make a vector from 1,2,...,5
freqv       = zeros((5,1),float)
for i in range(1,6):
    print i
    freqv[i-1]  = data[i][1]
    groupNv.append(data[i][0])
```
```

```

Variable header is a list that contains the **label** of our data. Compare the raw data file **Lecture_4_excel_a.csv** by opening it with a simple text editor. The data has a column of words and a column of numbers, the later are the absolute frequencies of the various groups. We read the words into a **list** called ```groupNv``` and the numbers into a **vector** called ```freqv```.
We use a **for loop** to "loop" over our data set. We start with the second row, so the iterator ```i``` will start at 1. Remember that this skips the first row in the data list, as the first row is indexed as 0.
In order to build a vector we first define it and fill it with zeros using ```freqv = zeros((5,1),float)```. We can then read through the data file (i.e. second column) and assign the values from ```data``` to our vector ```freqv``` using ```freqv[i-1]  = data[i][1]```.
In order to get the names our of the data file (i.e. the first column) we first assign an empty list ```groupNv     = []``` and then **append** one-by-one the strings from the first column in ```data``` to the list ```groupNv``` using  ```groupNv.append(data[i][0])```.
If you like to see the content of any of your lists or vectors just print them interactively by typing the following into the command line in **Spyder**: ```print freqv``` or ```print groupNv```.

We next generate a new variable called ```X``` that contains the relative frequencies.

```python
xv = copy(freqv/sum(freqv)) # calculate relative frequencies   
```
```

```


# 2 Making simple graphs from our data

## 2.1 Bar chart

We first make a bar chart of the absolute frequencies.

```python
fig1 = figure()
bar(groupv,freqv, align='center')
# Annotate with text
xticks(groupv, groupNv)
for i, val in enumerate(freqv):
    text(i+1, val/2, str(val), va='center', ha='center', color='white')
ylabel('%')
title('Relative frequency table')
show()   
savefig('./Graphs/fig1.pdf') 
```
```

```

This simple command plots the barchart into a window and saves it as **fig1.pdf** into a subfolder called ```Graphs```. Don't forget to first make this subfolder, otherwise ```Python``` will throw an error when it can't find the folder.

## 2.2 Pie chart
We next make a pie chart using the relative frequencies stored in vector ```xv```.

```python
fig2 = figure()
pie(xv, labels=groupNv, shadow=True)
# Annotate with text
title('Relative frequency table')
show() 
```
```

```

## 2.3 Histogram
Next we use a new data file called **Lecture_4_Excel_b.csv**. This data file contains data on height age and other variables. We first make a histogram of the continuous variable Height.

```python
data =[]
for row in csv.reader(open(filepath+"Lecture_4_Excel_b.csv"), delimiter=','):
    data.append(row)    # read data row by row
#print data
header = data[0]
   
height = zeros((len(data)-1,1),float)   
for i in range(1,len(height)+1):
    #print i
    height[i-1]  = data[i][0]
#print height    

# Initialize
N = len(height) # number of obs.
B = 8           # number of bins in histogram

# ------------- now we make the histogram -----
fig3 = figure()
prob, bins, patches = hist(height, bins=B, align='mid' )
# Annotate with text
for i, p in enumerate(prob):
    percent = int(float(p)/N*100)
    # only annotate non-zero values
    if percent:
        text(bins[i], p, str(percent)+'%', rotation=45, va='bottom', ha='center')
xlabel('Height groups')
ylabel('Number of obs')
title('Histogram of Height')
xlim(min(height),max(height))
show()
```
```

```

The actual command for the histogram is ```hist```. It returns three variables ```prob```, ```bins```, and ```patches```. We use them in the following to add information to the histogram.


## 2.4 Boxplots
A boxplot of height is made as follows:

```python
fig4 = figure()
boxplot(height)
# Annotate with text
title('Boxplot of Height')
show()
```
```

```

-----------------------------------------------------------
# 3. Summary statistics

We next go through some basic summary statistics.

## 3.1 Measures of central tendency

We first calculate the mean, median and mode. Note that ```mode``` is part of the ```stats``` package wich was imported as ```st``` using: ```from scipy import stats as st```. Now we have to add ```st``` to the mode command: ```st.mode(height)``` in order to call it.

```python
N = len(height)   # Number of observations (sample size)
print " -----------------------------------------"  
# Mean - Median - Mode
print "Mean(height)= " + str(mean(height))
print "Median(height)= " + str(median(height))
print "Mode(height)= " + str(st.mode(height)) # Mode (value with highest frequency)

```
```

```


We can also just summarize a variable using the ```st.describe``` command from the ```stats``` package.

```python
# Summary stats
print "Summary stats: " + str(st.describe(height))
```
```

```


## 3.2 Measures of dispersion

We now calculate the range, variance and standard deviations. Remember that for variance and standard deviation there is a distinction between population and sample.

```python
print "Range= " + str(max(height)-min(height))   # returns smallest a largest element
print "Population variance = " + str(sum((height-mean(height))**2)/N)    # population variance
print "Sample variance     = " + str(sum((height-mean(height))**2)/(N-1))       # sample variance
print "Pop.   standard dev = " + str(sqrt(sum((height-mean(height))**2)/N))
print "Sample standard dev = " + str(sqrt(sum((height-mean(height))**2)/(N-1)))
#or simply
print "Pop. standard dev = " + str(std(height))
```
```

```


## 3.3 Measures of relative standing

Percentiles are calculated as follows:

```python
print "1 quartile (25th percentile) = " + str(st.scoreatpercentile(height, 25))
print "2 quartile (50th percentile) = " + str(st.scoreatpercentile(height, 50))
print "3 quartile (75th percentile) = " + str(st.scoreatpercentile(height, 75))
# Inter quartile rante: Q3-Q1 or P_75-P_25
print "IQR = (P75-P25) = " + str(st.scoreatpercentile(height, 75)-st.scoreatpercentile(height, 25))
```
```

```



---------------------------------------------------------
# 4 Measures of linear relationship

## 4.1 Covariance

We first load two variables ```height``` and ```age```.
```python
data =[]
for row in csv.reader(open(filepath+"Lecture_4_Excel_b.csv"), delimiter=','):
    data.append(row)    # read data row by row
#print data
header = data[0]
   
height  = zeros((len(data)-1,1),float)   
age     = zeros((len(data)-1,1),float)   
for i in range(1,len(height)+1):
    #print i
    height[i-1] = data[i][0] 
    age[i-1]    = data[i][3] 
```
```

```

Now we calculate the covariance.

```python
n = len(age)
x = age
y = height

print "Population covariance= " + str(sum((x-mean(x))*(y-mean(y)))/n)   # Population covariance
print "Sample covariance= " + str(sum((x-mean(x))*(y-mean(y)))/(n-1))   # sample covariance
```
```

```



## 4.2 Correlation coefficient

```python
print "Correlation coefficient= " + str((sum((x-mean(x))*(y-mean(y)))/n)/(std(x)*std(y)))
```
```

```


## 4.3 Regression line

### Example 1: Simple example

We first generate some data. A variable ```x``` and a variable ```y```.

```python
# Define data. 2 vectors x and y
x = arange(1,9,1)
y = array([6,1,9,5,17,12,14,15])
```
```

```


We fist make a **scatterplot** with least squares trend line: $$y = \beta_0 + \beta_1 * x + \epsilon$$.

```python
p = polyfit(x,y,1)
print "p = " + str(p)

# --- scatterplot
fig4 = figure()
title('Linear regression with polyfit()')
plot(x,y, 'o', label = 'data')
plot(x,polyval(p,x),'-', label = 'Linear regression')
legend(loc='best') 
show()
```
```

```


We then run the same regression using a more general method called ```ols``` which is embedded in the ```myOLS.py``` script which you can download from my website. Here is the [myOLS.txt](./Python/myOLS.txt).
Keep in mind that before using it, you have to change the extension from .txt to .py!! Save it into the same folder where you have your script file.
When calling the ```ols``` function you need to add the module name in front of it: ```myOLS.ols()```.

```python
import myOLS
mymodel = myOLS.ols(y,x,'y',['x1'])
mymodel.b               # return estimated coefficients
mymodel.p               # return coefficient p-values
mymodel.summary()       # print results
```
```

```


Finally, we use the model to make a prediction of ```y``` when ```x=8.5```.

```python
betas =mymodel.b   # extract slope coefficients
print "Prediction of y for x=8.5 is: " + str(sum(betas * array([1,8.5])))
```
```

```

-------------------------
### Example 2: OLS with categorical (dummy variables)

The next example is a bit more involved as we increase the number of explanatory variables. In addition, some explanatory variables are categorical variables. In order to use them in our OLS regression we first have to make so called **dummy** variables (i.e. indicator variables that are either 0 or 1).
In **Python** this is more involved than in **R** and requires a loop and if-then commands.
We again load the data, this time a whole bunch of variables.


```python
data =[]
for row in csv.reader(open(filepath+"Lecture_4_Excel_b.csv"), delimiter=','):
    data.append(row)    # read data row by row
#print data
header = data[0]
   
y  = zeros((len(data)-1,1),float)   
x  = zeros((len(data)-1,7),float)
   
for i in range(1,len(height)+1):
    #print i
    y[i-1,0]            = data[i][2] # AverageMathSAT
    
    x[i-1,0]    = data[i][0] # height
    x[i-1,1]    = data[i][3] # age
    x[i-1,2]    = data[i][4] # d_female
    if data[i][6] == 'Hisp':  x[i-1,3] = 1 # d_hispanic
    if data[i][6] == 'Mex':  x[i-1,4] = 1 # d_mexican
    if data[i][6] == 'Oth': x[i-1,5] = 1 # d_other
    if data[i][6] == 'Wht': x[i-1,6] = 1 # d_white

print shape(x)
print shape(y)
```
```

```

We next use ```ols``` again to run the regression. At the end we make a prediction based on some values for the independent variables ```x1```, ```x2```, etc.


```python
mymodel = myOLS.ols(y[:,0],x[:,0:7],'y',['height','age','d_female','d_hisp','d_mex','d_other','d_white'])
mymodel.b               # return estimated coefficients
mymodel.p               # return coefficient p-values
mymodel.summary()       # print results

## Prediction: size of 2.5, 22 years of age, female, race=other will produce a math score of ...
betas = mymodel.b
print "Prediction: " +str(sum(betas * array([1,2.5,22,1,0,0,1,0])))

```
```

```

