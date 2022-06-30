# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python i an object

#create a class
class User:
    #constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        
    def greeting(self):
        return f"My name is {self.name} and I am {self.age}"
    
    def has_birthday(self):
        self.age += 1


# Extend another class
class Custumer(User):
    def __init__(self, name, email, age):
       self.name = name
       self.email = email
       self.age = age
       
    def set_balance(self, balance):
        self.balance = balance
    
    def greeting(self):
        return f"My name is {self.name} and I am {self.age} and my balance is {self.balance}"

#Initialize an object 
brad = User("Edilson Lopes", "test@gmail.com", 24)
janet = Custumer("Janet Johnson", 'jhonson@gmail.com', 65)

janet.set_balance(500)
print(brad.greeting())

brad.has_birthday()
print(brad.greeting())




        


