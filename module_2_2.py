# Ввод данных
first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))

# Проверка условий
if first == second == third:
    print(3)  # Все три числа равны
elif first == second or first == third or second == third:
    print(2)  # Два числа равны
else:
    print(0)  # Все числа разные


# программа для выполнения задачи "Все ли равны?"
def check_equal_numbers():
    # Ввод трех целых чисел
    first = int(input("Введите первое число: "))
    second = int(input("Введите второе число: "))
    third = int(input("Введите третье число: "))

    # Проверка условий
    if first == second == third:
        print(3)  # Все числа равны
    elif first == second or first == third or second == third:
        print(2)  # Два числа равны
    else:
        print(0)  # Все числа разные


# Запуск функции
if __name__ == "__main__":
    check_equal_numbers()
