#Задание 6.1)
print("  Задание 6.1)")
def divisible_by_3(n):
    return n % 3==0

num=int(input("Введите число:"))
if divisible_by_3(num):
    print(f"{num} делится на 3")
else:
    print(f"{num} не делится на 3")

#Задание 6.2)
print("  Задание 6.2)")
def divide_100(x):
    return 100/x

try:
    num=float(input("Введите число для деления 100 на него:"))
    result=divide_100(num)
    print(f"100/{num}={result}")
except ZeroDivisionError:
    print("Ошибка! Деление на ноль невозможно!")
except ValueError:
    print("Ошибка! Введите число, а не текст!")


#Задание 6.3)
print("  Задание 6.3)")
def is_magic_date(day,month,year):
    last_two=year % 100
    return day * month == last_two
d=int(input("День:"))
m=int(input("Месяц:"))
y=int(input("Год:"))
if is_magic_date(d,m,y):
    print("Магическая дата!")
else:
    print("Дата не магическая!")


#Задание 6.4)
print("  Задание 6.4)")

