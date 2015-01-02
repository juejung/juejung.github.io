# Homework 3

rm(list = ls())  # Remove almost everything in the memory

# -----------------------------------------------------------------------------
# Exercise 1
# -----------------------------------------------------------------------------
n = 26              # another arbitrary n for the test
i = 1
oddNum = vector()
while (i<=n){
    # tests whether or not the number is odd using modulo division %%
    if (i%%2==1){   
    oddNum = c(oddNum,i)    
    # cat(i,"\n")
  }
  i=i+1             # increments the counter i, otherwise the loop runs forever!
}
cat(oddNum, "\n")

# -----------------------------------------------------------------------------
# Exercise 2
# -----------------------------------------------------------------------------
a = c(1, 3, 5, 7)
b = c(13, 17)
c = c(a,b)    # appends vectors a and b into vector c
cat(c,"\n")
b[1] = -1     # b[0] in Python is b[1] in R, remember the indexing difference!
d = vector()
for (e in a) {
    d = union(d,c(e+1)) # This simply implements: a+1
}
cat(d,"\n")

d = c(d,b[1]+1)           # appends b[1] while adding 1 to that value
d = c(d,b[length(b)]+1)   # grabs last element of b and adds 1 and tags it onto d
cat(tail(d,2),"\n")       # prints last two elements of vector d

# -----------------------------------------------------------------------------
# Exercise 3
# -----------------------------------------------------------------------------
s = 0.0; k = 1.0; M = 100  
while (k <= M) {   # changed to include 100 
  s = s + (1./k)   # changed from += to s= s+
  # cat(s,"\n")    # prints intermediate values for method two
  k=k+1    #increment k to prevent infinite loop
}
cat(s,"\n")

# -----------------------------------------------------------------------------
# Exercise 4
# -----------------------------------------------------------------------------
s = 0.0; k = 1.0; M = 100  
for (k in (1:M)) {   
  s = s + (1./k)   
  # cat(s,"\n")    # prints intermediate values for method two
}
cat(s,"\n")

# -----------------------------------------------------------------------------
# Exercise 5
# -----------------------------------------------------------------------------
# Define the nested list using the list() command
q=list(list("a","b","c"),list("d","e","f"),list("g","h"))

# When using the cat() command with list elements, you need to translate the list
# elements into characters before printing, using the as.character() command

cat(as.character(q[[1]][1]),"\n")                 # the letter 'a' is indexed as the first element [1] in the first list: q[[1]] 
cat(as.character(q[[2]]),"\n")                    # extracts the second sublist
cat(as.character(q[[3]][length(q[[3]])]),"\n")    # last element of third sublist
cat(as.character(q[[2]][1]),"\n")                 # extracts first element of second sublist
cat(as.character(q[[length(q)]][1]),"\n")         # extracts first element of last sublist

# -----------------------------------------------------------------------------
# Exercise 6
# -----------------------------------------------------------------------------

# Lotka-Volterra predator-prey equations
br = 0.04   # growth rate of rabbits
dr = 0.0005 # death rate of rabbits due to predation
df = 0.2    # death rate of foxes
bf = 0.1    # efficiency of turning predated rabbits into foxes
x  = 4000   # Rabbit population
y  = 100    # Fox population
# Track rabbits and foxes over time in vectors
xv = c(x)   
yv = c(y)  
while (x > 3500) {
    # Run until rabbit population falls below 3900
    # cat("x =", x, " y =", y, "\n")
    x.new = (1+br)*x - dr*x*y
    y.new = (1-df)*y + bf*dr*x*y
    xv=c(xv,x.new)  # append number of rabbits
    yv=c(yv,y.new)  # append number of foxes
    x = x.new       # new number of rabbits for the next round
    y = y.new       # new number of foxes for the next round
}
# Plotting the populations over time
# ----------------------------------

par(mfrow = c(3, 1))

plot(xv,type="o",col="blue",pch = 21,xlab="Time",ylab="Population")
title("Rabbits over time")

plot(yv,type="o",col="red",pch = 23,xlab="Time",ylab="Population")
title(main="Foxes over time")

g_range = range(0, xv, yv)
plot(xv,type="o",col="blue",pch = 21,ylim=g_range,xlab="Time",ylab="Population")
lines(yv,type="o",col="red",pch = 23,xlab="Time",ylab="Population")
title(main="Predator vs. Prey")
legend(1, g_range[2], c("Rabbits", "Foxes"), cex = 0.6, col = c("blue", "red"), pch = c(21,23), lty = 1:2) 







