import numpy as np
a = np.array([1,23,8])
k= np.insert(a, 0, 6, axis=0)
print(k.shape)