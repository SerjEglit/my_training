# Задача: Составить списки простых и не простых чисел из numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# 🔧 Пустые списки для результата
primes = []  # Список для хранения простых чисел
not_primes = []  # Список для хранения составных чисел

# 🌐 Итерация по всем числам в numbers
for number in numbers:  # Проходим по каждому числу из списка numbers
	# 🔒 Переменная-флаг для проверки на простоту
	is_prime = True  # Предполагаем, что число простое

	# 📀 Особый случай для 1
	if number <= 1:  # Если число меньше или равно 1, пропускаем его
		continue

	# 🔄 Поиск делителей в диапазоне от 2 до квадратного корня числа (включительно)
	for divisor in range(2, int(number ** 0.5) + 1):  # Проверяем делимость на числа от 2 до sqrt(number)
		if number % divisor == 0:  # Если нашли делитель, число не простое
			is_prime = False  # Меняем флаг на False
			break  # Прерываем цикл, дальнейшая проверка не нужна

	# ✅ Относим число к списку primes или not_primes
	if is_prime:  # Если флаг остался True, число простое
		primes.append(number)  # Добавляем число в список primes
	else:  # Если флаг стал False, число составное
		not_primes.append(number)  # Добавляем число в список not_primes

# 🌟 Вывод результатов
print(f"Primes: {primes}")  # Вывод списка простых чисел
print(f"Not Primes: {not_primes}")  # Вывод списка составных чисел

# Альтернативное решение
# Задача: Составить списки простых и не простых чисел из numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


# Функция для проверки, является ли число простым
def is_prime_number(number):
	if number <= 1:
		return False  # 1 и меньше не являются простыми числами
	for divisor in range(2, int(number ** 0.5) + 1):
		if number % divisor == 0:
			return False  # Найден делитель, число не простое
	return True  # Число простое


# 🔧 Создаем списки для результатов
primes = [num for num in numbers if is_prime_number(num)]  # Простые числа
not_primes = [num for num in numbers if num > 1 and not is_prime_number(num)]  # Составные числа

# 🌟 Вывод результатов
print(f"Primes: {primes}")  # Вывод списка простых чисел
print(f"Not Primes: {not_primes}")  # Вывод списка составных чисел
