# Задача: Составить списки простых и не простых чисел из numbers

def get_matrix(n, m, value):
    """
    Создает матрицу (вложенный список) размеров n x m, заполненную значениями value.

    :param n: Количество строк матрицы
    :param m: Количество столбцов матрицы
    :param value: Значение, которым будет заполнена матрица
    :return: Вложенный список (матрица)
    """
    # 🟦 Пустая матрица
    matrix = []

    # 🔄 Создаем строки матрицы
    for _ in range(n):
        row = []  # 🔧 Создаем строку
        for _ in range(m):
            row.append(value)  # Добавляем столбец со значением value
        matrix.append(row)  # Добавляем строку в матрицу

    return matrix

# 🧪 Тестирование функции
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

# 🌟 Вывод результатов
print(result1)  # [[10, 10], [10, 10]]
print(result2)  # [[42, 42, 42, 42, 42], [42, 42, 42, 42, 42], [42, 42, 42, 42, 42]]
print(result3)  # [[13, 13], [13, 13], [13, 13], [13, 13]]