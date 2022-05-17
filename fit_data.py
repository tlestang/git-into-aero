import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from model import model

filename = "example_data.csv"
data = np.loadtxt(filename, delimiter=",", skiprows=1)
plt.plot(data[:, 0], data[:, 1])

popt, pcov = curve_fit(model, data[:, 0], data[:, 1], p0=(1, 0.2))

plt.show()
