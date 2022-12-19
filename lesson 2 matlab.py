import matplotlib.pyplot as plt
import numpy as np
# a= [0,-100 ,25,67,-323]
# b = [ 5,0,3,7,3,9]
# plt.hist(a)
# plt.hist(b)

nd = np.array([[1,2,3],[4,5,6]])
nd1 = np.array([[7,8,9]])
print(np.sum(nd))
print(np.sum(nd,axis = 0))
print(nd)
print(np.append(nd , nd1 , 0))
print(np.transpose(nd))