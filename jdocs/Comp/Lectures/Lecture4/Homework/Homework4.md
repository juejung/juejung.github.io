# Homework 4
Submit this homework in class on Tuesday.
I need two files:

  * R-scripts are submitted in one file called: ``Homework4.R``
  * Python-scripts are submitted in one file called: ``Homework4.py``

I need to be able to quickly run these scripts on my computer.

I will base your homework grade on my grading of 2 randomly selected homework exercises. So please make sure that you complete every homework 100% as you might otherwise end up with zero points.

For this homework you need to use the [Baltimore dataset](BaltimoreData.xlsx) posted on the website. Do all exercises in **R** and **Python**. Keep in mind that there are numerous ways to import data into **R** and **Python**.
The procedure I showed in class requires that you save  the data from within Excel as a .csv file. In Excel go to save as and switch the filetype from .xlsx to .cvs. This should save the Excel file as a .csv file (comma delimited values). 
Before you save it make sure that you remove all the extra formatting from the numbers in Excel, so that you don't run into problems importing them later into **R** or **Python**.
Marking numbers and then setting them to "general" in the ribbon should normally do the trick and remove extra formatting symbols like commas etc. 
For instance, a number that reads 16,216 should read 16216 after reformatting etc.

-------------------------------------------------------------------------------
## Exercise 1:

Import the data in a variable (matrix) called: myData 
Do this in **R** and **Python**.

-------------------------------------------------------------------------------
## Exercise 2:

Make summary statistics (e.g. mean, median, mode, and standard deviations) of all numerical variables. That is, print a table that says something like this: 

```
Variable 1:
==========
mean: mean(Variable 1)
median: median(variable 1)
mode: mode(variable 1)
standard deviation: stand.Dev.(Variable 1)

Variable 2:
==========
mean: mean(Variable 2)
median: median(variable 2)
mode: mode(variable 2)
etc.
```
Do this in **R** and **Python**.

-------------------------------------------------------------------------------
## Exercise 3:

Make a scatterplot of ``Median Income`` and ``Bachelors degree``. The latter variable measures the percentage of the population in the county that has a bachelors degree. Do this in **R** and **Python**.

-------------------------------------------------------------------------------
## Exercise 4:

Run a regression model of the following form: 

$$ JuvenileArrestRate = \beta_0 +
\beta1 Population + \beta_2 MedianIncome + \beta_3 Unemployment + \beta_4
Eduation + \beta_5 Poverty + \epsilon $$

Report a table with all coefficient estimates including p-values.

-------------------------------------------------------------------------------
## Exercise 5:

Run the model from **Exercise 4** again, but this time replace ``Population`` with a categorical variable for county size. You should make 3 categories here: small counties, middle sized counties, and large counties. A small county is defined as a county with a population smaller than $6,500$. A mid size county has a population between $6,500$ and $10,000$ and a large size county has a population larger than $10,000$ people. Make dummy variables and include those into your regression.
Review how to make dummies etc. from your stats notes or from the brief introduction of this class.