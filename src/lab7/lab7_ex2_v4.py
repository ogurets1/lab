def calculate_sum(n):
    total_sum = 0
    for i in range(n + 1):
        for j in range(i, n + 1):
            total_sum += (3**i - j) / 2
    return total_sum

n = int(input("Введите натуральное число n: "))
result = calculate_sum(n)
print("Результат суммирования:", result)