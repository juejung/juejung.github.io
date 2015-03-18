# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import myfunctions as myfun
# If you work with user written functions that are saved in separate script
# files you need to make sure that you are always using the latest version of
# the functions. When developing your programs I would recommend you always put
# these two lines on top of your codes to ensure that it always reloads the
# latest version of your function definitions. Once the functions are debugged
# and correct, you can comment the next two lines out.
import imp
imp.reload(myfun)

print("---------------------------------------------------------------")
print("Question 1")
print("---------------------------------------------------------------")
xv = np.array([3, 2,6, 7.8, 1, 3, 2.5])
for i,x in enumerate(xv):
    if x < 4:
        xv[i] = xv[i] + 5
print("xv = ", xv)

xv = np.array([3, 2,6, 7.8, 1, 3, 2.5])
for i,x in enumerate(xv):
    if (2 <= x <= 5):
        xv[i] = -1
print("xv= ", xv)

xv = np.array([3, 2,6, 7.8, 1, 3, 2.5])
sqv = (xv - np.sum(xv))**2

print("---------------------------------------------------------------")
print("Question 2")
print("---------------------------------------------------------------")
xv = np.array([1., 5.5, 7.8, 4.2, -2.7, -5.4, 8.9])
yv = np.array([0.1, 1.5, 0.8, -4.2, 2.7, -9.4, -1.9])
print('The covariance with option 1 = {}'.format( myfun.cov(xv, yv)))
print('The covariance with option 2 = {}'.format( myfun.cov2(xv, yv)))
print('The covariance with option 3 = {}'.format( myfun.cov3(xv, yv)))

print("---------------------------------------------------------------")
print("Question 3")
print("---------------------------------------------------------------")
xv = np.linspace(-4, 4, 200)
# Create empty yv vector that we can the fill with the function values
yv = np.zeros(len(xv))
for i,x in enumerate(xv):
    yv[i] = myfun.f(x)

fig, ax = plt.subplots()
ax.plot(xv, yv, 'b.')
ax.set_title('Function')
plt.show()

print("---------------------------------------------------------------")
print("Question 4")
print("---------------------------------------------------------------")
A = np.array([[1.2, 3.4, 10.3],[2, 8, 78], [45, -36, 8]])
row, col = A.shape

for i in range(row):
    A[i,i] = -5
print(A)

A = np.array([[1.2, 3.4, 10.3],[2, 8, 78], [45, -36, 8]])

for i in range(row):
    for j in range(col):
        if (i != j):
            A[i,j] = 100
print(A)

print("---------------------------------------------------------------")
print("Question 5")
print("---------------------------------------------------------------")
# Since the class definition is in a different file, we needed to import it
# So don't forget the myfun. prefix!!
firstnames = ['Jim', 'Jack', 'Michelle', 'Ron', 'Coline']
lastnames = ['Dorn', 'Boon', 'Mills', 'Woods', 'Jung']
genders = ['male', 'male', 'female', 'male', 'female']
statuses = ['junior', 'freshman', 'senior', 'sophomore', 'junior']
gpas = [3.8, 3.2, 2.0, 3.5, 3.4]

student_list =[]
for fname,lname,gen,stat,gpa in zip(firstnames,lastnames,genders,statuses,gpas):
    # Create students and append them to list
    student_list.append(myfun.Student(fname,lname,gen,stat,gpa))

studytime_list = [60, 100, 40, 300, 1000]
for i,stime in enumerate(studytime_list):
    student_list[i].show_myself()
    print("Study time is {}".format(stime))
    print("Now let the guy study ...")
    student_list[i].study_time(stime)

print(" ")
print("New GPA's: ")
for x in student_list:
    x.show_myself()

