from PIL import Image

# Открытие изображения
image = Image.open("1.jpg")

# Преобразование в черно-белое изображение
bw_image = image.convert("L")

# Зеркальное отражение относительно центральной вертикальной оси
mirrored_image = bw_image.transpose(Image.FLIP_LEFT_RIGHT)

# Изменение размера изображения
new_size = (400, 300)  # новая ширина и высота
resized_image = mirrored_image.resize(new_size)

# Сохранение преобразованного изображения
resized_image.save("2.jpg")

# Показ изображения
resized_image.show()