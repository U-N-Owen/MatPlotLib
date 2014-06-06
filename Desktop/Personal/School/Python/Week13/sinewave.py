import numpy as np
import matplotlib.pyplot as mpl

x=np.linspace(0, 10, 100)
ysin=np.sin(x)
ycos=np.cos(x)

mpl.xlim([0, 2* np.pi])
mpl.ylim([1.1, -1.1])

mpl.plot(x,ysin,'g^', label = "Sin")
mpl.plot(x,ycos,'r+', label = "Cos")

mpl.text(2.5, -.5, "$ \int_a^b \sin\phi dx $")

mpl.xlabel("angle $ \phi $")
mpl.ylabel("$ \sin\phi $")
mpl.legend(loc='center center')

mpl.title("a sine wave")

mpl.show()
