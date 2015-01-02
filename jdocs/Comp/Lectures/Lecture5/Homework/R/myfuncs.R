#------------------------------------------------------------------------------
# Exercise 1
#------------------------------------------------------------------------------
f_celsius = function(f) {
    c = (5.0/9.0)*(f-32.0) # the conversion equation
    return (c) # return the value  
}


f_fahrenheit = function(c) {
    f = c*(9.0/5.0)+32.0 # the conversion equation
    return (f) # return the value    
}    

#------------------------------------------------------------------------------
# Exercise 2
#------------------------------------------------------------------------------
f_pathlength = function(xv,yv) {
    # requires the input of two vectors: xv, yv
    L = 0
    i = 2
    while (i <= length(xv)) {
        L = L+ sqrt(((xv[i]-xv[i-1])^2)+((yv[i]-yv[i-1])^2)) #calculate the distance of each part of path
        i= i+1  # the update for the loop
    }
    return (L)    # return the value    
}

#------------------------------------------------------------------------------
# Exercise 3
#------------------------------------------------------------------------------
f_factorial = function(n) {
    f=1 #variable to store factorial
    if (n==0) {
        f=1    
    } else if (n==1) {
        f=1
    } else if (n>1) {
        for (i in (1:n)) {
            f=f*i
        }     
    }   
    return (f) # return value    
}


#------------------------------------------------------------------------------
#Exercise 4
#------------------------------------------------------------------------------
f_vecnorm = function(xv) {
    return (sqrt(sum(xv^2))) # returns the square root of the sum of squared elements    
}
    
#------------------------------------------------------------------------------  
# Exercise 5 
#------------------------------------------------------------------------------
# h(x,n)=1+x+x^2+x^3+...+x^n # the equation for reference
f_geomseries = function(x,n) {
    s = 0.0
    for (i in (0:(n))) {
        s=s+x^i  # adds up the series as in the formula
    }
    return (s) 
}
