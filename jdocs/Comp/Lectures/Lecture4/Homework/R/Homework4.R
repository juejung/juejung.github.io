# Homework 4

rm(list = ls())  # Remove almost everything in the memory
library(foreign)
library(matlab)

cat("-------------- START ----------------")
setwd("C:/Dropbox/Towson/Teaching/3_ComputationalEconomics/Lectures/Lecture4/Homework")

# -----------------------------------------------------------------------------
# Exercise 1
# -----------------------------------------------------------------------------

# Read in small data from .csv file
mydata <- read.csv("BaltimoreData.csv", header=T)
#View(mydata)


# -----------------------------------------------------------------------------
# Exercise 2
# -----------------------------------------------------------------------------
nameListStr = c('Population',' MedIncome', 'Unemployed', 'FamPov', 'BachDegree', 'JuvArrest', 'Homicides', 'LifeExp')

for (i in 1:length(nameListStr)) {
    cat(i,"\n")
    cat("======================= \n")
    cat(nameListStr[i], "\n")
    cat("======================= \n")
    cat("Mean:      ", sapply(mydata[i+1],mean), "\n")
    cat("Median:    ", sapply(mydata[i+1],median), "\n")
    cat("Mode:      ", sapply(mydata[i+1],mode), "\n")
    cat("Stand.Dev: ", sapply(mydata[i+1],sd), "\n")
}
    
# -----------------------------------------------------------------------------
# Exercise 3
# -----------------------------------------------------------------------------
plot((mydata$Bachelors.degree*100), mydata$Median.Income, main="Median Income vs. Percentage of Bachelor's Degrees",xlab="Percentage with Bachelor's Degree", ylab="Median Income")

# -----------------------------------------------------------------------------
# Exercise 4
# -----------------------------------------------------------------------------
res = lm(mydata$Juvenile.Arrest.Rate ~ mydata$Population + mydata$Median.Income + mydata$Unemployed + mydata$Bachelors.degree + mydata$Families.in.Poverty)

summary(res)

# -----------------------------------------------------------------------------
# Exercise 5
# -----------------------------------------------------------------------------
# Generate categorical variable

mydata$Size = 'M'  # for mid size county
mydata$Size[mydata$Population<6500]  = 'S' # replace with S, when pop<6500
mydata$Size[mydata$Population>10000]  = 'L'
#View(mydata)

res2 = lm(mydata$Juvenile.Arrest.Rate ~ mydata$Median.Income + mydata$Unemployed + mydata$Bachelors.degree + mydata$Families.in.Poverty+as.factor(mydata$Size))
summary(res2)
