# Создайте игру, в которой пользователь 
# угадывает случайное число от 1 до 10, пока не угадает.

import random  # Импортируем модуль для генерации случайных чисел

# Генерируем случайное число от 1 до 10
target_number = random.randint(1, 10)

print("Угадайте число от 1 до 10!")

while True:
    # Вводим число от пользователя
    user_guess = int(input("Введите ваше число: "))
    
    # Проверяем, угадал ли пользователь
    if user_guess < target_number:
        print("Слишком мало! Попробуйте снова.")
    elif user_guess > target_number:
        print("Слишком много! Попробуйте снова.")
    else:
        print("Поздравляю! Вы угадали число!")
        break  # Выход из цикла, если число угадано
