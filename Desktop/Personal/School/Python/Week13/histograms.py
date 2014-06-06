import numpy as np
import matplotlib.pyplot as plt

data = np.random.rand(10)

plt.hist(data)

plt.xlabel("random")
plt.ylabel("Random")
plt.title("random")

plt.show()