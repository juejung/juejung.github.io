-------------------------------------------------------------------------------
# 1 Plot simple vectors

In this chapter we explore some of the graphical functionality of **R**. We first define 3 simple vectors and try to plot them.



```r
rm(list = ls())  # Remove almost everything in the memory
setwd("C:/Dropbox/Towson/Teaching/3_ComputationalEconomics/Lectures/Lecture2/R")
```

```
## Error: cannot change working directory
```

```r
cars = c(1, 3, 6, 4, 9)
trucks = c(2, 5, 4, 5, 12)
suvs = c(4, 4, 6, 6, 16)
```




-------------------------------------------------------------------------------
## 1.1 First plot

We then simply plot the first vector using the ```plot()``` command.



```r
plot(cars)
```

![plot of chunk R2](figure/R2.png) 

We can change the way the graph looks adding plot symbols and color. In addition we add a title.



```r
# Graph cars using blue points overlayed by a line
plot(cars, type = "o", col = "blue")
# Create a title with a red, bold/italic font
title(main = "Autos", col.main = "red", font.main = 4)
```

![plot of chunk R3](figure/R3.png) 


-------------------------------------------------------------------------------
## 1.2 Adjusting the plot
We can also adjust the plot range in both dimensions as follows.



```r
plot(cars, type = "o", col = "blue", ylim = c(0, 12))  # Create a title with a red, bold/italic font
title(main = "Autos", col.main = "red", font.main = 4)
```

![plot of chunk R4](figure/R4.png) 


-------------------------------------------------------------------------------
## 1.3 Graph autos: 2 types
Finally, we can the second vector to the plot using the command ```line```.
We graph autos using y axis that ranges from 0 to max value in cars or trucks vector.  
Turn off axes and annotations (axis labels) so we can specify them ourself.



```r
# Calculate range from 0 to max value of cars and trucks
g_range <- range(0, cars, trucks)

plot(cars, type = "o", col = "blue", ylim = g_range, axes = FALSE, 
    ann = FALSE)
# Make x axis using Mon-Fri labels
axis(1, at = 1:5, lab = c("Mon", "Tue", "Wed", "Thu", "Fri"))

# Make y axis with horizontal labels that display ticks at every 4 marks.
# 4*0:g_range[2] is equivalent to c(0,4,8,12).
axis(2, las = 1, at = 4 * 0:g_range[2])

# Create box around plot
box()

# Graph trucks with red dashed line and square points
lines(trucks, type = "o", pch = 22, lty = 2, col = "red")

# Create a title with a red, bold/italic font
title(main = "Autos", col.main = "red", font.main = 4)

# Label the x and y axes with dark green text
title(xlab = "Days", col.lab = rgb(0, 0.5, 0))
title(ylab = "Total", col.lab = rgb(0, 0.5, 0))

# Create a legend at (1, g_range[2]) that is slightly smaller (cex) and
# uses the same line colors and points used by the actual plots
legend(1, g_range[2], c("cars", "trucks"), cex = 0.8, col = c("blue", 
    "red"), pch = 21:22, lty = 1:2)
```

![plot of chunk R5](figure/R5.png) 


-------------------------------------------------------------------------------
## 1.4 Graph autos: 3 types

Finally, we graph all three into one figure.
This time we save the graph as ```fig1.pdf``` into subfolder Graphs.



```r
max_y = max(cars, trucks, suvs)

# Define colors to be used for cars, trucks, suvs
plot_colors = c("blue", "red", "forestgreen")

# Start PDF device driver to save output to fig1.pdf
# pdf(file='./Graphs/fig1.pdf')

# Graph autos using y axis that ranges from 0 to max_y.  Turn off axes and
# annotations (axis labels) so we can specify them ourself
plot(cars, type = "o", col = plot_colors[1], ylim = c(0, max_y), 
    axes = FALSE, ann = FALSE)

# Make x axis using Mon-Fri labels
axis(1, at = 1:5, lab = c("Mon", "Tue", "Wed", "Thu", "Fri"))

# Make y axis with horizontal labels that display ticks at every 4 marks.
# 4*0:max_y is equivalent to c(0,4,8,12).
axis(2, las = 1, at = 4 * 0:max_y)

# Create box around plot
box()

# Graph trucks with red dashed line and square points
lines(trucks, type = "o", pch = 22, lty = 2, col = plot_colors[2])

# Graph suvs with green dotted line and diamond points
lines(suvs, type = "o", pch = 23, lty = 3, col = plot_colors[3])

# Create a title with a red, bold/italic font
title(main = "Autos", col.main = "red", font.main = 4)

# Label the x and y axes with dark green text
title(xlab = "Days", col.lab = rgb(0, 0.5, 0))
title(ylab = "Total", col.lab = rgb(0, 0.5, 0))

# Create a legend at (1, max_y) that is slightly smaller (cex) and uses
# the same line colors and points used by the actual plots
legend(1, max_y, c("cars", "trucks", "suvs"), cex = 0.8, col = plot_colors, 
    pch = 21:23, lty = 1:3)
```

