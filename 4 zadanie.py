#Задание 4.1)
from math import remainder

password1=input("Введите пароль:")
password2=input("Подтвердите пароль:")

if password1 == password2:
    print("Пароль принят!")
else:
    print("Пароль не принят")


#Задание 4.2)
n=int(input("Введите номер места (1-54):"))
remainder=n%4
if remainder==1:
    print("нижнее боковое")
elif remainder==2:
    print("верхнее в купе")
elif remainder==3:
    print("нижнее в купе")
elif remainder==0:
    print("верхнее боковое")


#Задание 4.3)
y=int(input("Введите номер года:"))

if (4<=y<=100) or (y==400):
    print(f"Год - високосный", y)
else:
    print("Год не високосный")


#Задание 4.4)
color1=input("Введите первый цвет:")
color2=input("Введите второй цвет:")

primary={"красный","синий","жёлтый"} #проверка, что оба цвета основные
colors=sorted([color1,color2])

if colors==["красный","синий"]:
    print("фиолетовый")
elif colors ==["красный","жёлтый"]:
    print("оранжевый")
elif colors ==["синий","жёлтый"]:
    print("зелёный")
    