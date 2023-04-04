class Car:
    """Attempt to model a basic car"""
    def __init__(self,make,model,year):
        #Initialize instance attributes
        self.make = make
        self.model = model
        self.year = year

        #More attributes
        self.fuel_capacity = 50
        self.fuel_type = '98 octanes'
        self.fuel_level = 0
        self.fuel_efficiency = 0.95

    #Some methods
    def fill_tank(self):
        '''Fill gas tank to capacity'''
        self.fuel_level = self.fuel_capacity
    
    def drive(self):
        '''Simulate driving'''
        print('The car is driving')
    
    def brake(self):
        '''Simulate braking'''
        print('The car is braking')
    
    def turn(self):
        '''Simulate turning'''
        print('The car is turning either left or right')
    
#Creating an object from a class
my_car = Car('Audi','RS4', 2018)
my_other_car = Car('Lamborghini','Urus', 2022)

#Accessing attribute values
print(my_car.make)
print(my_car.model)
print(my_car.year)
print(my_other_car.make)
print(my_other_car.model)
print(my_other_car.year)

#Calling methods for each object

my_car.drive()
my_car.brake()
my_car.turn()
my_other_car.drive()
my_other_car.brake()
my_other_car.turn()

#Modifying attributes directly

my_car.fuel_level = 1.5
my_car.fuel_capacity = 53
my_other_car.fuel_capacity = 65
my_other_car.fuel_level = 8

