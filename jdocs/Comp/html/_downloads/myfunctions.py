# -*- coding: utf-8 -*-
import numpy as np
#------------------------------------------------------------------------------
# Question 2
#------------------------------------------------------------------------------
# Option 1
def cov(xv, yv):
    n = len(xv)
    mu_x = np.average(xv)
    mu_y = np.average(yv)
    accum = 0
    for i in range(len(xv)):
        accum = accum + (xv[i] - mu_x)*(yv[i] - mu_y)
    return accum/(n-1)

# Option 2
def cov2(xv, yv):
    n = len(xv)
    mu_x = np.sum(xv)/n
    mu_y = np.sum(yv)/n
    accum = 0
    for x, y in zip(xv,yv):
        accum = accum + (x - mu_x)*(y - mu_y)
    return accum/(n-1)

# Option 3: Vectorized version
def cov3(xv, yv):
    return np.sum((xv-np.average(xv))*(yv-np.average(yv)))/(len(xv)-1)


#------------------------------------------------------------------------------
# Question 3
#------------------------------------------------------------------------------
def f(x):
    if x < 0:
        return np.log(np.abs(x))
    elif (x >= 0) & (x < 2):
        return -x
    else:
        return (x**2)/(3-x)

#------------------------------------------------------------------------------
# Question 5
#------------------------------------------------------------------------------
class Student(object):
    """This is the Student class. It's the top class."""

    def __init__(self, firstname, lastname, gender, status, gpa):
        """Initialize the student-object with first and last name variables etc.
        """
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.status = status
        self.gpa = gpa

    def show_myself(self):
        """Method: show_myself()
        prints out all the variables."""
        print("\n")
        print("-------------------------------")
        print("Name: {}".format(self.firstname), "{}".format(self.lastname))
        print("Gender: {}".format(self.gender))
        print("Status: {}".format(self.status))
        print("GPA: {}".format(self.gpa))
        print("-------------------------------")

    def study_time(self, studytime):
        """Method: study_time()
        Will increment the gpa of the student according to the formula:
        gpa = gpa + log(studytime)"""
        self.gpa += np.log(studytime)
        if self.gpa > 4.0:
            self.gpa = 4.0

