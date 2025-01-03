# 🚀 Стиль Эглит: Код с душой и уникальной эстетикой
from random import choice


# 🎨 Разделитель для красоты
def print_separator():
	print("💡" + "⭐" * 40 + "💡")


# 📝 Список цитат
QUOTES = [
	"Успех приходит к тем, кто не сдаётся! 💪",
	"Каждая ошибка — это шаг к победе. 🔥",
	"Робототехника — это будущее, создавай его сегодня! 🤖",
	"Искусственный интеллект начинается с естественного. 🧠",
	"Программируй так, как будто за тобой наблюдают звёзды. 🌌"
]


# 🔮 Функция для генерации случайной цитаты
def generate_quote():
	return choice(QUOTES)


# 🏁 Основной блок программы
if __name__ == "__main__":
	print_separator()
	print("🌟 Добро пожаловать в мир вдохновения! 🌟")
	print_separator()
	print(f"✨ Случайная цитата: {generate_quote()}")
	print_separator()
	print("🔧 Продолжай творить в стиле Эглит!")
