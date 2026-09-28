# class Car:
#     def __init__(self, brand,model):   #constructor to initilize the attributes
#         self.brand=brand
#         self.model = model
        
#     def start_engine(self):
#         print(f"{self.brand} {self.model} engine runing now")
        
# car1=Car("Suzuki","Mehran")
# car1.start_engine()  #calling the method using the object
# print(car1.model)  #accessing the attribute using the object
# car2=Car("audi","A5")
# car2.start_engine()  #calling the method using the object
# print(car2.brand)


# class Dog:
#     species="canine"
#     def __init__(self, name, age):
#         self.name = name
#         self.age=age
# dog1=Dog("german",3)
# print(dog1.species)  #accessing the class attribute using the object
# print(dog1.name,dog1.age)



class Animal:
    def eat(self):
        print("Eating...")
        
class Dog(Animal):
    def bark(self):
        print("Woof!")

dog=Dog()
dog.eat()  #calling the method from the parent class using the child class object
dog.bark()

