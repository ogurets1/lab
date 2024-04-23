import module1

# Ввод списка A
A = [int(x) for x in input("Введите элементы списка A через пробел: ").split()]
# Ввод значения K
K = int(input("Введите значение K: "))

# Вызов функции и вывод результата
B = module1.copy_without_value(A, K)
print("Список B (без элементов равных K):", B)