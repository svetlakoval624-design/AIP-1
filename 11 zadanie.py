# #Задание 11.1)
# print("===Задание 11.1===")
#
# from PIL import Image, ImageFilter
# import os
#
#
# def task_11_1():
# #создаем папку для обработанных картинок
#     output_folder = "filtered_images"
#     os.makedirs(output_folder, exist_ok=True)
#
# #папка с исходниками
#     input_folder = "images"
#
# #проверяем существует ли папка
#     if not os.path.exists(input_folder):
#         print("Папка 'images' не найдена!")
#         return
#
# #обход файлов в папке через os
#     files = os.listdir(input_folder)
#
# #обрабатываем каждый файл
#     for filename in files:
#         input_path = os.path.join(input_folder, filename)
#
#         if os.path.isfile(input_path):
#             name, ext = os.path.splitext(filename)
#             output_path = os.path.join(output_folder, f"blur_{name}{ext}")
#
#             img = Image.open(input_path)
#             img_filtered = img.filter(ImageFilter.BLUR)
#             img_filtered.save(output_path)
#
#             print(f"Обработано: {filename}")
#
#
# task_11_1()
#
# #Задание 11.2)
# print("===Задание 11.2===")
#
# from PIL import Image
# import os
#
# def task_11_2():
#     input_folder = "images"
#
#     if not os.path.exists(input_folder):
#         print("Папка 'images' не найдена!")
#         return
#
#     allowed_extensions = {'.jpg', '.jpeg', '.png'}
#     files = os.listdir(input_folder)
#
#     for filename in files:
#         input_path = os.path.join(input_folder, filename)
#
#         if os.path.isfile(input_path):
#             name, ext = os.path.splitext(filename)
#             ext = ext.lower()
#
#             if ext in allowed_extensions:
#                 img = Image.open(input_path)
#                 width, height = img.size
#                 format_img = img.format
#                 mode = img.mode
#
#                 img.show()
#
#                 print(f"Файл: {filename}")
#                 print(f"Размер: {width} x {height} пикселей")
#                 print(f"Формат: {format_img}")
#                 print(f"Цветовая модель: {mode}")
#
#
# task_11_2()

#Задание 11.3)
print("===Задание 11.3===")

import csv
import os

def task_11_3():
    filename = 'products.csv'


    with open(filename, 'w', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Продукт', 'Количество', 'Цена'])
        writer.writerow(['Молоко', 2, 80])
        writer.writerow(['Сыр', 1, 500])
        writer.writerow(['Хлеб', 2, 70])

    total_sum = 0
    products = []

    with open(filename, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            product = row[0]
            quantity = int(row[1])
            price = int(row[2])
            total_price = quantity * price
            total_sum += total_price
            products.append((product, quantity, price))

    print("Нужно купить:")
    for product, quantity, price in products:
        print(f"{product} - {quantity} шт. за {price} руб.")

    print(f"Итоговая сумма: {total_sum} руб.")


task_11_3()