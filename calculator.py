def add(a, b):
    """Сложение двух чисел"""
    return a + b

def subtract(a, b):
    """Вычитание второго числа из первого"""
    return a - b

def multiply(a, b):
    """Умножение двух чисел"""
    return a * b

def divide(a, b):
    """Деление первого числа на второе"""
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b

def power(a, b):
    """Возведение первого числа в степень второго"""
    return a ** b

def main():
    """Основная функция для запуска калькулятора"""
    print("Простой калькулятор"
    print("Доступные операции:")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    print("5. Возведение в степень (^)")
    print("0. Выход")
    print("Бананчики")

    while True:
        choice = input("\nВыберите операцию (0-5): ")

        if choice == '0':
            print("До свидания!")
            break

        if choice not in ['1', '2', '3', '4', '5']:
            print("Неверный выбор. Попробуйте снова.")
            continue

        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))

            if choice == '1':
                result = add(num1, num2)
                print(f"Результат: {num1} + {num2} = {result}")
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"Результат: {num1} - {num2} = {result}")
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"Результат: {num1} * {num2} = {result}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"Результат: {num1} / {num2} = {result}")
            elif choice == '5':
                result = power(num1, num2)
                print(f"Результат: {num1} ^ {num2} = {result}")

        except ValueError as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
