import os

# Указываем путь для библиотеки Tcl/Tk, если они не установлены по умолчанию
os.environ['TCL_LIBRARY'] = r'C:\Program Files\Python313\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Program Files\Python313\tcl\tk8.6'

import tkinter as tk
from tkinter import messagebox


# Функция обработки нажатия кнопок
def on_button_click(symbol):
    current_text = entry.get()
    if symbol == "=":
        try:
            result = eval(current_text)  # Вычисление выражения
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
        except Exception:
            messagebox.showerror("Ошибка", "Некорректное выражение")
    elif symbol == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, symbol)


# 🚀 Стиль Эглит: Проверяем наличие Tkinter и пути к библиотекам Tcl/Tk
def check_tkinter():
    try:
        import tkinter as tk
    except ImportError as e:
        print("🚨 Ошибка импорта Tkinter! Проверьте установку Tcl/Tk.")
        print(f"Причина: {e}. Перейдите в настройки Python или переустановите его.")
        exit(1)  # Завершаем программу с ошибкой, чтобы не тратить время!

    # Проверяем, если проблемы с графическим интерфейсом
    try:
        root = tk.Tk()
        root.title("Графика с Tkinter 💻")
        root.mainloop()
    except Exception as e:
        print(f"🚨 Ошибка при запуске Tkinter: {e}")
        print("Проверьте, что Tcl/Tk правильно установлен и путь корректен. ❌")

# Проверим настройки перед запуском программы
check_tkinter()

# Создание главного окна
root = tk.Tk()
root.title("Калькулятор")

# Поле ввода
entry = tk.Entry(root, width=25, font=("Arial", 18), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Кнопки калькулятора
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Расположение кнопок
row = 1
col = 0
for button in buttons:
    action = lambda x=button: on_button_click(x)
    tk.Button(
        root, text=button, width=5, height=2, font=("Arial", 14), command=action
    ).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Запуск главного цикла программы
root.mainloop()
