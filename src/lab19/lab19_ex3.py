from PIL import Image

# Открытие изображения
image = Image.open("1.jpg")

# Получение размеров изображения
width, height = image.size

# Создание нового изображения
new_image = Image.new("RGB", (width, height))

# Обработка каждого пикселя
for y in range(height):
    for x in range(width):
        # Получение цвета пикселя
        pixel = image.getpixel((x, y))
        red, green, blue = pixel

        # Нахождение минимального и максимального значения компонент
        min_value = min(red, green, blue)
        max_value = max(red, green, blue)

        # Применение преобразований
        new_red = min_value
        new_green = green
        new_blue = max_value

        # Запись цвета пикселя в новое изображение
        new_image.putpixel((x, height - y - 1), (new_red, new_green, new_blue))

# Сохранение преобразованного изображения
new_image.save("3.jpg")

# Показ преобразованного изображения
new_image.show()