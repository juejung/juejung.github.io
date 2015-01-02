# 1 Plot simple vectors

In this chapter we explore some of the graphical functionality of **R**. We first define 3 simple vectors and try to plot them.

```python
import time                     # Imports system time module to time your script
from pylab import *             # Imports numpy, scipy, and matplotlib etc.
from scipy import stats as st
tic = time.clock()              # Start timer
# -----------------------------------------------------------------------------

close('all')  # close all open figures
# Define 2 vectors with 5 values each
xv     = array([1,2,3,4,5])
cars   = array([1, 3, 6, 4, 9])
trucks = array([2, 5, 4, 5, 12])
suvs   = array([4, 4, 6, 6, 16])
```
```

```


## 1.1 First plot

We then simply plot the first vector using the ```plot()``` command.

```python
fig1 = figure()
plot(cars)
show()
```
```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
NameError: name 'figure' is not defined
```

We can change the way the graph looks adding plot symbols and color. In addition we add a title.

```python
# Graph cars using blue points overlayed by a line 
fig2 = figure()
plot(cars, '-o', label='cars')
# Create a title with a red, bold/italic font
title('Autos')
show()
```
```
Traceback (most recent call last):
  File "<string>", line 2, in <module>
NameError: name 'figure' is not defined
```



## 1.2 Graph autos 2 types

```python
fig3 = figure()
plot(xv,cars, '-o',xv,trucks,'-')
# Create a title with a red, bold/italic font
title('Autos')
show()
```
```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
NameError: name 'figure' is not defined
```


## 1.3 Graph autos using y axis that ranges from min to max
```python
fig4 = figure()
plot(xv, cars, '-o', xv, trucks,'-')
title('Autos')   
xlabel('Days')
ylabel('Total')
xlim(0.5,5.5)
ylim(min(flatten(zip(cars,trucks))), max(flatten(zip(cars,trucks))))   
# Create a legend 
legend(('cars', 'trucks'),'lower right', shadow=True)
show()
```
```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
NameError: name 'figure' is not defined
```


## 1.4 Graph autos: 3 types

Finally, we graph all three into one figure.
This time we save the graph as ```fig1.pdf``` into subfolder Graphs.

```python
fig5 = figure()
plot(xv, cars, '-bo', xv, trucks,'r-', xv, suvs, 'r:')
title('Autos')   
xlabel('Days')
ylabel('Total')
xlim(0.5,5.5)
#ylim(min(cars,trucks),max(cars,trucks))   
# Create a legend 
legend(('cars', 'trucks','suvs'),'lower right', shadow=True)  
# Save graphs in subfolder Graphs under name: fig1.pdf
savefig('./Graphs/fig1.pdf')
show()
```
```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
NameError: name 'figure' is not defined
```


# 2 Plotting functions

We next want to plot mathematical functions. We again first define the input vector ```x``` and then specify the "output" vector ```y``` as: $$latex y = f(x)$$ where for our first example $latex f(x) = x^2$, $latex f(x)=3*y/2 - 5$, and finally $latex f(x)=5*y/2 - \sqrt{y}$.

```python
x = arange(1, 10, 0.1)
y = x**2
y1 = 3*y/2 - 5
y2 = 5*y/2 - sqrt(y)
```
```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
NameError: name 'arange' is not defined
```


We have now two columns of values: x and y that we can plot against each other into a coordinate system.

```python
fig6=figure()
plot(x,y,x,y1,x,y2)
show()
```
```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
NameError: name 'figure' is not defined
```


# 3 3DGraphing 

Finally, we can also plot 3-D graphs in **Python**. In order to do this we need the library ```Axes3D``` from ```mpl_toolkits.mplot3d```. This introduces a new command called ```Axes3D```. It is used as follows.

```python
from mpl_toolkits.mplot3d import Axes3D

xv = arange(1, 10, 1)
yv = arange(1, 10, 1)
n = len(x)
zv = 3 * yv**2 /2 + xv - sqrt(xv*yv) /5

## 3.1 Simply use x,y,z as coordinates for points in 3D space
fig7=figure()
ax = Axes3D(fig7)
ax.plot(xv, yv, zv, zdir='z',label='parametric curve')
show()
```
```
Traceback (most recent call last):
  File "<string>", line 3, in <module>
NameError: name 'arange' is not defined
```


--------------------------------------------------------------------------------
## 3.2 Use 'surface' command if you want to plot the graph over its entire domain

```python
fig7b = figure()
ax = gca(projection='3d')
X = arange(1, 10, 1)
Y = arange(1, 10, 1)
X, Y = meshgrid(X, Y)
Z = 3.0 * Y**2.0 /2.0 + X - sqrt(X*Y) /5.0
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.jet,
        linewidth=0, antialiased=False)
show()
```
```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
NameError: name 'figure' is not defined
```


--------------------------------------------------------------------------------
# 4 Subplots

If we have more than one figure it might be good to put them all into one graph. In the following example we plot 6 figures into one picture. We plot into 3 rows and 2 columns. You can obviously rearrange all this.

```python
# creates  a 3 x 2 grid of subplots
fig8 = figure()
subplot(321)   
plot([1,2,3])  
title('figure 1')

subplot(322, axisbg='y') # creates 2nd subplot with yellow background
plot(rand(12), rand(12), 'bo')
title('figure 2')

subplot(323)   
plot([1,1,1])  
title('figure 3')

subplot(324, axisbg='g') 
plot(rand(12), rand(12), 'rx')
title('figure 4')

subplot(325)   
plot([1,2,1],':')  
title('figure 5')

subplot(326, axisbg='w') 
plot(rand(12), rand(12), 'kx')
title('figure 6')
show()
```
```
Traceback (most recent call last):
  File "<string>", line 2, in <module>
NameError: name 'figure' is not defined
```

-------------------------------------------------------------------------------
```python
toc = time.clock()              # Stop timer
print "Time passed: " + str(toc - tic)
```
```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
NameError: name 'time' is not defined
```

