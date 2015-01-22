# -*- coding: utf-8 -*-
"""
# =====================================================================
#
# Scriptfile Appendix A
# -------------------------
# Computational Economics
# (c) Juergen Jung, 2012
#
# =====================================================================

"""
import time
import os
import math
from pylab import *
import numpy

# -------------------------------------------
# Call external fortran routines to speed up code
# -------------------------------------------

close('all')  # close all open figure



print("-------------- START ----------------")

# -----------------------------------------------------------------------------------
# 1. First run the pure Python implementation
# -----------------------------------------------------------------------------------

def func(x):
    # Do someting time consuming
    jm = zeros((x,x),float)
    for i in range(x):
        for j in range(x):
            jm[i][j]=log(i+2.0)/1000**2 / (2.0+j)
    s=sum(jm)
    return s

start = time.clock()
print "sum(func(x))=" + str(func(600))
print "time passed: " + str(time.clock() - start)

# -----------------------------------------------------------------------------------
# 2. Implement the slow routine in Fortran 90 and call it from Python
# -----------------------------------------------------------------------------------

# Write fortran.90 subroutine called 'f_func' and save it as: f_func_Source.f90
# Compile it with: 
# ....$: gfortran -c f_func_Source.f90
# If there are array intent(in,out) variables the also run:
# ....$: !f2py intent(in,out) :: VAR
# The run f2py:
# ....$: f2py –c –m MODULENAME SOURCE.f90 --fcompiler=gnu95 --compiler=mingw32 
# So in our example, this is:
# ....$: f2py –c –m myFuncs f_func_Source.f90 --fcompiler=gnu95 --compiler=mingw32 
# In order to use it in Python code, import the module with
# import myFuncs
# We can now call functions and subroutines defined in this module: myFunc.f_func

os.chdir(str(os.getcwd()))
print "Working directory: " +str(os.getcwd())

# Compile the source code into .o file, just to check whether it's compiling
os.system('gfortran -c f_func_Source.f90')

if os.name=='nt':
    # windows: will generate a .pyd library called myFuncs
    os.system('f2py -c -m myFuncs f_func_Source.f90 --fcompiler=gfortran --compiler=mingw32')
elif os.name=='posix':
    # linux: will generate a .os library called myFuncs
    os.system('f2py -c -m myFuncs f_func_Source.f90 --fcompiler=gfortran')
    

import myFuncs

start = time.clock()
print "sum(func(x))=" + str(myFuncs.f_func(600))
print "time passed: " + str(time.clock() - start)
