# -*- coding: utf-8 -*-
#! /usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

print(' ------------------------------------- ')
print('Question 1')
print(' ------------------------------------- ')
xv=np.array([3.2,6,7.8,1,3,2.5,100])

for i in range(len(xv)):
    if xv[i] < 4:
        xv[i] = xv[i] + 5

print('xv = ', xv)

xv=np.array([3.2,6,7.8,1,3,2.5,100])
for i in range(len(xv)):
    if 2 < xv[i] < 5:
        xv[i] = -1

print('xv = ', xv)

xv=np.array([3.2,6,7.8,1,3,2.5,100])
# Calculate the mean
jsum = 0
for i in range(len(xv)):
    jsum = jsum + xv[i]

xmean = jsum/len(xv)

#Prefill sqv vector with zeros - same length as xv vector
sqv = np.zeros(len(xv))
for i in range(len(xv)):
    sqv[i] = (xv[i]-xmean)**2

print('sqv = ', sqv)
print()
print(' ------------------------------------- ')
print('Question 2')
print(' ------------------------------------- ')

def my_cov_f(xv,yv):
    n = len(xv)
    # Calculate means for each vector
    mx = 0
    my = 0
    for i in range(n):
        mx = mx + xv[i]
        my = my + yv[i]
    meanx = mx/n
    meany = my/n

    # Prefill vector with same length as xv with zeros
    jsum = 0
    for i in range(n):
        jsum = jsum + (xv[i]-meanx)*(yv[i]-meany)

    cov = jsum/(n-1)
    return cov

print('Test function')

xv = np.array([1.,5.5,7.2,4.2,-2.7,-5.4,8.9])
yv = np.array([0.1,1.5,1.8,-4.2,2.7,-9.4,-1.9])
cov = my_cov_f(xv, yv)
print('cov = ', cov)

print()
print(' ------------------------------------- ')
print('Question 3')
print(' ------------------------------------- ')
xv = np.linspace(-4,4,100)
yv = np.zeros(len(xv))
for i in range(len(xv)):
    if xv[i] < 0:
        yv[i] = np.log(np.abs(xv[i]))
    elif 0<= xv[i] < 2:
        yv[i] = -xv[i]
    else:
        yv[i] = xv[i]**2/(3 - xv[i])

plt.plot(xv,yv)
#plt.show()

print()
print(' ------------------------------------- ')
print('Question 4')
print(' ------------------------------------- ')
A = np.array([[1.2,3.4,10.3],[2,8,78],[45,-36,8]])
Nrow, Ncol = A.shape

for i in range(Nrow):
    for j in range(Ncol):
        if j == i:
            A[i,j] = -5
print('A = {}'.format(A))

A = np.array([[1.2,3.4,10.3],[2,8,78],[45,-36,8]])
Nrow, Ncol = A.shape
for i in range(Nrow):
    for j in range(Ncol):
        if i != j:
            A[i,j] = 100
print('A = {}'.format(A))

print()
print(' ------------------------------------- ')
print('Question 5')
print(' ------------------------------------- ')
personList = [['Julie', 'married', 35000, 'Jack'], \
              ['Angie', 'not married', 55000, 'na'],\
              ['Sarah', 'married', 45000, 'Jim'],\
              ['Jack', 'married', 35000,'Julie'],\
              ['John',  'not married', 25000, 'na'],\
              ['Jim', 'married', 35000, 'Sarah']]

# Define empty list, so we can append to it
marriedList = []
for i in range(len(personList)):
    if personList[i][1] == 'married':
        marriedList.append(personList[i])

print('Content of marriedList')
print('----------------------')
for person in marriedList:
    print(person)

# Define empty list, so we can append to it
householdIncome = []
for i in range(len(personList)):
    marriageStatus = personList[i][1]
    personIncome = personList[i][2]
    personSpouse = personList[i][3]

    if marriageStatus == 'married':
        # Search rest of list for partner
        for j in range(i+1, len(personList)):
            if personSpouse == personList[j][0]:
                # Found spouse, now assign spouse income
                spouseIncome = personList[j][2]
                # Add income together into one household income and store
                hhincome = personIncome + spouseIncome
                householdIncome.append(hhincome)
    else:
        # Person is not married, just assign person income into HH income
        hhincome = personIncome
        householdIncome.append(hhincome)

print()
print('Household       Total Income')
print('----------------------------')
for i in range(len(householdIncome)):
    print("{}                {:5.2f}".format(i+1, householdIncome[i]))


