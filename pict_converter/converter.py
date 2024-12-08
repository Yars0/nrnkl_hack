from PIL import Image
import os

def convert_png_to_jpg(input_path, output_path, quality=95):
    """
    Конвертирует изображение из формата PNG в формат JPG.

    :param input_path: Путь к исходному PNG изображению.
    :param output_path: Путь для сохранения JPG изображения.
    :param quality: Качество JPG изображения (по умолчанию 95).
    """
    try:
        # Открываем PNG изображение
        with Image.open(input_path) as img:
            # Убедимся, что изображение в режиме RGB (не RGBA)
            if img.mode == 'RGBA':
                img = img.convert('RGB')
            
            # Сохраняем изображение в формате JPG
            img.save(output_path, format='JPEG', quality=quality)
            print(f"Изображение успешно конвертировано: {output_path}")
    except Exception as e:
        print(f"Ошибка при конвертации: {e}")

source_dir = 'C:\\Users\\minim\\Downloads\\soiling_dataset\\train\\rgbImages'
destination_dir = 'C:\\Users\\minim\\Downloads\\soiling_dataset\\train\\rgbImagesJpg'

for file in os.listdir(source_dir):
    #print(file)
    # Пример использования
    convert_png_to_jpg(os.path.join(source_dir, file), os.path.join(destination_dir, f'{file.split('.')[0]}.jpg'))
