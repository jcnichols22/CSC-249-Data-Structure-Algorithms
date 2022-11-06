class Car:
    #constructor
    def __init__(self, year, make):
        self.__year_model = year
        self.__make = make
        self.__speed = 0
    #accelerate method
    def accelerate(self):
        self.__speed += 5
    #brake method
    def brake(self):
        if(self.__speed >= 5):
            self.__speed -= 5
        else:
            self.__speed = 0
    #method to get current speed
    def get_speed(self):
        return self.__speed

c = Car(2020, "Honda")
c.accelerate();
print(c.get_speed())
c.accelerate();
print(c.get_speed())
c.accelerate();
print(c.get_speed())
c.accelerate();
print(c.get_speed())
c.accelerate();
print(c.get_speed())
c.brake()
print(c.get_speed())
c.brake()
print(c.get_speed())
c.brake()
print(c.get_speed())
c.brake()
print(c.get_speed())
c.brake()
print(c.get_speed())