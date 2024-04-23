import random
# Генерируем случайное трехзначное число
random_number = random.randint(100, 999)
# Выводим отдельные цифры через запятую
print(f"Отдельные цифры: {random_number // 100}, {random_number // 10 % 10}, {random_number % 10}")