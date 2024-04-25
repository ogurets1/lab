import my_module

print(my_module.welcome_message())

num = int(input("Введите число для проверки на четность: "))
if my_module.is_even(num):
    print(f"{num} - четное число")
else:
    print(f"{num} - нечетное число")

num = int(input("Введите число для проверки на простоту: "))
if my_module.is_prime(num):
    print(f"{num} - простое число")
else:
    print(f"{num} - составное число")
