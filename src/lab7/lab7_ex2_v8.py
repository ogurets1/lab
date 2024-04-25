def calculate_average(n, x, m):
   sum_x_k = sum([(x + k) / m for k in range(1, n + 1)])
   return sum_x_k

n = int(input("Введите натуральное число n: "))
x = float(input("Введите действительное число x: "))
m = int(input("Введите число m: "))

average = calculate_average(n, x, m)
print(f"Среднее значение: {average}")