![plot of chunk R6](figure/R61.png) 

```r
# Turn off device driver (to flush output to png)
dev.off()
```

![plot of chunk R6](figure/R62.png) 

```
## RStudioGD 
##         2 
```





-------------------------------------------------------------------------------
# 2 Plotting functions


We next want to plot mathematical functions. We again first define the input vector ```x``` and then specify the "output" vector ```y``` as: $$y = f(x)$$ where for our first example $latex f(x) = x^2$ , $latex f(x)=3*y/2 - 5$, and finally $latex f(x)=5*y/2 - \sqrt{y}$.



```r
x = seq(1, 10, by = 0.1)
y = x^2
y1 = 3 * y/2 - 5
y2 = 5 * y/2 - sqrt(y)
```




We have now two columns of values: x and y that we can plot against each other into a coordinate system.



```r
plot(x, y)
# plot(x,y,type='l') if you want to add plots to the one we just made, use
# the 'line' command.
lines(x, y1)
lines(x, y2)
```

![plot of chunk R8](figure/R8.png) 



--------------------------------------------------------------------------------
# 3 3-D Graphs 

--------------------------------------------------------------------------------

## 3.1 Simply use x,y,z as coordinates for points in 3D space
Finally, we can also plot 3-D graphs in **R**. In order to do this we need the library ```rgl```.
This introduces a new command called ```plot3d``` with a slightly more involved syntax.



```r
library("rgl")

x = seq(1, 10, by = 1)
y = seq(1, 10, by = 1)
n = length(x)
z = 3 * y^2/2 + x - sqrt(x * y)/5

# Simply use x,y,z as coordinates for points in 3D space
plot3d(x, y, z, type = "p", col = "red", xlab = "X", ylab = "Y", 
    zlab = "Z", size = 5, lwd = 15, box = F)
```



--------------------------------------------------------------------------------
## 3.2 Use 'wireframe' command if you want to plot the graph over its entire domain



```r
library("lattice")
## Make data for wireframe command
i = 1
for (x0 in seq(1, 10, 1)) {
    for (y0 in seq(1, 10, 1)) {
        x[i] = x0
        y[i] = y0
        z[i] = 3 * y[i]^2/2 + x[i] - sqrt(x[i] * y[i])/5
        i = i + 1  # data counter
    }
}
wireData = data.frame(x = x, y = y, z = z)

wireframe(z ~ x * y, main = "3 D Wireframe Plot", xlab = "x", ylab = "y", 
    data = wireData)
```

![plot of chunk R10](figure/R10.png) 


--------------------------------------------------------------------------------
# 4 Subplots


If we have more than one figure it might be good to put them all into one graph. In the following example we plot 6 figures into one picture. We plot into 3 rows and 2 columns. You can obviously rearrange all this.



```r
# Open a new default device.
get(getOption("device"))()
```

```
## Error: invalid first argument
```

```r

## Set up plotting in 3rows and 2 columns, plotting along rows first.
par(mfrow = c(3, 2))

plot(c(1, 2, 3), type = "o")
title("figure 1")


plot(runif(12), runif(12), type = "l", col = "red")
title("figure 2")


plot(c(1, 1, 1))  # implicitly creates subplot(111)
title("figure 3", pch = 22, lty = 2, col = "red")


plot(runif(12), runif(12), type = "o", pch = 23, lty = 3, col = "blue")
title("figure 4")


plot(c(1, 2, 1), type = "l")  # implicitly creates subplot(111)
title("figure 5")

plot(runif(12), runif(12), type = "l", lty = 2, lwd = 2)
title("figure 6")
```

![plot of chunk R11](figure/R11.png) 


------------------------------------------------------------------------------- 
# Exercises

1. Define vector $latex x=[0,...,10]$ and function y as $latex y(x) = \frac{\sqrt{x}}{x}$.
2. Plot values of $latex x$ against $latex y(x)$.
3. Define a new function $latex z(y) = y +5.5$ and plot it as subplot,
   underneath the first plot. Note that $latex z$ is ultimately a function of $latex x$, as in $latex z(y(x))$.
4. Add a third subplot that has both, $latex y$ and $latex z$ in the same
   graph.