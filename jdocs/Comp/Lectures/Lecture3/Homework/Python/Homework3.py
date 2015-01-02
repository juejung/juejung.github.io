# Homework 3

from pylab import *
close('all')  # close all open figures

# -----------------------------------------------------------------------------
# Exercise 1
# -----------------------------------------------------------------------------
n = 26
i = 1
oddNum=[]
while i<=n:  
    # tests whether or not the number is odd using modulo division %%
    if i%2==1:   
        oddNum.append(i)  
        #print str(i)   # prints the odd numbers
    i = i + 1   #increments c to prevent infinite loop
print str(oddNum)

# -----------------------------------------------------------------------------
# Exercise 2
# -----------------------------------------------------------------------------
a = [1, 3, 5, 7, 11]
b = [13, 17]
c = a + b  # c becomes the list a with the appended values in list b
print c    # prints the list c as [1, 3, 5, 7, 11, 13, 17]
b[0] = -1  #changes the first value in b to -1.
d = [e+1 for e in a]  # runs a loop through the values of a and adds 1 to each and assign that to vector d
print d  
d.append(b[0] + 1)  # appends the value of b[0]+1, which is 0, to the list d
print d
d.append(b[-1] + 1) # appends the last value of b to the list d and also adds 1, which makes it 18
print d
print d[-2:]        # prints last 2 elements in d


# -----------------------------------------------------------------------------
# Exercise 3
# -----------------------------------------------------------------------------
# Original program
# s = 0; k = 1; M = 100     # need floating point numbers
# while k < M:              # k needs to include 100 and therefore should be k<=100
    #s += 1/k               # translate to float, otherwise results might be zero
# print s                   # will never be done due to infinite loop


# Corrected program
s = 0.0; k = 1.0; M = 100  #changed values to floating point numbers to get correct calculations
while k <= M:               # include 100
    s += (1.0/k)            # add float 1.0/.... to make sure you don't get zero as result
    #print s                # prints intermediate values for method two
    k=k+1                   # increment k to prevent infinite loop
print s

# -----------------------------------------------------------------------------
# Exercise 4
# -----------------------------------------------------------------------------
s = 0.0
for k in range(1,M+1):
    #print k
    s=s+(1.0/k)
print str(s)

# -----------------------------------------------------------------------------
# Exercise 5
# -----------------------------------------------------------------------------
q=[['a','b','c'],['d','e','f'],['g','h']]
# 1
print q[0][0]       # prints a
# 2
print q[1]          # prints second sublist ['d','e','f']
# 3
print q[-1][-1]     # last element in last sublist: prints h
# 4
print q[1][0]       # second sublist, first element: prints d
# 5
print q[-1][-2]     # last sublist, the last two elements

# -----------------------------------------------------------------------------
# Exercise 6
# -----------------------------------------------------------------------------
# Lotka-Volterra predator-prey equations
br = 0.04       # growth rate of rabbits
dr = 0.0005     # death rate of rabbits due to predation
df = 0.2        # death rate of foxes
bf = 0.1        # efficiency of turning predated rabbits into foxes
x  = 4000       # starting number of rabbits
y  = 100        # starting number of foxes
xv =[]      # define empty vector
yv =[]      # define empty vector
while x > 3500:     
# print "x =", x, " y =", y, "\n"
    x_new=(1.0+br)*x - dr*x*y
    y_new=(1.0-df)*y + bf*dr*x*y
    xv.append(x_new)
    yv.append(y_new)
    x=x_new
    y=y_new
xv=array(xv)  #converts xv list into an array to graph
yv=array(yv)  #converts yv list into an array for graph    
tv=arange(1,len(xv)+1)  #gives comparison to time for graph


fig1=figure()
subplot(3,1,1)
plot(tv, xv,'-o')   
title('Rabbits')        # Gives graph a title
xlabel('Time')          # labels x-axis
ylabel('Population')    # labels y-axis

subplot(3,1,2)
plot(tv, yv,'-')    
title('Foxes')          # Gives graph a title
xlabel('Time')          # labels x-axis
ylabel('Population')    # labels y-axis

subplot(3,1,3)
plot(tv, xv,'-o', tv, yv,'-')   # xv shows as blue line with dots and yv appears as a green line with no dots
title('Predator vs. Prey')     
xlabel('Time')  
ylabel('Population') 
ylim(0,4500)            # sets plot limits for y vals
legend(('Rabbits','Foxes'),'middle right', shadow=True)  #legend appears in the middle and to the ri

show()








