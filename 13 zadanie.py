#Задание 13.1)
print("===Задание 13.1===")
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Ресторан: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name} открыт!")


newRestaurant = Restaurant("Уютный дворик", "Русская кухня")
print(newRestaurant.restaurant_name)
print(newRestaurant.cuisine_type)
newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()


#Задание 13.2)
print("===Задание 13.2===")
restaurant1 = Restaurant("Моя Италия", "Итальянская кухня")
restaurant2 = Restaurant("Утро Японии", "Японская кухня")
restaurant3 = Restaurant("Маленький Париж", "Французская кухня")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()


#Задание 13.3)
print("===Задание 13.3===")
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = 0

    def describe_restaurant(self):
        print(f"Ресторан: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name} открыт!")

    def update_rating(self, new_rating):
        self.rating = new_rating
        print(f"Рейтинг ресторана {self.restaurant_name} обновлён до {self.rating}")


my_restaurant = Restaurant("Морской бриз", "Средиземноморская кухня")
my_restaurant.describe_restaurant()
print(f"Текущий рейтинг: {my_restaurant.rating}")
my_restaurant.update_rating(5)
print(f"Новый рейтинг: {my_restaurant.rating}")