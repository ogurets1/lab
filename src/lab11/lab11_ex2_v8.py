# Ввод списка температур за март
temperatures = [float(input(f"Введите температуру {i+1}-го марта: ")) for i in range(31)]

# Подсчет количества раз, когда температура опускалась ниже 0°С
below_zero_count = sum(1 for temp in temperatures if temp < 0)

# Вывод результата
print("Температура опускалась ниже 0°С", below_zero_count, "раз(а) в марте.")