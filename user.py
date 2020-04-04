class Car:
    def __init__(self, age, name):
        self.age = str(age)
        self.name = name

    def __str__(self):
        www = "Возраст: " + self.age + ", Имя: " + self.name
        return www

car1 = Car(3, 'Bob')
print(car1)