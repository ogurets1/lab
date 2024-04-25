# Ввод списка Х
X = [int(input(f"Введите элемент {i+1}: ")) for i in range(15)]

# Нахождение наибольшего элемента и его порядкового номера
max_value = max(X)
max_index = X.index(max_value)

# Вывод результата
print("Наибольший элемент:", max_value)
print("Его порядковый номер:", max_index + 1)