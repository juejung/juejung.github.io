# -*- coding: utf-8 -*-
import numpy as np
import scipy.linalg as sp
import pandas as pd
import matplotlib.pyplot as plt

def f_stochroot(A,p):
    # Algorithm based on: J. Chhatwal, S. Jayasuriya, and E. H. Elbasha, “Changing
    # Cycle Lengths in State-Transition Models: Challenges and Solutions,” Medical
    # Decision Making, vol. 36, no. 8, pp. 952–964, 2016.
    
    # This script executes the distance minimization algorithm for a transition
    # matrix A with desired pth root. The function nrootmat is the function
    # used earlier to calculate the pth root of the matrix.
    
    Ap= sp.fractional_matrix_power(A,p)
    
    (n, m) = np.shape(A)
    if (n != m):
        raise ValueError('A is not a square matrix')
    #end
    
    b = np.zeros((n,n))
    
    for j in range(n):
        a = np.real(Ap[j,:])

        while True:
            if np.sum(a)==1 and np.min(a)>=0:
                b[j,:] = a
                break
            #end
            
            jlambda = (np.sum(a)-1)/n
            x = a - jlambda*np.ones((1,n))[0]
        
            if np.min(x)>=0:
                b[j,:]=x 
                break
            #end
    
            for k in range(n):
               
                x[k] = max(0, x[k])
            #end
    
            a = x
        #end
    #end
    return b
#end


def main():
    print('------------------------------------');
    print('        Test Start                  ');
    print('------------------------------------');

    A = np.array([[0.7, 0.3, 0], [0, 0.6, 0.4], [0,0,1]])
    print(A)
    
    print('\n Time period = 2');
    B = f_stochroot(A, 2)
    print(B)
    
    print('\n Time period = 1/12');
    B = f_stochroot(A, (1./12))
    print(B)
    
    print('\n Time period = 1/2');
    B = f_stochroot(A, (1./2))
    print(B)

if __name__ == "__main__":
    main()



