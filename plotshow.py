import matplotlib
matplotlib.use('TkAgg')  # Ubuntu GUI backend
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)
y = 2*x + np.random.normal(0,2,50)

plt.scatter(x, y)
plt.plot(x, 2*x, color='red')
plt.title("Random Dataset")
plt.show()