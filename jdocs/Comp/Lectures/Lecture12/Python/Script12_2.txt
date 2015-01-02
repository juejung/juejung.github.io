# http://computationallegalstudies.com/2009/10/21/programming-dynamic-models-in-python-coding-efficient-dynamic-models/

#a simple object-based SIR model written in Python
#Jon Zelner
#University of Michigan
#October 20, 2009
ic-models/


#import 'sirWithClasses' to use the components of this model as you wish
#or just run this script as 'python sirWithClasses.py' to do a sample model run

import random
import heapq
import scipy
from scipy import random, stats

class simpleSIRModel():
    
    #this is the constructor for the model object
    def __init__(self, b = .1, g = .01, S = 1000, I = 1, R = 0):
        #we use keyword arguments so we can set one parameter at a time
        #and so we have default values for demo runs
        self.b = b
        self.g = g
        
        #use these lists to keep track of how many 
        #people are in each state at each time
        self.sList = []
        self.iList = []
        self.rList = []
        self.newIList = []
        
        #this will be used for a more 
        #efficient implementation of the recovery process
        self.recoveryTimesHeap = []
        
        #setting up the initial conditions
        self.S = S
        self.I = I
        self.R = R
        
        self.N = S+I+R
        self.N = float(self.N)
        self.t = 0
        
        #telling the model we're starting 
        #with I initial infecteds
        for i in xrange(I):
            self.infectAgent()
       
# heap-based method for recovering agents using an 
#arbitrary distribution of recovery times

    def infectAgent(self):
        #uncomment for exponentially distributed recovery times
        #same as looping over and drawing a random number every time, but more efficient
        #use 1/gamma to get the expected duration of infectiousness
        #and just add it to the current time
        recoveryTime = self.t + scipy.random.exponential(1/self.g)
        
        #these are other distributions to give you some 
        #idea of what happens when you try different
        #assumptions about recovery times
        
        #lognormal with mean 1/g
        #recoveryTime = self.t + scipy.random.lognormal(mean = scipy.log(1/g), sigma = scipy.log(20) )
        ##this is to make sure that we don't get anyone recovering in the past or at the moment of 
        ##infection
        #if recoveryTime <= self.t:
        #    recoveryTime = self.t + 1
        
        #gamma distributed times with mean 1/g
        #shape = 10.0
        #recoveryTime = self.t + scipy.random.gamma(shape, scale = 1/(shape*self.g))
        
        #normally distributed with mean 1/g
        #recoveryTime = self.t + scipy.random.normal(1/self.g, 10)
        #if recoveryTime <= self.t:
        #    recoveryTime = self.t + 1
        
        #constant
        #recoveryTime = self.t + (1/g)
        
        #we use the 'heappush' method from heapq to 
        #put the next recovery time on the heap
        #if you add them using some other method, 
        #it is important to use heapq.heapify(heap)
        #to maintain it's heap-ness
        heapq.heappush(self.recoveryTimesHeap, recoveryTime)
        
        return 1
    
    def recoverAgents(self):
        recoverI = 0
        if len(self.recoveryTimesHeap) > 0: #make sure we have folks to recover
            while self.recoveryTimesHeap[0] <= self.t: #top item will always be the smallest, i.e., nearest
                                                       #to self.t
                                                       
                #all we need to know is that the top item on the list
                #should have recovered by now, so we pop it off the list
                #using heapq.heappop and let it disappear into the magical 
                #land of garbage collection
                heapq.heappop(self.recoveryTimesHeap)
                recoverI += 1
                
                #if we run out of individuals to recover, just stop looping
                if len(self.recoveryTimesHeap) == 0:
                    break
    
        return recoverI

#simplest (and inefficient) way to recover individuals 
#with exponentially distributed recovery times
#    
#    def infectAgent(self):
#        #this is just a wrapper that increments the count of infected
#        #individuals in the model
#        return 1
#    
#    def recoverAgents(self):
#        #drawing a random value on each step for every infected
#            recoverI = 0
#            for i in range(self.I):
#                if random.random() < self.g:
#                    recoverI += 1
#            return recoverI
    
    #this method contains the real guts of the model
    def run(self):
        #while individuals are still infectious, we run the process
        while self.I > 0:
            newI = 0
            for i in range(self.S):
                if random.random() < self.b*(self.I/self.N):
                    newI += self.infectAgent()
            #let the model take care of any mechanics involved in recovering agents
            #and record the number who will recover @ the end of this step
            recoverI = self.recoverAgents()
            
            #do the bookkeeping
            self.S -= newI
            self.I += (newI - recoverI)
            self.R += recoverI
            
            #and keep track of how many individuals were in each state on this step
            self.sList.append(self.S)
            self.iList.append(self.I)
            self.rList.append(self.R)
            self.newIList.append(newI)
            print('t', self.t, 'numS', self.S, 'numI', self.I)
            
            #don't forget to increment the time!
            self.t += 1
            
            
        return [self.sList, self.iList, self.rList, self.newIList]

if __name__ == '__main__':
    
    #transmission parameters
    b = .6 / 24.0
    g = .5 / 24.0
    
    #initial conditions
    S = 2000
    I = 1
    
    import pylab as pl
    myModel = simpleSIRModel(b = b, g = g, S = S, I = I)
    simpleModelResults = myModel.run()
    numMassActionCases = sum(simpleModelResults[3])
    pl.plot(simpleModelResults[1], label = 'mass action outbreak; '+ str(numMassActionCases) + ' cases')
    pl.show()