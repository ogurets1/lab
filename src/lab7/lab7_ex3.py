import random
import math

# Цикл для генерации 10 случайных чисел и вычисления их квадратных корней
for _ in range(10):
    num = random.randint(-10, 10)
    if num < 0:
        continue
    elif num == 0:
        break
    else:
        print(f"Квадратный корень из {num}: {math.sqrt(num)}")
