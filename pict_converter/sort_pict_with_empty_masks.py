import os
import shutil
from PIL import Image

source_dir_masks =  "C:\\Users\\minim\\OneDrive\\Документы\\Hackathon_nornikel\\train_dataset\\cv_open_dataset\\open_msk"
source_dir_images = "C:\\Users\\minim\\OneDrive\\Документы\\Hackathon_nornikel\\train_dataset\\cv_open_dataset\\open_img"

destination_dir_masks = "C:\\Users\\minim\\OneDrive\\Документы\\Hackathon_nornikel\\pict_with_empty_masks\\masks"
destination_dir_images = "C:\\Users\\minim\\OneDrive\\Документы\\Hackathon_nornikel\\pict_with_empty_masks\\images"

for mask_file_name in os.listdir(source_dir_masks):
    full_file_path = os.path.join(source_dir_masks, mask_file_name)
    file_size = os.path.getsize(full_file_path)
    with Image.open(full_file_path) as img:
        img_size = img.size
        if img_size == (1920, 1080) and file_size == 7923  or img_size == (800, 600) and file_size == 2478:
            image_file_name = mask_file_name.replace('.png', '.jpg')
            shutil.copy(os.path.join(source_dir_images, image_file_name), os.path.join(destination_dir_images, image_file_name))
            img.save(os.path.join(destination_dir_masks, mask_file_name), 'PNG')