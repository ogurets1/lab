from PIL import Image, ImageDraw, ImageFont

# Создание изображения
width, height = 400, 200
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Настройки для рисования
font_size = 60
font_color = "black"
font = ImageFont.truetype("arial.ttf", font_size)

# Рисование имени
text = "Lena"
text_width, text_height = draw.textsize(text, font=font)
x = (width - text_width) // 2
y = (height - text_height) // 2
draw.text((x, y), text, font=font, fill=font_color)

# Сохранение изображения
image.save("name.png")

