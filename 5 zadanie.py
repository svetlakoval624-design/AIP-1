#Задание 5.1)
print("  Задание 5.1)")
n=int(input("Введите кол-во слов:"))
result=" "
for i in range(n):
    word=input(f"Введите слово{i+1}:")
    if i==0:
        result=word
    else:
        result+= " " + word
        print("Результат:", result)


#Задание 5.2)
print("  Задание 5.2)")
words=[]
while True:
    word=input("Введите слово или 'stop' для завершения:")
    if word.lower()=="stop":
        break
        words.append(word)


#Задание 5.3)
print("  Задание 5.3)")
word=input("Введите слово:")
print("Вы ввели:", repr(word))
if "ф" in word.lower():
    print("Ого! Это редкое слово!")
else:
    print("Эх, это не очень редкое слово...")


#Задание 5.4)
print("  Задание 5.4)")
import random
correct=0
errors=0
print("Игра Математика для детей")
print("Нужно решить примеры. После 3 ошибок игра закончится!")
while errors < 3:
    a=random.randint(1,9)
    b=random.randint(1,9)
    print(f"{a}+{b}=", end="")
    answer=input()
    if answer==str(a+b):
        print("Правильно!")
        correct+=1
    else:
        print("Ответ неверный.")
        errors+=1
        print("Игра окончена. Правильных ответов:", correct)
