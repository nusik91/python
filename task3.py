#Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

num = int(input('Введите число'))
print(num)
if (num%10 == 0 or num%15 == 0) and num%30 != 0:
     print("Число удовлетворяет условию")
else:
     print("Число НЕ удовлетворяет условию")   