from random import shuffle
n = int(input('Количество степеней: '))
arr = [3 ** (i + 1) for i in range(n)]
shuffle(arr)
print(arr)
