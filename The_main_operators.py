def generate_password(n):
	"""
	Генерирует пароль для заданного числа n.
	:param n: Число для проверки кратности (от 3 до 20)
	:return: Строка, содержащая все подходящие пары чисел
	"""
	result = ""  # Строка для хранения результата

	# Перебираем все числа от 1 до n-1
	for i in range(1, n):
		for j in range(i + 1, n):  # Учитываем только уникальные пары
			if n % (i + j) == 0:  # Проверяем кратность
				result += f"{i}{j}"  # Формируем строку результата

	return result


# 🧪 Тестирование функции
for number in range(3, 21):
	print(f"{number} - {generate_password(number)}")

	"""
	   Объяснение кода:
	1.Внешний цикл for i in range(1, n)
	Перебирает первое число пары от 1 до n−1
	
	2.Вложенный цикл for j in range(i + 1, n)
	Исключает повторяющиеся пары, например, если уже была пара 
	(1,2),то (2,1) не рассматривается.
	
	3.Проверка кратности:
	Используем выражение n%(i+j)==0, чтобы проверить, делится ли 𝑛
	на сумму пары без остатка.
	
	4.Формирование результата:
	Строка result заполняется строковыми представлениями чисел i и j.
	"""

print()


# Альтернативное решение задачи
def generate_password_optimized(n):
	"""
	🌀 Функция:
	Генерирует пароль для заданного числа n.
	📥 Параметры:
	:param n: Число для проверки кратности (от 3 до 20)
	📤 Возвращает:
	:return: Строка, содержащая все подходящие пары чисел
	"""
	result = ""  # 🟦 Строка для хранения результата

	# 🔄 Перебираем числа только до n // 2
	for i in range(1, n):
		j = n - i  # 🔑 Вычисляем второе число пары
		if j > i and n % (i + j) == 0:  # 🎯 Условие уникальности и кратности
			result += f"{i}{j}"  # ✨ Формируем строку результата

	return result ## 🏁 Возвращаем сформированный результат


# 🧪 Тестирование функции
for number in range(3, 21):
	print(f"{number} - {generate_password_optimized(number)}")

	"""
	Преимущества альтернативного подхода:
	1.Уменьшение количества итераций:
	Рассматриваем только числа до n/2, исключая лишние проверки.
	2.Четкость вычислений:
	Второе число пары вычисляется явно, без необходимости вложенного цикла.
	"""