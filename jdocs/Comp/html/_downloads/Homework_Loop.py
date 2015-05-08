# Homework 2: Branching and looping
# -----------------------------------------------------------------------------
# Exercise 1
# -----------------------------------------------------------------------------
print('------ Exercise 1 -------')
n = 10
i = 1
oddNum=[]
while i<=n:
    # tests whether or not the number is odd using modulo division %%
    if i%2==1:
        oddNum.append(i)
        #print str(i)   # prints the odd numbers
    i = i + 1   #increments c to prevent infinite loop
print(oddNum)


# Here is another solution:
n = 9
x = -1
oddList = []
while (x < n):
    x = x + 2
    oddList.append(x)

print("Oddlist = {}".format(oddList))
print()
# -----------------------------------------------------------------------------
# Exercise 2
# -----------------------------------------------------------------------------
print('------ Exercise 2 -------')
a = [1, 3, 5, 7, 11]
b = [13, 17]

c = a + b  # c becomes the list a with the appended values in list b
print(c)    # prints the list c as [1, 3, 5, 7, 11, 13, 17]

b[0] = -1  #changes the first value in b to -1.
d = [e+1 for e in a]  # runs a loop through the values of a and adds 1 to each and assign that to vector d
print(d)

d.append(b[0] + 1)  # appends the value of b[0]+1, which is 0, to the list d
print(d)

d.append(b[-1] + 1) # appends the last value of b to the list d and also adds 1, which makes it 18
print(d)
print(d[-2:])        # prints last 2 elements in d
print()

# -----------------------------------------------------------------------------
# Exercise 3
# -----------------------------------------------------------------------------
print('------ Exercise 3 -------')
# Original program
# s = 0; k = 1; M = 100     # need floating point numbers
# while k < M:              # k needs to include 100 and therefore should be k<=100
    #s += 1/k               # translate to float, otherwise results might be zero
# print s                   # will never be done due to infinite loop


# Corrected program
s = 0.0; k = 1.0; M = 100
while k <= M:               # include 100
    s += (1.0/k)            # add float 1.0/.... to make sure you don't get zero as result
    #print(s)               # prints intermediate values for method two
    k = k+1                   # increment k to prevent infinite loop
print(s)
print()

# -----------------------------------------------------------------------------
# Exercise 4
# -----------------------------------------------------------------------------
print('------ Exercise 4 -------')
s = 0.0; k = 1.0; M = 100
for k in range(1, M+1):
    s = s+(1.0/k)
print(s)
print()

# -----------------------------------------------------------------------------
# Exercise 5
# -----------------------------------------------------------------------------
print('------ Exercise 5 -------')
q=[['a','b','c'],['d','e','f'],['g','h']]
# 1
print(q[0][0])       # prints a
# 2
print(q[1])          # prints second sublist ['d','e','f']
# 3
print(q[-1][-1])     # last element in last sublist: prints h
# 4
print(q[1][0])       # second sublist, first element: prints d
# 5
print(q[-1][-2])     # last sublist, the last two elements
print()

# ------------------------------------------------------------------------------
# Exercise 6
# ------------------------------------------------------------------------------
print('------ Exercise 6 -------')
klist = ['john', 'james', 'jim', 'jason', 'jill', 'jane', 'jinn']
stud_numbers = [345, 123, 876, 234, 198, 456, 876]
print("-----------------------------")
print("    Student Database")
print("-----------------------------")
print("Name:            ID number: ")
print("-----------------------------")
for k, s in zip(klist, stud_numbers):
    # The \t add tab stops into the output
    print('{0} \t \t {1}'.format(k, s))
print("-----------------------------")


