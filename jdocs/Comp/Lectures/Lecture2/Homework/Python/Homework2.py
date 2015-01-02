# Homework 2

# -----------------------------------------------------------------------------
# Exercise 1
# -----------------------------------------------------------------------------
from pylab import *
close('all')  # close all open figures

Kv  = arange(0,21,1)
A   = 10.0
alph= 0.33
L   = 20.0
y1v  = A*(Kv**alph)*(L**(1-alph))

fig1=figure()
plot(Kv,y1v,"-o")
#show()

# -----------------------------------------------------------------------------
# Exercise 2
# -----------------------------------------------------------------------------
A    = 20  #I copied what I did above and changed the A variable. I also deleted unnecessary parts that were repeated.
y2v  = A*(Kv**alph)*(L**(1-alph))

plot(Kv,y2v,"-^")
legend(('A=10', 'A=20'),'lower right', shadow=True)
title('Production functions')
show()

# -----------------------------------------------------------------------------
# Exercise 3
# -----------------------------------------------------------------------------
Groc_Line=[] # create empty list

Groc_Line=['Steve','Russell','Alison','Liam']
print Groc_Line
print 'Barry gets in line.'
Groc_Line.append('Barry') # adds Barry
print Groc_Line
print 'Steve is served and leaves.'
Groc_Line.remove('Steve') # removes Steve
print Groc_Line
print 'Pam talks her way to the front of the line.'
Groc_Line.insert(0,'Pam')
print Groc_Line
print 'Barry gets impatient and leaves.'
Groc_Line.remove('Barry') # removes Barry
print Groc_Line
print 'Alison gets impatient and leaves.'
Groc_Line.remove('Alison') # removes Alison
print Groc_Line
print 'Russell is customer ', Groc_Line.index('Russell')+1, ' in line'


# -----------------------------------------------------------------------------
# Exercise 4
# -----------------------------------------------------------------------------
m       = 0.0 
sig     = 2.0
x       = 1.0
gauss   = (1.0/(sig*sqrt(2*pi)))*exp((-0.5)*((x-m)/sig)**2) 
print "f(x=1)= " + str(gauss) 

# -----------------------------------------------------------------------------
# Exercise 5
# -----------------------------------------------------------------------------
m       = 0.0 
sig     = 2.0
xv      = arange(-8.,8.,0.1) 
yv      = (1.0/(sig*sqrt(2.0*pi)))*exp((-0.5)*((xv-m)/sig)**2) 

fig2=figure()
plot(xv,yv)
title("Density of normal distribution")
show() 