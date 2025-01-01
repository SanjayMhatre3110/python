class Dog():
	"""A simple attempt to model a dog."""
	def __init__(self, name, age):
		"""Initialize name and age attributes."""
		self.name = name
		self.age = age
	def sit(self):
		"""Simulate a dog sitting in response to a command."""
		print(self.name.title() + " is now sitting.")
	def roll_over(self):
		"""Simulate rolling over in response to a command."""
		print(self.name.title() + " rolled over!")
	
my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")	

## excersize 9.1 - second class 
class Resturant():
	def __init__(self,r_name,r_type,**details):
		self.resto = {}
		self.resto['rest_name']=r_name
		self.resto['rest_type']=r_type
		for k,v in details.items():
			self.resto[k]=v
	def roll_over(self):
		print("\nyour hotel "+" is now rolling")

desc_rest = Resturant('sai krupa','lapeta',cost='medium',staff='good',rating='5 star')
print(desc_rest.resto)
desc_rest.roll_over()









class Car():
	"""A simple attempt to represent a car."""
	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading=0
	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
	def read_odometer(self):
		"""Print a statement showing the car's mileage."""
		print("This car has " + str(self.odometer_reading) + " miles on it.")
	def update_odometer(self, mileage):
		"""
		Set the odometer reading to the given value.
		Reject the change if it attempts to roll the odometer back.
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")	
	def increment_odometer(self, miles):
		"""Add the given amount to the odometer reading."""
		self.odometer_reading += miles		
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
print(my_new_car.read_odometer())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
my_new_car.update_odometer(43)
my_second_car = Car('BMW', 'B6', 2010)
print(my_second_car.get_descriptive_name())
print(my_second_car.read_odometer())
my_second_car.read_odometer()
my_new_car.read_odometer()
my_new_car.increment_odometer(120)
my_new_car.read_odometer()









# Resturant class 9.1
class Resturant():
    """"this class represent a resturant"""
    def __init__(self, resturant_name, crusine_type):
        """This is a constructor class"""
        self.resturant_name = resturant_name
        self.crusine_type = crusine_type
        self.number_served=0
    
    def describe_resturant(self):
        """This method describes resturant"""
        print(f"{self.resturant_name} serves {self.crusine_type}")
    
    def open_resturant(self):
        """This method opens resturant"""
        print(f"{self.resturant_name} resturant is open now")
    def set_number_served(self,ke):
        self.number_served = ke
    def increment_number_served(self,le):
        self.number_served+=le

resturant = Resturant("Sai Krupa", "Italian")
print(f"Resturant {resturant.resturant_name} has best {resturant.crusine_type} crusine in the panvel city")
resturant.describe_resturant()
resturant.open_resturant()
print(resturant.number_served)
resturant.increment_number_served(110)
print(resturant.number_served)






## excersize 9.5
class User():
    """This class respresent users stores many attributes"""
    def __init__(self, first_name, last_name, **user_info):
        """this is constructor class"""
        self.login_attempts=15
        self.user_info = {}
        self.user_info["user_first_name"] = first_name
        self.user_info["user_last_name"] = last_name
        for k, v in user_info.items():
            self.user_info[k]=v
    
    def describe_users(self):
        """This method describes user by printing attributes"""
        print(f"This is user information: {self.user_info}")
    
    def greet_user(self):
        """this method greets user"""
        print("Wecome "+self.user_info["user_first_name"]+" "+self.user_info["user_last_name"])
    def increament_login_attempt(self):
        self.login_attempts+=1
    def reset_login_attempt(self):
        self.login_attempts=0
user_1 = User("Rajesh", "mhatre", age=38, sport="TT")
user_1.describe_users()
user_1.greet_user()

user_2 = User("Harshal", "Patil", age=58, sport="FUgadi")
user_2.describe_users()
user_2.greet_user()
usr_lgin_atpm = User('sanjay','mhatre')
print(user_1.login_attempts)
user_1.increament_login_attempt()
print(user_1.login_attempts)
user_1.reset_login_attempt()
print(user_1.login_attempts)
