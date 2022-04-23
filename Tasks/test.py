import numpy as np
import math
net = np.array([1,0,0])
net=0.3
c=0
result = 1 / (1 + np.exp(-1 * net))
result = math.tanh(net)
result2=(np.exp(net) - np.exp(-1 * net)) / (np.exp( net) + np.exp(-1 * net))
print(result)
print(result2)
