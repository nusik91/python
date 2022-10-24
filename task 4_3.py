# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности
N = int(input('Введите N: '))
from random import randint 
L = [randint(1,9) for x in range(N)]
print(L, end=" ")

for i in L:
   if L.count(i) == 1:
       print(i, end=" ")