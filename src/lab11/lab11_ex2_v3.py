# Ввод последовательности
sequence = [int(input(f"Введите элемент {i+1}: ")) for i in range(16)]

# Создание списка из значений под четными номерами
even_index_values = [sequence[i] for i in range(0, len(sequence), 2)]

# Вывод результата
print("Список из значений под четными номерами:", even_index_values)