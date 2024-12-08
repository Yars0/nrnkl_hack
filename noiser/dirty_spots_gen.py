from PIL import Image, ImageDraw, ImageFilter
import random
import numpy as np

def add_realistic_dirt(image_path, output_path, num_spots=10, spot_size_range=(20, 100)):
    """
    Добавляет реалистичные пятна грязи на изображение.
    
    :param image_path: Путь к исходному изображению.
    :param output_path: Путь для сохранения изображения с пятнами.
    :param num_spots: Количество пятен.
    :param spot_size_range: Диапазон размеров пятен (минимальный и максимальный радиус).
    """
    # Загружаем изображение
    image = Image.open(image_path).convert("RGB")
    width, height = image.size

    # Копируем изображение
    dirty_image = image.copy()

    for _ in range(num_spots):
        # Генерируем случайный центр и размер пятна
        center_x = random.randint(0, width)
        center_y = random.randint(0, height)
        radius = random.randint(*spot_size_range)

        # Создаём текстурное пятно
        dirt_texture = Image.new("L", (radius * 2, radius * 2), 0)
        texture_draw = ImageDraw.Draw(dirt_texture)

        # Добавляем случайный шум внутри пятна
        for _ in range(50):  # Количество "шумовых точек"
            x = random.randint(0, radius * 2)
            y = random.randint(0, radius * 2)
            texture_draw.ellipse(
                (x, y, x + random.randint(3, 10), y + random.randint(3, 10)),
                fill=random.randint(50, 150),
            )

        # Размываем текстуру для более реалистичного вида
        dirt_texture = dirt_texture.filter(ImageFilter.GaussianBlur(40))

        # Создаём цветное пятно
        dirt_color = Image.new(
            "RGB",
            (radius * 2, radius * 2),
            (
                random.randint(50, 80),
                random.randint(40, 70),
                random.randint(30, 50),
            ),
        )
        dirt_color.putalpha(dirt_texture)

        # Накладываем пятно на изображение
        dirty_image.paste(dirt_color, (center_x - radius, center_y - radius), dirt_texture)

    # Сохраняем результат
    dirty_image.save(output_path, format="JPEG")
    print(f"Сохранено изображение с пятнами: {output_path}")

# Пример использования
image_path = "./noiser/_11.jpg"
output_path = "./dirty_spots_images/realistic_dirt_output.jpg"
add_realistic_dirt(image_path, output_path, num_spots=10, spot_size_range=(50, 200))


