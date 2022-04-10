import numpy as np
import math
a = np.array([1,23,8])
result = math.tanh(0.3)
result2 = (1 - np.exp(-2* 0.3))/ (1 + np.exp(-2 * 0.3))
print(result)
print(result2)