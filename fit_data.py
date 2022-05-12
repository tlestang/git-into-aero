import numpy as np
import matplotlib.pyplot as plt

filename = "example_data.csv"
data = np.loadtxt(filename, delimiter=",", skiprows=1)
plt.plot(data[:, 0], data[:, 1])
plt.show()
