n = int(input("Введите натуральное число n: "))

sum = 0
for i in range(n):
for j in range(i, n):
sum += (n + i) / (2 * i + j + 1)

print("Значение суммы равно:", sum)