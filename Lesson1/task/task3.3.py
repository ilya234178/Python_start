#Напишите функцию, которая принимает строку и возвращает её длину.

def analyze_text(text):
    text_length = len(text)  # Общая длина строки
    letters = sum(1 for char in text if char.isalpha())  # Количество букв
    digits = sum(1 for char in text if char.isdigit())  # Количество цифр
    spaces = sum(1 for char in text if char.isspace())  # Количество пробелов
    special_chars = text_length - (letters + digits + spaces)  # Остальные символы
    
    return {
        "length": text_length,
        "letters": letters,
        "digits": digits,
        "spaces": spaces,
        "special_chars": special_chars,
    }

# Ввод текста от пользователя
str_txt = input("Введите текст: ").strip()

if len(str_txt) == 0:
    print("Вы ввели пустую строку.")
else:
    stats = analyze_text(str_txt)
    print(f"\nАнализ введенного текста:")
    print(f"- Общая длина: {stats['length']}")
    print(f"- Количество букв: {stats['letters']}")
    print(f"- Количество цифр: {stats['digits']}")
    print(f"- Количество пробелов: {stats['spaces']}")
    print(f"- Количество специальных символов: {stats['special_chars']}")
