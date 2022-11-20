from random import shuffle
import numpy as np
n = int(input('Количество степеней: '))
np.array(n)
arr = [3 ** (i + 1) for i in range(n)]
shuffle(arr)
print(arr)
