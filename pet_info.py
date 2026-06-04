class Pet:

    def __init__(self, name="", animal_type="", age=0):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def get_year_model(self):
        return self.__year_model

    def get_make(self):
        return self.__make

    def get_speed(self):
        return self.__speed