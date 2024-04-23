from PIL import Image, ImageDraw

# Создаем изображение
width, height = 400, 400
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Рисуем домик
draw.rectangle([50, 250, 350, 350], outline="black")
draw.polygon([(50, 250), (200, 50), (350, 250)], outline="black", fill="red")
draw.rectangle([120, 250, 180, 300], outline="black", fill="blue")

# Сохраняем изображение
image.save("house.png")