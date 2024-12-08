import cv2
import numpy as np
import os
from PIL import Image

def add_synthetic_dirt(image_path, output_path, num_spots=10, spot_size_range=(20, 100)):
    """
    Добавляет синтетические пятна грязи на изображение.
    
    :param image_path: Путь к исходному изображению.
    :param output_path: Путь для сохранения изображения с пятнами.
    :param num_spots: Количество пятен.
    :param spot_size_range: Диапазон размеров пятен (минимальный и максимальный радиус).
    """
    # Загружаем изображение
    image = cv2.imread(image_path)
    if image is None:
        print("Ошибка: невозможно загрузить изображение.")
        return

    # Переводим изображение в RGB (если нужно)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Получаем размеры изображения
    height, width, _ = image.shape

    # Копируем изображение для рисования пятен
    dirty_image = image.copy()

    for _ in range(num_spots):
        # Случайный центр пятна
        center_x = np.random.randint(0, width)
        center_y = np.random.randint(0, height)

        # Случайный размер пятна
        radius = np.random.randint(spot_size_range[0], spot_size_range[1])

        # Цвет пятна (темный коричневый, близкий к грязи)
        color = (np.random.randint(21, 26), np.random.randint(21, 26), np.random.randint(20, 26))  # RGB

        # Создаём пятно с размытыми краями
        thickness = -1  # Заполненный круг
        overlay = dirty_image.copy()
        cv2.circle(overlay, (center_x, center_y), radius, color, thickness)

        # Прозрачность пятна (0.5 для полупрозрачности)
        alpha = 0.8
        dirty_image = cv2.addWeighted(overlay, alpha, dirty_image, 1 - alpha, 0)

    # Конвертируем обратно в PIL для сохранения
    dirty_image = Image.fromarray(dirty_image)
    dirty_image.save(output_path)
    print(f"Изображение с синтетическими пятнами сохранено в {output_path}")

# Основной код
image_path = "./noiser/_11.jpg"  # Относительный путь к изображению
output_dir = "./dirty_spots_images"
os.makedirs(output_dir, exist_ok=True)  # Создаём директорию, если её нет

output_path = os.path.join(output_dir, "output_with_dirt12.jpg")
if not os.path.exists(image_path):
    print("Файл не найден:", image_path)
else:
    add_synthetic_dirt(image_path, output_path, num_spots=10, spot_size_range=(30, 120))
