#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#Пример:

#пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def find_factorial(num):
    factorial=1
    if(num%1==0 and num >= 0):
        for i in range(1, num+1):
            factorial = i*factorial 
            print(factorial,end=', ')       
        return (f'{num}! = {factorial}')
    else:
        return ('Невозможно вычислить факториал нецелого и/или отрицательного числа!')
num = eval(input("Факториал какого числа считаем? "))
factorial = find_factorial(num)
