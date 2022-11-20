import numpy as np
a = np.array(input('Введіть числа через пробіл:').split(' '), dtype=int)
b = np.array(input('Введіть числа через пробіл:').split(' '), dtype=int)
c = np.array([a, b])
p = a+b
print(c)
for i in p:
    print(i)
