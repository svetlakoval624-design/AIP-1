#Задание 7.1)
print("===Задание 7.1)===")
numbers=[17,27,37,42,99]
user_num=int(input("Введите число:"))
print(f"Исходный список: {numbers}")
if user_num in numbers:
    print("Поздравляю, Вы угадали число!")
else:
    print("Нет такого числа!")

#Задание 7.2)
print("===Задание 7.2)===")
my_list=[3,7,2,7,9,3,5,1,7]
print(f"Исходный список: {my_list}")
found_duplicates = set()
for item in my_list:
    if my_list.count(item)>1:
        found_duplicates.add(item)
if found_duplicates:
    print(f"Повторяющиеся элементы: {list(found_duplicates)}")
else:
    print("Повторяющихся элементов нет")

#Задание 7.3)
print("===Задание 7.3)===")
days=("Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье")
weekend_count=int(input("Сколько выходных на неделе вы хотите:"))
weekend_days=list(days[-weekend_count:])
work_days=list(days[:-weekend_count])
print(f"Ваши выходные дни: {weekend_days}")
print(f"Ваши рабочие дни: {work_days}")

#Задание 7.4)
print("===Задание 7.4)===")
group1=["Иванов","Петров","Сидоров","Козлов","Смирнов","Волков","Морозов","Кузнецов","Лебедев","Будилов"]
group2=["Александров","Борисов","Васильев","Зайцев","Жуков","Комаров","Григорьев","Попов","Соколов","Новиков"]
print(f"Группа 1: {group1}")
print(f"Группа 2: {group2}")
team=tuple(group1[:5]+group2[:5])
print(f"Команда: {team}")
print(f"Длина кортежа: {len(team)}")

sorted_team=tuple(sorted(team))
print(f"Отсортированная команда: {sorted_team}")

#проверяем студента морозова
count_morozov=team.count("Морозов")
print(f"Фамилия 'Морозов' встречается {count_morozov} раз(а)")
if "Морозов" in team:
    print("Студент Морозов входит в команду")
else:
    print("Студент Морозов НЕ входит в команду")