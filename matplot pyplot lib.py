
# importing libraries
import matplotlib.pyplot as plt
import numpy as np
import math
  
X = np.arange(0, math.pi*2, 0.05)

Y1 = np.sin(X)
Y2 = np.cos(X)

  
figure, axis = plt.subplots(2, 2)
  
axis[0, 0].plot(X, Y1)
axis[0, 0].set_title("Sine Function")
  
axis[0, 1].plot(X, Y2)
axis[0, 1].set_title("Cosine Function")
  
plt.show()