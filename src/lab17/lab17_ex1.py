import random
import string

# Функция для генерации пароля
def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Функция для генерации N различных паролей длиной K символов
def generate_passwords(N, K):
    passwords = set()
    while len(passwords) < N:
        passwords.add(generate_password(K))
    return passwords

# Ввод количества паролей и их длины
N = int(input("Введите количество паролей: "))
K = int(input("Введите длину паролей: "))

# Генерация паролей и вывод результата
passwords = generate_passwords(N, K)
print("Сгенерированные пароли:")
for password in passwords:
    print(password)