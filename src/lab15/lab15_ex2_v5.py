def is_triangle(sides):
    a, b, c = sorted(sides)
    if a + b > c:
        print("Это треугольник")
    else:
        print("Это не треугольник")

# Ввод списка с клавиатуры
sides = list(map(int, input("Введите длины трех отрезков, разделенные пробелами: ").split()))

# Вызов функции
is_triangle(sides)