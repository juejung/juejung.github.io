# -----------------------------------------------------------------------------
# Exercise 1
# -----------------------------------------------------------------------------

# Simple solution
v1 = c(1,2,3,4,5,6,7,8,7,6,5,4,3,2,1)
# More elegant would be this here:
x=seq(1,8, by=1)
y=seq(7,1, by=-1)
v1=c(x,y)
cat('v1 = ', v1, "\n")

# Second vector simple
v2 = c(1,2,2,3,3,3,4,4,4,4,5,5,5,5,5)
# Or more elegant, how for such a short vector the extra work doesn't pay off
v2=c(rep(1,1),rep(2,2), rep(3,3), rep(4,4), rep(5,5))
cat('v2 = ', v2, "\n")

# Matrix
m1 = rbind(c(0,1,1),c(1,0,1),c(1,1,0))
m2 = rbind(c(0,2,3),c(0,5,0),c(7,0,0))
m1
m2

# -----------------------------------------------------------------------------
# Exercise 2
# -----------------------------------------------------------------------------

p=5.0  # 5% ! Do not use 0.05 here, otherwise the formula is incorrect.
A=1000.0
n=3
final_amount=A*(1.0+(p/100))^n 
cat("\n\n")
cat("The final amount is", final_amount, "euros")


# -----------------------------------------------------------------------------
# Exercise 3
# -----------------------------------------------------------------------------

# pi doesn't need to be imported in R
h = 5.0 # height 
b = 2.0 # base
r = 1.5 # radius
area_parallelogram = h*b
cat("The area of the parallelogram is" , area_parallelogram)
cat("\n")
area_square = b^2  # the power symbol in R is ^, in Python it's **
cat("The area of the square is" , area_square)
cat("\n")
area_circle = pi*r^2
cat("The area of the circle is" , area_circle)
cat("\n")
volume_cone = 1.0/3*pi*r^2*h
cat("The volume of the cone is" , volume_cone) #All of the print statements had to be translated from Python into R

# -----------------------------------------------------------------------------
# Exercise 4
# -----------------------------------------------------------------------------

# -------------------------------
# [4.1] 
# -------------------------------
x = pi/4
val_1 = sin(x)^2 + cos(x)^2 
cat("val_1= ", val_1) # The value turns out to be 1

# You can also try:
1 == sin(x)^2 + cos(x)^2
# The output of this will tell you whether the expression is true or false.
# Read about boolean type variables in your book if you want to know why this
# works

# -------------------------------
# [4.2] 
# -------------------------------
v0 = 3  # in m/s
t = 1   # in s
a = 2   # in m/s^2
s = v0*t + 1.0/2*(a*t^2) # In R you don't need to worry about 1/2 vs. 1.0/2.0, but
# it's good practice to do it anyway
cat("s= ", s)  

# -------------------------------
# [4.2] 
# -------------------------------
a = 3
b = 5
a2 = a^2 
b2 = b^2
eq1_sum = a2 + 2*a*b + b2 #added multiplication signs to 2ab
eq2_sum = a2 - 2*a*b + b2
eq1_pow = (a + b)^2
eq2_pow = (a - b)^2
cat("First equation:", eq2_sum %% eq2_sum) #Added extra % to find modulus
cat("\n")
cat("Second equation:", eq2_pow %% eq2_pow)
cat("\n")
# You can then do it again with
a = 3
b = 3

# A more elegant way is to use vector evaluation
a = c(3,3) 
b = c(5,3)
a2 = a^2
b2 = b^2
eq1_sum = a2 + 2*a*b + b2
eq2_sum = a2 - 2*a*b + b2
eq1_pow = (a + b)^2
eq2_pow = (a - b)^2
all.equal(eq1_sum, eq1_pow)
all.equal(eq2_sum, eq2_pow)
# or
eq1_sum == eq1_pow
eq2_sum == eq2_pow



# -----------------------------------------------------------------------------
# Exercise 5
# -----------------------------------------------------------------------------

# I printed the final results and checked
# whether it sums to zero. You can see that it does.
a=2
b=1
c=2   # This exercise has a complex number, which calls for the complex() command.
q=complex(real=0,imaginary=sqrt(15))   # The complex command in R, not it's
sqrt(15) not just 15!

x_1 = (-b + q)/(2.0*a)   # add parentheses for precedence
x_2 = (-b - q)/(2.0*a)   
cat(x_1)
cat("\n")
cat(x_2)
cat("\n")
cat("a*x_1^2 + b * x_1 + c=", a*x_1^2 + b * x_1 + c)
cat("\n")
cat("a*x_2^2 + b * x_2 + c=", a*x_2^2 + b * x_2 + c)
