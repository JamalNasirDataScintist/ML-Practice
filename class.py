# class Car:
#     def __init__(self,model,brand):  #constructor to initilize the attributes
#         self.model=model
#         self.brand=brand
#     def start_engine(self):      #method to start the engine
#         print(f"{self.brand}{self.model} engine is running")
    

# #Creating instances 
# car1=Car("A4","Audi")
# car2=Car("Civic","Honda")
# print(car1.brand)
# car2.start_engine()



# class Dog:
#     species="sheperd"
#     def __init__(self,name,age):  #constructor to initilize the attributes
#         self.name=name
#         self.age=age


# #instances of the class dog
# dog1=Dog("Bella",5)
# dog2=Dog("Max",3)
# print(dog1.name)
# print(dog2.species)
# print(dog2.age)






# class Animal:      # parent class
#     def eat(self):
#         print("Animal eats...")

# class Husky(Animal):        # child class inheriting from parent class
#     def bark(self):
#         print("Husky barks...")
   
# dog=Husky()
# #Accessing the parent class method dog.eat()
# dog.eat()
# #Accessing the child class method
# dog.bark()




class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print(f"{self.name} inherit from parent (is eating...)")

class Dog(Animal):
    def eat(self):
        super().eat()
        print(f"{self.name} is eating dog food...")
d=Dog("siberian husky",5)
d.eat()  # Output: siberian husky is eating... siberian hus
