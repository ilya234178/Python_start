# Задача 2: Напишите программу, которая выводит результат сложения 
# двух чисел, введенных пользователем.
# Цель: Использование арифметических операторов
try:
    num1 = int(input("Number 1: "))
    num2 = int(input("Number 2: "))
    total = num1 + num2
    print(total)
except:
    print("введи число.")
