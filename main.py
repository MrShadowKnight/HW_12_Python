# TACK №1

try:
    num = int(input("Введіть число: "))
    if num < 0:
        raise ValueError("Факторіал від'ємного числа не визначений.")

    factorial = 1
    for i in range(1, num + 1):
        factorial *= i

    print(f"Факторіал числа {num} дорівнює {factorial}")
except ValueError as e:
    print(f"Помилка: {e}")


# TACK №2.1

def factorial(n):
    result = n * factorial(n - 1)
    return result

try:
    num = int(input("Введіть число: "))
    if num < 0:
        raise ValueError("Факторіал не можна обчислити для від'ємного числа.")
    elif num == 0 or num == 1:
        print("1")
    else:
        print(f"Факторіал числа {num} дорівнює {factorial(num)}.")
except ValueError as ve:
    print(f"Помилка: {ve}")
except Exception as e:
    print(f"Сталася невідома помилка: {e}")


# TACK №2.2

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

try:
    num = int(input("Введіть число: "))
    if num < 0:
        raise ValueError("Факторіал не можна обчислити для від'ємного числа.")
    result = factorial(num)
    print(f"Факторіал числа {num} дорівнює {result}.")
except ValueError as ve:
    print(f"Помилка: {ve}")
except Exception as e:
    print(f"Сталася невідома помилка: {e}")

# TACK №3

try:
    # Запитуємо користувача ввести числа для створення списку
    num_list = [int(x) for x in input("Введіть числа через пробіл: ").split()]

    while True:
        print("\nМеню:")
        print("1. Відображення списку")
        print("2. Максимальне значення")
        print("3. Мінімальне значення")
        print("4. Значення елемента за індексом")
        print("5. Видалення елемента за індексом")
        print("6. Вийти")

        choice = int(input("Виберіть операцію (1-6): "))

        if choice == 1:
            print("Список:", num_list)
        elif choice == 2:
            print("Максимальне значення:", max(num_list))
        elif choice == 3:
            print("Мінімальне значення:", min(num_list))
        elif choice == 4:
            try:
                index = int(input("Введіть індекс елемента: "))
                print("Значення за індексом:", num_list[index])
            except IndexError:
                print("Помилка: Індекс виходить за межі списку.")
        elif choice == 5:
            try:
                index = int(input("Введіть індекс елемента для видалення: "))
                del num_list[index]
                print("Елемент видалено.")
            except IndexError:
                print("Помилка: Індекс виходить за межі списку.")
        elif choice == 6:
            print("До побачення!")
            break
        else:
            print("Неправильний вибір. Виберіть операцію зі списку.")
except ValueError:
    print("Помилка: Введено некоректне значення. Будь ласка, введіть лише числа через пробіл.")

# TACK №4.1

# Не знаю як зробити

# TACK №4.2

def display_menu():
    print("\nМеню:")
    print("1. Відображення списку")
    print("2. Отримання максимального значення")
    print("3. Отримання мінімального значення")
    print("4. Відображення значення елемента за індексом")
    print("5. Видалення елемента за індексом")
    print("6. Вихід")

def get_user_input():
    try:
        choice = int(input("Введіть номер операції: "))
        return choice
    except ValueError:
        print("Будь ласка, введіть число.")
        return None

def main():
    my_list = []

    while True:
        display_menu()
        choice = get_user_input()

        if choice == 1:
            print("Список:", my_list)
        elif choice == 2:
            if my_list:
                print("Максимальне значення:", max(my_list))
            else:
                print("Список порожній.")
        elif choice == 3:
            if my_list:
                print("Мінімальне значення:", min(my_list))
            else:
                print("Список порожній.")
        elif choice == 4:
            try:
                index = int(input("Введіть індекс елемента: "))
                print(f"Значення за індексом {index}: {my_list[index]}")
            except IndexError:
                print("Помилка: Неправильний індекс. Елемент не знайдено.")
            except ValueError:
                print("Помилка: Будь ласка, введіть ціле число для індексу.")
        elif choice == 5:
            try:
                index = int(input("Введіть індекс елемента для видалення: "))
                if 0 <= index < len(my_list):
                    my_list.pop(index)
                    print(f"Елемент за індексом {index} успішно видалений.")
                else:
                    print("Помилка: Неправильний індекс. Елемент не знайдено.")
            except ValueError:
                print("Помилка: Будь ласка, введіть ціле число для індексу.")
        elif choice == 6:
            print("Дякуємо за використання програми!")
            break
        else:
            print("Помилка: Неправильний вибір операції. Будь ласка, спробуйте знову.")

main()