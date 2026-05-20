# #Задание 9.1)
# from PIL import Image
#
# def task_9_1(image_path):
#     #открываем картинкку
#     img = Image.open(image_path)
#
#     #получаем информацию
#     width, height = img.size
#     format_img = img.format
#     mode = img.mode
#
#     #вывод картинки на экран
#     img.show()
#
#     print(f"Размер: {width} x {height} пикселей")
#     print(f"Формат: {format_img}")
#     print(f"Цветовая модель: {mode}")
#
#
#
# task_9_1("cat.jpg")
#
# #Задание 9.2)
# from PIL import Image
#
# def task_9_2(image_path):
#     img = Image.open(image_path)
#
#     new_size = (img.width // 3, img.height // 3)
#     img_resized = img.resize(new_size, Image.Resampling.LANCZOS)
#     img_resized.save("small_image.jpg")
#     print("Уменьшенное изображение сохранено как small_image.jpg")
#
#     img_mirror_horizontal = img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
#     img_mirror_horizontal.save("mirror_horizontal.jpg")
#     print("Горизонтальное отражение сохранено как mirror_horizontal.jpg")
#
#     img_mirror_vertical = img.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
#     img_mirror_vertical.save("mirror_vertical.jpg")
#     print("Вертикальное отражение сохранено как mirror_vertical.jpg")
#
# task_9_2("cat.jpg")
#
# #Задание 9.3)
# from PIL import Image, ImageFilter
# import os
#
# def task_9_3():
#     #создание новой папки для обработанных картинок
#     output_folder = "filtered_images"
#     os.makedirs(output_folder, exist_ok=True)
#
#     #обработка 5 картинок
#     for i in range(1, 6):
#         input_filename = f"{i}.jpg"
#         output_filename = f"emboss_{i}.jpg"
#         output_path = os.path.join(output_folder, output_filename)
#
#         #Проверяем, существует ли файл
#         if os.path.exists(input_filename):
#             img = Image.open(input_filename)
#
#             #применяем фильтр "Тиснение" (3D эффект)
#             img_filtered = img.filter(ImageFilter.EMBOSS)
#
#             #Сохраняем в новую папку
#             img_filtered.save(output_path)
#             print(f"Обработано: {input_filename} -> {output_path}")
#         else:
#             print(f"Файл {input_filename} не найден!")
#
# task_9_3()

#Задание 9.4)
from PIL import Image, ImageDraw, ImageFont
import os


def add_watermark_single(input_path, output_path, text="Watermark", opacity=120):

    #Открываем изображение
    img = Image.open(input_path).convert("RGBA")

    #Создаем прозрачный слой для водяного знака
    watermark_layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(watermark_layer)

    #Пытаемся загрузить шрифт
    try:
        font = ImageFont.truetype("arial.ttf", 50)
    except:
        try:
            font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 50)
        except:
            font = ImageFont.load_default()
            print("Используется стандартный шрифт")

    #Вычисляем размер текста
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    #Позиция (нижний правый угол)
    margin = 20
    position = (img.width - text_width - margin, img.height - text_height - margin)

    #Рисуем текст
    draw.text(position, text, fill=(255, 255, 255, opacity), font=font)

    #Объединяем слои
    watermarked = Image.alpha_composite(img, watermark_layer)
    watermarked = watermarked.convert("RGB")
    watermarked.save(output_path)
    print(f"Водяной знак добавлен: {output_path}")


def task_9_4_multiple():

    #Создаём папку для результатов
    output_folder = "watermarked"
    os.makedirs(output_folder, exist_ok=True)

    #Обрабатываем 5 картинок
    for i in range(1, 6):
        input_path = f"{i}.jpg"
        output_path = os.path.join(output_folder, f"watermarked_{i}.jpg")

        if os.path.exists(input_path):
            add_watermark_single(input_path, output_path, "Funny Photo", 120)
        else:
            print(f"Файл {input_path} не найден!")

task_9_4_multiple()
