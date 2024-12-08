точка входа для обучения модели - файл main.ipynb
что изменено: 
1. изменен датасет (помимо 250 пар фотографий + 147 синтетических) добавлены собственные пары синтетических изображений/масок (около 250 пар). Добавлено 200 пар фотографий/масок из датасета
2. добавлены несколько новых фильтров (папка /noiser - мало пригодны). 
3. Добавлены конвертеры картинок (папка /pict_converter). 
3.1 файл color_white_black преобразует многоцветные маски к монохромной. Использовался при преобразовании масок из датасета Soiling Detection.
3.2 файл converter.py создан для преобразования форматов изображений. Использовался для реобразовании масок из датасета Soiling Detection.
3.3 файл sort_pict_with_empty_masks.py - отбирает из начальной выборки данные, маски в которых пустые.
4. папка pict_with_empty_masks содержит все изображения и маски с пустыми масками.
5. train18 - последняя обученная модель, получившая финальный скор.
