import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("example_data.csv", delimiter=",", skiprows=1)
plt.plot(data[:, 0], data[:, 1])
plt.show()
