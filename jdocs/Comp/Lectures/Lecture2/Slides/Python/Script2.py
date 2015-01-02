#!/usr/bin/env python

# Here we want to call our two Python functions that are saved in myfunctions.py
# We can import these functions as follows:

import time                     # Imports system time module to time your script
from pylab import *             # Imports numpy, scipy, and matplotlib etc.
from scipy import stats as st
tic = time.clock()              # Start timer
# -----------------------------------------------------------------------------

close('all')  # close all open figures
# --------------------------------------------
# 1 Graphing vectors
# --------------------------------------------

# Define 2 vectors with 5 values each
xv     = array([1,2,3,4,5])
cars   = array([1, 3, 6, 4, 9])
trucks = array([2, 5, 4, 5, 12])
suvs   = array([4, 4, 6, 6, 16])

# --------------------------------------------
## 1.1 Graph the cars vector with all defaults
# --------------------------------------------
fig1 = figure()
plot(cars)
show()

# Graph cars using blue points overlayed by a line 
fig2 = figure()
plot(cars, '-o', label='cars')
# Create a title with a red, bold/italic font
title('Autos')
show()

# --------------------------------------------
## 1.2 Graph cars using a y axis that ranges from 0 to 12
# --------------------------------------------
fig3 = figure()
plot(xv,cars, '-o',xv,trucks,'-')
# Create a title with a red, bold/italic font
title('Autos')
show()

# --------------------------------------------
## 1.3 Graph autos using y axis that ranges from min to max  
# --------------------------------------------
# value in cars or trucks vector.  Turn off axes and 
# annotations (axis labels) so we can specify them ourself

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

# --------------------------------------------
## 1.4 Graph autos: 3 types
# --------------------------------------------

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


# --------------------------------------------
# 2 Graphing functions
# --------------------------------------------

x = arange(1, 10, 0.1)
y = x**2
y1 = 3*y/2 - 5
y2 = 5*y/2 - sqrt(y)

fig6=figure()
plot(x,y,x,y1,x,y2)
show()
#
## --------------------------------------------
## 3 3DGraphing 
## --------------------------------------------

from mpl_toolkits.mplot3d import Axes3D

xv = arange(1, 10, 1)
yv = arange(1, 10, 1)
n = len(x)
zv = 3.0 * yv**2.0 /2.0 + xv - sqrt(xv*yv) /5.0

## 3.1 Simply use x,y,z as coordinates for points in 3D space
fig7=figure()
ax = Axes3D(fig7)
ax.plot(xv, yv, zv, zdir='z',label='parametric curve')
show()

## 3.2 Surface 3D plot over entire domain of the function
fig7b = figure()
ax = gca(projection='3d')
X = arange(1, 10, 1)
Y = arange(1, 10, 1)
X, Y = meshgrid(X, Y)
Z = 3.0 * Y**2.0 /2.0 + X - sqrt(X*Y) /5.0
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.jet,
        linewidth=0, antialiased=False)
show()



## -------------------------------------------
## 4 Subplots
## -------------------------------------------
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


# -----------------------------------------------------------------------------
toc = time.clock()              # Stop timer
print "Time passed: " + str(toc - tic)

