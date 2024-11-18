# Напишите программу, которая принимает два числа от пользователя и
# выводит их сумму, разность, произведение и частное.

def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Деление на ноль невозможно"
    return a / b

while True:
    try:
        num1 = int(input("\nВведите первое число: "))
        num2 = int(input("Введите второе число: "))
        print("\nВыберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Выход")

        choice = input("\nВведите номер операции (1-5): ")

        if choice == '1':
            print(f"Сумма: {sum(num1, num2)}")
        elif choice == '2':
            print(f"Разность: {sub(num1, num2)}")
        elif choice == '3':
            print(f"Произведение: {mult(num1, num2)}")
        elif choice == '4':
            print(f"Частное: {div(num1, num2)}")
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Ошибка: Неверный выбор операции.")
    except ValueError:
        print("Ошибка: Введите корректные числовые значения.")

