class Fan:
    # Constants
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=SLOW, radius=5, color="blue", on=False):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on

    def get_speed(self):
        return self.__speed

    def get_radius(self):
        return self.__radius

    def get_color(self):
        return self.__color

    def get_on(self):
        return self.__on

    def set_speed(self, speed):
        self.__speed = speed

    def set_radius(self, radius):
        self.__radius = radius

    def set_color(self, color):
        self.__color = color

    def set_on(self, on):
        self.__on = on

fan1 = Fan()
fan1.set_speed(Fan.FAST)
fan1.set_radius(10)
fan1.set_color("yellow")
fan1.set_on(True)

fan2 = Fan()
fan2.set_speed(Fan.MEDIUM)
fan2.set_radius(5)
fan2.set_color("blue")
fan2.set_on(False)

print("Fan 1")
print("Speed:", fan1.get_speed())
print("Radius:", fan1.get_radius())  # Wrong object
print("Color:", fan1.get_color())
print("On:", fan1.get_on())

print("")

print("Fan 2")
print("Speed:", fan2.get_speed())
print("Radius:", fan2.get_radius())
print("Color:", fan2.get_color())
print("On:", fan2.get_on())