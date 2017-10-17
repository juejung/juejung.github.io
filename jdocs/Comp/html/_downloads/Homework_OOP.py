# Homework 6 - OOP

#------------------------------------------------------------------------------
# Exercise 1
#------------------------------------------------------------------------------

class Student(object):
    def __init__(self, firstname = 'J', lastname = 'J', gender = 'na', \
                 status= 'freshman', gpa = 0):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.status = status
        self.gpa = gpa

    def showMyself(self):
        print('--------------------------------------')
        print('First name: {}'.format(self.firstname))
        print('Last name:  {}'.format(self.lastname))
        print('Gender:     {}'.format(self.gender))
        print('Status:     {}'.format(self.status))
        print('GPA:        {}'.format(self.gpa))
        print('--------------------------------------')

    def study_time(self, studytime = 0.0):
        self.gpa = self.gpa + m.log(studytime/60)
        # Check whether it's too large
        if self.gpa > 4:
            self.gpa = 4

        return(self.gpa)

#------------------------------------------------------------------------------
# Exercise 2
#------------------------------------------------------------------------------
# Now that the class object is defined, we can start using it by making (or
# instantiating) student-objects

first_list = ['Mike','Jim', 'Jack', 'Jane', 'Mary']
last_list = ['Barnes','Nickerson','Indabox','Miller','Scott']
gend_list = ['Male','Male','Male', 'Female', 'Female']
stat_list = ['freshman','sophomore', 'junior', 'senior', 'senior']
gpa_list = [4.0, 3.0, 2.5, 3.6, 2.7]

# Create student object
student_list = []
for i, (firstname, lastname, gender, status, gpa) in enumerate(zip(first_list,last_list,gend_list,stat_list,gpa_list)):
    student_list.append(mf.Student(firstname=firstname, lastname=lastname, gender=gender, status=status, gpa=gpa))

for i in range(len(student_list)):
    print('Student {}:'.format(i+1))
    print(student_list[i].showMyself())

#------------------------------------------------------------------------------
# Exercise 3
#------------------------------------------------------------------------------
studytime_list =[60,100,40,300,1000]
for i in range(len(studytime_list)):
    student_list[i].study_time(studytime_list[i])
    print("{}'s new GPA is {:.2f}".format(student_list[i].firstname, student_list[i].gpa))


