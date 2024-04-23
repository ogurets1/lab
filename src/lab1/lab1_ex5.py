# Вводим цену пирожка (рубли и копейки) и количество пирожков
rubles = int(input("Введите цену пирожка в рублях: "))
kopecks = int(input("Введите цену пирожка в копейках: "))
quantity = int(input("Введите количество пирожков: "))

# Вычисляем общую сумму в копейках
total_kopecks = rubles * 100 + kopecks
# Вычисляем общую сумму в рублях и копейках
total_rubles = total_kopecks * quantity // 100
total_kopecks = total_kopecks * quantity % 100

print("Общая сумма:", total_rubles, "руб.", total_kopecks, "коп.")