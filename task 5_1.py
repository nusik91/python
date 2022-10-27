# Напишите программу, удаляющую из текста все слова, содержащие ""абв""

text = input("Введите текст через пробел:\n")
print(f"Исходный текст: {text}")
search = input("Поиск: ")
print(f"Исходный текст: {search}")
lst = [i for i in text.split() if search not in i]
print(f'Результат: {" ".join(lst)}')