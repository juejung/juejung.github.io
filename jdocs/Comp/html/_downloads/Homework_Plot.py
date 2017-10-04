# -*- coding: utf-8 -*-
# Homework_Plot

import numpy as np
import matplotlib.pyplot as plt

#------------------------------------------------------------------------------
# Problem 1
#------------------------------------------------------------------------------
A = 10
alpha = .33
L = 20
Kv = np.linspace(0, 10, 100)
Yv = A*(Kv**alpha)*(L**(1-alpha))

fig, ax = plt.subplots()
ax.plot(Kv, Yv, 'b-', linewidth=2, label='points')
ax.set_title('Production function')
ax.set_xlabel('Capital: K')
ax.set_ylabel('Output: Y')
plt.show()
print("-------------------------------------------------------------------")

#------------------------------------------------------------------------------
# Problem 2
#------------------------------------------------------------------------------

Av = np.arange(20, 25, 1)
# Insert original value of A=10 at position 0
Av = np.insert(Av, 0, 10)

fig, ax = plt.subplots()
for A in Av:
    Yv = A*(Kv**alpha)*(L**(1-alpha))
    ax.plot(Kv, Yv)

ax.set_title('Production function with varying TFP')
ax.set_xlabel('Capital: K')
ax.set_ylabel('Output: Y')
plt.show()
print("-------------------------------------------------------------------")

#------------------------------------------------------------------------------
# Problem 3
#------------------------------------------------------------------------------
queue = ["Steve", "Russell", "Alison", "Liam"]

# 1. Barry arrives
queue.append("Barry")
print(queue)

# 2. Steve is served
queue.remove("Steve")
print(queue)

# 3. Pam talks her way to the front because she only buys one item
queue.insert(0, "Pam")
print(queue)

# 4. Barry gets impatient and leaves
queue.remove("Barry")
print(queue)

# 5. Alison gets impatient and leaves
queue.remove("Alison")
print(queue)
print("-------------------------------------------------------------------")

#------------------------------------------------------------------------------
# Problem 4
#------------------------------------------------------------------------------
v0 = 10
g = 9.81
tv = np.linspace(0, 2*v0/g, 100)
yv = v0 * tv -.5 * g * (tv**2)

fig, ax = plt.subplots()
ax.plot(tv, yv, 'b-')
ax.set_ylabel('Height m')
ax.set_xlabel('Time t')
plt.show()
print("-------------------------------------------------------------------")

#------------------------------------------------------------------------------
# Problem 5
#------------------------------------------------------------------------------
num_cols = 1
num_rows = 3
title_size = 26

fig = plt.figure(figsize=(5, 10))
fig.suptitle("Figure with multiple subplots", fontsize=title_size, fontweight='bold')

# [1]
xv = np.linspace(0.0001, 10, 100)
fv = np.log(xv)

ax = plt.subplot2grid((num_rows, num_cols), (0,0))
ax.plot(xv, fv)
ax.set_title("f(x) = Log(x)")
# [2]
xv = np.linspace(0.1, 10, 100)
gv = 1./xv
ax = plt.subplot2grid((num_rows, num_cols), (1,0))
ax.plot(xv, gv, 'b-o')
ax.set_title("f'(x) = 1/x")
# [3]
xv = np.linspace(-4, 4, 100)
hv = np.abs(xv)
ax = plt.subplot2grid((num_rows, num_cols), (2,0))
ax.plot(xv, hv)
ax.set_title("h(x) = |x|")
plt.show()
print("-------------------------------------------------------------------")

#------------------------------------------------------------------------------
# Problem 6
#------------------------------------------------------------------------------
xv = np.linspace(-3, 5, 200)
yv = np.zeros(len(xv))

for i,x in enumerate(xv):
    if x < 0:
        yv[i] = np.abs(x)
    elif (x >= 0) & (x < 1):
        yv[i] = -1
    elif (x >= 1) & (x < 2):
        yv[i] = 1
    else:
        yv[i] =np.log(x)

fig, ax = plt.subplots()
ax.plot(xv, yv, 'b.')
# For x/y axes in red
ax.axvline(x=0, color = 'r')
ax.axhline(y=0, color = 'r')
# For the dotted vertical lines at the jump points
ax.plot((0, 0), (-1,0), 'k:')
ax.plot((1, 1), (-1,1), 'k:')
ax.plot((2, 2), (-1,1), 'k:')
ax.set_title('Composite discontinuous function')
ax.set_xlabel('x')
plt.show()
