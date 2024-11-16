#Задача 7: Напишите программу, которая вычисляет сумму чисел от 1 до 100.
count = 0
for i in range(1,100 + 1):
    
    count +=i
    print(f"{count} + {i} = {count}")