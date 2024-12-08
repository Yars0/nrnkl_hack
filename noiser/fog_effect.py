import numpy as np
from PIL import Image, ImageFilter
import os

def create_fog_effect_no_noise(image_path, output_image_path, output_mask_path, intensity=0.5):
    """
    Создаёт эффект пелены на изображении и маску пелены без использования библиотеки noise.
    
    :param image_path: Путь к исходному изображению.
    :param output_image_path: Путь для сохранения изображения с эффектом пелены.
    :param output_mask_path: Путь для сохранения маски пелены.
    :param intensity: Интенсивность пелены (значение от 0 до 1).
    """
    # Загружаем изображение
    image = Image.open(image_path).convert("RGB")
    width, height = image.size

    # Генерация случайного шума
    random_noise = np.random.randint(0, 256, (height, width), dtype=np.uint8)

    # Применяем размытие к шуму, чтобы создать текстуру пелены
    fog_texture = Image.fromarray(random_noise).filter(ImageFilter.GaussianBlur(100))

    # Создаём маску пелены
    fog_mask = fog_texture.point(lambda x: x * intensity).convert("L")

    # Создаём пелену как полупрозрачный белый слой
    fog_layer = Image.new("RGB", (width, height), (21, 23, 25))
    fog_layer.putalpha(fog_mask)

    # Накладываем пелену на изображение
    image_with_fog = Image.alpha_composite(image.convert("RGBA"), fog_layer)

    # Сохраняем изображение с эффектом пелены и маску
    image_with_fog.convert("RGB").save(output_image_path, format="JPEG")
    fog_mask.save(output_mask_path, format="PNG")
    print(f"Сохранены изображения: {output_image_path}, {output_mask_path}")

# Пример использования
image_path = "./noiser/_11.jpg"  # Входное изображение
output_image_path = "./dirty_spots_images/fog_effect_no_noise_image.jpg"  # Изображение с эффектом пелены
output_mask_path = "./dirty_spots_images/fog_effect_no_noise_mask.png"  # Маска пелены

create_fog_effect_no_noise(image_path, output_image_path, output_mask_path, intensity=0.7)
