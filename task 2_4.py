#Реализуйте алгоритм перемешивания списка

import random

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

b = a[:]
random.shuffle(b)
print(b)