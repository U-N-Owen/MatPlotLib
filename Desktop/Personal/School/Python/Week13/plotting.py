import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,100)

y0 = x **0
y1 = x
y2 = x*x
y3 = x*x*x

r = np.linspace(0,10,100)

th0 = r **0
th1 = r
th2 = r*r
th3 = r*r*r

plt.subplot (1,2,1)
plt.plot (x, y0, 'k', label = "$x^0$")
plt.plot (x, y1, 'b', label = "$x$")
plt.plot (x, y2, 'g', label = "$x^2$")
plt.plot (x, y3, 'r', label = "$x^3$")
plt.title ("Polynomial Functions")
plt.xlabel ("x")
plt.ylabel ("y")
plt.legend(loc = 'upper left')

plt.subplot (1, 2, 2, polar = True)
plt.plot (r, th0, 'k', label = "$r^0$")
plt.plot (r, th1, 'b', label = "$r$")
plt.plot (r, th2, 'g', label = "$r^2$")
plt.plot (r, th3, 'r', label = "$r^3$")
plt.legend(loc = 'lower right')

plt.show()