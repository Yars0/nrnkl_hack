from PIL import Image
import os
import numpy as np

def process_image(input_path, output_path):
    # Открываем изображение
    image = Image.open(input_path).convert("RGBA")
    pixels = image.load()

    # Проходим по всем пикселям
    for y in range(image.height):
        for x in range(image.width):
            r, g, b, a = pixels[x, y]  # Получаем цвет пикселя
            if r > 0 and g == 0 and b == 0:  # Если пиксель красный
                pixels[x, y] = (255, 255, 255, 255)  # Делаем его белым
            else:
                pixels[x, y] = (0, 0, 0, 0)  # Остальные делаем прозрачными

    # Сохраняем результат
    image.save(output_path, "PNG")
    print(f"Обработанное изображение сохранено в: {output_path}")



def convert_red_to_white(input_path, output_path):
    """
    Переводит красный цвет в изображении в белый, остальные цвета в чёрный.
    
    :param input_path: Путь к входному изображению (формат .png или другой).
    :param output_path: Путь для сохранения обработанного изображения.
    """
    try:
        # Открываем изображение и переводим его в режим RGB
        image = Image.open(input_path).convert("RGB")

        # Преобразуем изображение в массив NumPy
        image_array = np.array(image)

        # Определяем красный цвет
        red_color = [255, 0, 0]

        # Создаём маску для красного цвета
        red_mask = (image_array == red_color).all(axis=-1)

        # Создаём новое изображение, где все пиксели чёрные
        processed_array = np.zeros_like(image_array)

        # Устанавливаем красные пиксели в белый цвет
        processed_array[red_mask] = [255, 255, 255]  # Белый
        processed_array[~red_mask] = [0, 0, 0]       # Чёрный

        # Преобразуем обработанный массив обратно в изображение
        processed_image = Image.fromarray(processed_array)

        # Сохраняем изображение
        processed_image.save(output_path)

        print(f"Обработанное изображение сохранено в: {output_path}")
    except Exception as e:
        print(f"Ошибка при обработке изображения: {e}")


source_dir = 'C:\\Users\\minim\\Downloads\\soiling_dataset\\train\\rgbLabels' #директория, откуда искать маски
destination_dir = 'C:\\Users\\minim\\Downloads\\soiling_dataset\\train\\rgbLabelsBin' #директория, куда сохранять маски

for file in os.listdir(source_dir):
    convert_red_to_white(os.path.join(source_dir, file), os.path.join(destination_dir, f'{file.split('.')[0]}.png'))
