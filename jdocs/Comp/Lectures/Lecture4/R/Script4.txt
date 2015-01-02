#-------------------------------------------------------------------------------
# Author: Juergen JUng
# Date  : 22 July 2012
#-------------------------------------------------------------------------------
rm(list=ls()) # Remove almost everything in the memory
library(foreign)
library(matlab)

print("-------------- START ----------------")
setwd("C:/Dropbox/Towson/Teaching/3_ComputationalEconomics/Lectures/Lecture4")

print(paste("Today is",format(Sys.time(), "%a %b %d %X %Y")),quote=FALSE)   #Printing today's date & current time
print(paste("My current working directory is:",getwd()),quote=FALSE)        #Printing the current R working directory

tic()          # Start timer
# ------------------------------------------------------------------------------

# --------------------------------------------------------
# A. Read-data and making graphs
# --------------------------------------------------------

# Read in small data from .csv file
mydata <- read.csv("Lecture_4_Excel_a.csv", header=T)
View(mydata)
mydata$X = mydata$Frequency/sum(mydata$Frequency)
View(mydata)

# [1] Bar chart
barplot(mydata$Frequency, main = "Barplot", xlab = "Categories", 
        ylab = "Absolute frequencies" , ylim = c(0, 100), names.arg = mydata$Area)
   # write this graps into a .pdf file and save it in a subfolder
   pdf(file="./R/Graphs/Fig1_R.pdf")
   barplot(mydata$Frequency, main = "Barplot", xlab = "Categories", 
        ylab = "Absolute frequencies" , ylim = c(0, 100), names.arg = mydata$Area)
   dev.off()

# [2] Pie chart
lbls = paste(mydata$Area, round(mydata$X,4)*100)  # add percent to labels 
lbls = paste(lbls,"%",sep="")                     # add % to labels
pie(mydata$X, main = "Pie chart", labels = lbls)


# [3] Histogram
mydata <- read.csv("Lecture_4_Excel_b.csv", header=T)
View(mydata)
hist(mydata$Height,main="Histogram of Height")

# [4] Boxplots
boxplot(mydata$Height,ylab="Height")


# -----------------------------------------------------------
# B. Summary statistics
# -----------------------------------------------------------
# ------------------------------------------
# [1] Measures of central tendency
# ------------------------------------------
mydata <- read.csv("Lecture_4_Excel_b.csv", header=T)
View(mydata)

n = length(mydata$Height)
sum(mydata$Height)/n           # average
# or simply
mean(mydata$Height)

# Median
median(mydata$Height)

# Mode (value with highest frequency)
mode(mydata$Height)

summary(mydata$Height)

# ------------------------------------------
# [2] Measures of dispersion
# ------------------------------------------
range(mydata$Height)           # returns smallest a largest element
diff(range(mydata$Height))     # returns (largest-smallest)

sum((mydata$Height-mean(mydata$Height))^2)/n      # population variance
sum((mydata$Height-mean(mydata$Height))^2)/(n-1)  # sample variance
var(mydata$Height)
sqrt(var(mydata$Height))
sd(mydata$Height)

sd(mydata$Height)/mean(mydata$Height)             # CV ... coefficient of variation

# ------------------------------------------
# [3] Measures of relative standing
# ------------------------------------------
quantile(mydata$Height,0.25)
quantile(mydata$Height,c(0.25,0.5,0.75))
quantile(mydata$Height)
IQR(mydata$Height)             # Inter quartile rante: Q3-Q1 or P_75-P_25



# -----------------------------------------------
# [4] Measures of linear relationship
# -----------------------------------------------

# --------------------------------
# [4.1] Covariance
# --------------------------------
n = length(mydata$Age)
x = mydata$Age
y = mydata$Height

sum((x-mean(x))*(y-mean(y)))/n           # Population covariance
sum((x-mean(x))*(y-mean(y)))/(n-1)       # sample covariance
# or simply
cov(x,y)

# --------------------------------
# [4.2] Correlation coefficient
# --------------------------------
cov(x,y)/(sd(x)*sd(y))
# or simply
cor(x,y)

# --------------------------------
# [4.3] Regression line
# --------------------------------

# -------------------------
# Example 1: Simple example
# -------------------------
x = (1:8)
y = c(6,1,9,5,17,12,14,15)
res = lm(y~x)  # runs regression

# Plot scatterplot with least squares trend line
plot(x, y,main="Regression: y = beta0 + beta1*x +eps")
abline(res)
# R^2: Coefficient of determination
summary(res)

# Prediction: size of 8.5 will produce a math score of ...
betas = coef(res)
cat("Prediction for y of x=8.5 is:", sum(betas * c(1,8.5)))

# -------------------------
# Example 2: More real data
# -------------------------
# OLS with categorical (dummy variables)
res = lm(mydata$AverageMathSAT ~ mydata$Height + mydata$Age + as.factor(mydata$Female) + as.factor(mydata$Race))   # type res to see output table

# R^2: Coefficient of determination
summary(res)

# Prediction: size of 8.5 will produce a math score of ...
betas = coef(res)
sum(betas * c(1,2.5,22,1,0,0,1,0))



# -----------------------------------------------------------------------------
toc()       # Stop timer

