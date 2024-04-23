def welcome_message():
    return "Добро пожаловать в мой модуль! Этот модуль содержит несколько функций для демонстрации работы с модулями в Python."

def is_even(num):
    return num % 2 == 0

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True