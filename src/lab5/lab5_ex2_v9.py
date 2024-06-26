# Заданная сумма
desired_sum = 324

# Первый член последовательности
first_term = 5

# Шаг последовательности
step = 4

# Инициализация счетчика
count = 0

# Переменная для хранения текущей суммы
current_sum = 0

# Пока текущая сумма меньше или равна заданной сумме
while current_sum < desired_sum:
    # Увеличиваем счетчик на 1
    count += 1
    # Добавляем следующий член последовательности к текущей сумме
    current_sum += first_term + (count - 1) * step

# Выводим результат
print("Для получения суммы, равной", desired_sum, "нужно взять", count, "слагаемых.")
