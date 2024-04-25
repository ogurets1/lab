# Ввод строки, подстроки для замены и новой подстроки
string = input("Введите строку: ")
substring_to_replace = input("Введите подстроку для замены: ")
new_substring = input("Введите новую подстроку: ")

# Замена подстроки
result = string.replace(substring_to_replace, new_substring)

# Вывод результата
print("Результат замены:", result)
