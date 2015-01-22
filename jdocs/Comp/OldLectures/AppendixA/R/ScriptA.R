# -------------------------------------------
# Call Fortran routines from R: 
# -------------------------------------------
library(matlab)

print("-------------- START ----------------")
rm(list=ls()) # Remove almost everything in the memory

# -----------------------------------------------------------------------------------
# 1. First run the pure R implementation
# -----------------------------------------------------------------------------------

func = function(x) {
   # Do someting time consuming
   jm = array(0,c(x,x))
   for (i in 1:x) {
      for (j in 1:x) {
         jm[i,j]=log(i+1.0)/1000^2 / (1.0+j)
      }
   }
   s=sum(sum(jm))
   return (s)
}


tic()
cat("sum(func(x))=",func(600),"\n")
toc()       # Stop timer

# -----------------------------------------------------------------------------------
# 2. Implement the slow routine in Fortran 90 and call it from Python
# -----------------------------------------------------------------------------------

# Write fortran.90 subroutine called 'f_func' and save it as: f_func_Source.f90
# Compile it with: 
# ....$: gfortran -c f_func.f90
# The run dllwrap:
# ....$: dllwrap --export-all-symbols f_func.o -o f_func.dll
# In order to use it in R code, import the module with:
#
# dyn.load("c:/.../.../f_func.dll")
# x1=100
# result=.C("f_func_", as.integer(length(x1)))
# -----------------------------------------------

# We automatize this now:
if (Sys.info()["sysname"]=="Windows") {
   #
   # ---------- Windows ------------------
   #
   wdir = 'C:/Dropbox/Towson/Teaching/3_ComputationalEconomics/Lectures/AppendixA/R'
   setwd(wdir)
   system("cmd dir", intern=TRUE)
   #system("gfortran -c f_func.f90")
   #system("dllwrap --export-all-symbols f_func.o -o myfunc.dll")
   system("gfortran -shared -o myfunc.dll f_func_Source.f90")
   dyn.load("myfunc.dll") # only works with R 32 bit
   # -------------------------------------
} else if (Sys.info()["sysname"]=="Linux") {
   #
   # ---------- Linux -------------------
   #
   wdir = '~/Dropbox/Towson/teaching/3_ComputationalEconomics/Lectures/AppendixA/R'
   setwd(wdir)
   system("ls", intern=TRUE)
   #system("gfortran -c f_func.f90")
   #system("R CMD SHLIB f_func.f90 -o myfuncs.so")
   system("gfortran -shared -o myfunc.so f_func_Source.f90")
   dyn.load("myfunc.so")
   # -------------------------------------
}   


# Check whether function is loaded
is.loaded('f_func')

tic()
.Fortran("f_func",as.integer(600),c=integer(1))
toc()