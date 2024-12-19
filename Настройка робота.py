from datetime import time

import emoji

print(emoji.emojize("Python is fun :snake:"))

# Вывод: Python is fun 🐍

print("🔧 Настройка робота... 🚀")


def task_status(status):
	icons = {"выполнено": "✅", "ошибка": "❌", "в процессе": "⏳"}
	return icons.get(status, "❓")  # Если статус не распознан


print(f"Задача: {task_status('выполнено')}")
print("📊 Начало тестов")
print("===================")
print("✅ Тест 1: пройден")
print("❌ Тест 2: ошибка")
print("===================")
print("🔚 Конец тестов")


# 📡 Эглит Сергей Николаевич, 54 года. Миссия: научить робота работать, а не лениться.
# 🛠️ Управление скоростью и направлением движения.

def control_robot_arm(speed: float, direction: str) -> str:
	"""
	🤖 Управляет движением робота с максимальной ясностью и минимальными рисками.

	:param speed: Скорость движения (в м/с).
	:param direction: Направление движения ('вверх', 'вниз', 'влево', 'вправо').
	:return: Результат выполнения команды.
	"""
	# ——— Проверяем входные данные — кто-то ведь должен следить за порядком
	valid_directions = ['вверх', 'вниз', 'влево', 'вправо']
	if direction not in valid_directions:
		return f"💥 Ошибка: направление '{direction}' не поддерживается. Робот теряет терпение!"

	# ——— Настраиваем скорость — медленно, но уверенно
	adjusted_speed = max(0.1, min(speed, 5.0))  # Всё по инструкции: от 0.1 до 5.0 м/с

	# ——— Сообщаем результат работы — робот любит говорить
	return f"✅ Движение: {direction}. Скорость: {adjusted_speed} м/с. Хорошая работа, Эглит!"


# Пример использования
print(control_robot_arm(3.5, 'вверх'))  # Ожидаемый результат: успешное выполнение
print(control_robot_arm(0, 'непонятно'))  # Ожидаемый результат: сообщение об ошибке


def test_robot_logic():
	"""
	📊 Тестируем мозги робота — пусть докажет свою эффективность.
	"""
	print("🔍 Начало испытаний Эглит-Бота 3000:\n")

	# ——— Список испытаний
	test_cases = [
		{"speed": 2.5, "direction": "вправо", "expected": "✅"},
		{"speed": 0, "direction": "вверх", "expected": "✅"},
		{"speed": 6.0, "direction": "влево", "expected": "✅"},
		{"speed": 3.2, "direction": "вперед", "expected": "💥"}
	]

	# ——— Запускаем тесты
	for i, test in enumerate(test_cases, 1):
		print(f"⚙️ Тест #{i}: Скорость {test['speed']}, направление '{test['direction']}'")
		result = control_robot_arm(test["speed"], test["direction"])
		status = "✅ Успех" if test["expected"] in result else "❌ Провал"
		print(f"🔹 Результат: {result} | {status}\n")

	print("📌 Все тесты завершены. Выдержка робота доказана!\n")


# Запускаем тесты
test_robot_logic()
