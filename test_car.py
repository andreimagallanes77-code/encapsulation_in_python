class Car:

    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def get_year_model(self):
        return self.__year_model

    def get_make(self):
        return self.__make

    def get_speed(self):
        return self.__speed

    def set_year_model(self, year_model):
        self.__year_model = year_model

    def set_make(self, make):
        self.__make = make

    def accelerate(self):
        self.__speed += 8

    def brake(self):
        self.__speed -= 8

car1 = Car(2024, "Toyota")

print("Car Information")
print("Year Model:", car1.get_year_model())
print("Make:", car1.get_make())
print("Current Speed:", car1.get_speed())

print("\nAccelerating...")
for i in range(5):
    car1.accelerate()
    print("Current Speed:", car1.get_speed())

print("\nBraking...")
for i in range(5):
    car1.brake()
    print("Current Speed:", car1.get_speed())



