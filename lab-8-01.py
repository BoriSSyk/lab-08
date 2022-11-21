import numpy as np
a = np.array([i**3 for i in range(-9, 11)]).reshape((5, 4))
print(a, '\n')
np.random.shuffle(a)
print(a)
