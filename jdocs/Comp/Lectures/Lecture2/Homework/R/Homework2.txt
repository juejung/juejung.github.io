# Homework 2

rm(list = ls())  # Remove almost everything in the memory

# -----------------------------------------------------------------------------
# Exercise 1
# -----------------------------------------------------------------------------
Kv  = seq(0,5,by=0.1) 
A   = 10
alph= 0.33
L   = 20
y1v = A*(Kv^alph)*(L^(1-alph))

plot(Kv,y1v,'o',pch = 21,ylim = c(0, 250)) 

# -----------------------------------------------------------------------------
# Exercise 2
# -----------------------------------------------------------------------------
A   = 20
y2v = A*(Kv^alph)*(L^(1-alph))

lines(Kv,y2v,'o',pch = 22)
legend(0.5, 250, c("A=10", "A=20"), cex = 0.8, pch = 21:22, lty = 1:2)
title("Production functions")

# -----------------------------------------------------------------------------
# Exercise 3
# -----------------------------------------------------------------------------
rm(list = ls()) # Remove almost everything in the memory
cat('------------------------------- \n')
Grocery_Line  = c("Steve","Russell","Alison","Liam")
Grocery_Line
Grocery_Line  = c(Grocery_Line,"Barry") # add Barry
Grocery_Line
Grocery_Line  = Grocery_Line[-1]        # Steve leaves
Grocery_Line
Grocery_Line  = c("Pam",Grocery_Line)   # Pam talks her way to the front
Grocery_Line
Grocery_Line  = Grocery_Line[-length(Grocery_Line)] # Barry leaves
Grocery_Line
y=which(Grocery_Line=="Alison")         # returns index of Alison
Grocery_Line  = Grocery_Line[-y]        # Alison leaves
Grocery_Line
x=which(Grocery_Line=="Russell")        # returns Russell's position
cat("Russell is customer ", x, " in line.\n")

# -----------------------------------------------------------------------------
# Exercise 4
# -----------------------------------------------------------------------------
m       = 0
sig     = 2
x       = 1
gauss   = (1./(sig*sqrt(2*pi)))*(exp(-.5*((x-m)/sig)^2))

cat("f(x=1) =  ", gauss) 

# -----------------------------------------------------------------------------
# Exercise 5
# -----------------------------------------------------------------------------
m   = 0
sig = 2
xv  = seq(-8,8,0.1)
yv  = (1./(sig*sqrt(2*pi)))*(exp(-.5*((xv-m)/sig)^2))

plot(xv,yv,'o')
title("Density of normal distribution")