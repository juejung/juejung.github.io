# http://computationallegalstudies.com/2009/10/11/programming-dynamic-models-in-python/

# A simple SIR model written in Python
#Jon Zelner
#University of Michigan
#October 8, 2009


#Ok, so first we're going to import our random number and plotting libraries
# this is Python's standard random number library. 
#For heavy-duty applications you'll want to use something else 
#(like Scipy) but for this example, this will be more than adequate.

import random

#Now we're going to import pylab, which lets us do plotting and a 
#bunch of other useful stuff. Notice the 'as' on the import. 
#This means that when we want to use pylab tools, we have to
#reference them as pl.blah where 'blah' is the name of the tool.

#Although this entails a little more typing than 
#'from pylab import *', it makes your code more readable
#in the long run. It's commented out for the time being,
#but if you have Matplotlib installed and want to plot your 
#output, go ahead and uncomment it.

import pylab as pl

#Ok, so now we're going to set the initial state of our model.
S = 1000 #this is the number of susceptibles
I = 1 #we seed the outbreak with one infectious individual
R = 0 #and no one has recovered yet

#here, we calculate the total number of individuals in the system 
#we'll be using this for reference as we go along
N = S+I+R

#Python is pretty informal about types - integers, floating point numbers, etc.,
#but if you try to divide two integers by each other, you will get zero as a result. 

#So, here, we convert N to a float so that we can use it in division without 
#rounding errors.
N = float(N)

#Now we're going to set the simulation clock to zero.
t = 0

#Here are the model transmission parameters

#Infectivity (probability of generating a new case at each step)
#This is often called 'beta', and we'll abbreviate it here by 'b'
b = .09


#Probability of recovering @ each step. Similarly, this is often called
#gamma, and we will abbreviate it here to 'g'.
g = .05

#Here, we make some lists to  keep track of number of individuals 
#in each state at each time step. These will be useful at the end 
#of the run when we want to see what the model actually did.

sList = [] #we'll keep the number of susceptible individuals at each step on this list
iList = [] #the number of infected individuals here
rList = [] #the number who have recovered here
newIList = [] #and we'll use this to record the number of newly infected people on each step.


#Ok, so now we're done setting up the initial state of the model and it's time to actually
#get down to running it!

#We make a loop that runs as long as there are still infectious individuals
while I > 0:
    # so far, no one has been infected yet
    newI = 0
    
    #there is a single random trial for each susceptible individual
    for i in range(S):
        #here, we're using a frequency dependent transmission process;
        #density dependence would be b*I
        
        #we use the method 'random.random()' to draw uniformly distributed numbers
        #in the range [0,1).
        if random.random() < b*(I/N):
            newI += 1
        
        #to switch to density dependence, comment out the block above and
        #uncomment the following:
        #if random.random() < b*I:
        #    newI += 1
    
    #Now we're going to see how many individuals recovery on this step.    
    recoverI = 0
    for i in range(I):
        if random.random() < g:
            recoverI += 1
    
    #Then, we wait to the all of the final accounting at the end of the step.
    #This is because we're making the assumption that all events on a step
    #happen simultaneously, so that individuals are infected on this step 
    #at the same time as others recover.
    
    S -= newI
    I += (newI - recoverI)
    R += recoverI
    
    #Then we add these values to their respective lists
    sList.append(S)
    iList.append(I)
    rList.append(R)
    newIList.append(newI)
    
    #This prints the time to standard out - usually the terminal you're running from -
    # and increments the timestep.
    print('t', t)
    t += 1

#We'll drop out of the loop above when we satisfy the stopping condition, I = 0 
#and then print out the values to the terminal
print('sList', sList)
print('iList', iList)
print('rList', rList)
print('newIList', newIList)

#And if you want to plot the time series of how many people were
#infectious on each step (and have matplotlib installed),
#go ahead and uncomment these lines:

pl.figure()
pl.plot(iList)
pl.show()