# # class Animal:
# #     def sound(self):
# #         print("Animals make sounds")
# # class Dog(Animal):
# #     def sound(self):
# #         print("Dog barks")

# # class Cat(Animal):
# #     def sound(self):
# #         print("Cat meows")

# # animals=[Dog(),Cat()]

# # for animal in animals:
# #     animal.sound()
    
    
    
    
# # #two class father and mother 

# # #one child class inheriting from both father and mother class    


# # #represent attributes and methods of both father and mother class in child class  (at least two method) 

# # #Matplotlib   (Data Voisualization)

# # class Mobile:
# #    def __init__(self,brand,model,price,storage,camera):
# #     self.brand=brand
# #     self.model=model
# #     self.price=price
# #     self.storage=storage
# #     self.camera=camera
# #    def mobile_info(self):
# #        print(f"the brand is:{self.brand},the model is: {self.model},the price is :{self.price}, the storage is :{self.storage},the camera is: {self.camera} ")
       
# # mob1=Mobile("Apple","iphone-15",150000,256,"16mp")
# # mob1.mobile_info()
# # mob2=Mobile("Samsung","S24",140000,"1TB","100mp")
# # mob2.mobile_info()



# #first example of polymorphism thorugh operator

# print(3+5)
# print("Hello" + "World")

# #second thorough functions
# def add(a,b,c=1):
#     return a+b+c
# print(add(3,5))
# print(add(74,15,7))  #96


# class Bird:
#     def fly(self):
#         print("Bird is flying by flapping its wings")
        
# class Airplane:
#     def fly(self):
#         print("Airplane is flying by using its wings and engines")

# class Drone:
#     def fly(self):
#         print("Drone is flying by using its propellers")
        
        
# flying_objects=[Bird(),Airplane(),Drone()]

# for obj in flying_objects:
#     obj.fly()
    
    
    
    
# #third example of polymorphism through inheritance 
# class Animal:
#     def speak(self):
#         return "Animal is speaking"

# class Dog(Animal):
#     def speak(self):
#         return "Dog is barking"
    
# obj1=Animal()
# print(obj1.speak())
# obj2=Dog()
# print(obj2.speak())  #Dog is barking





class Animal:
    def sound(self):
        print("Animals make sounds")
    
class Dog(Animal):
    def sound(self):
        print("Dog barks")
        
class Cat(Animal):
    def sound(self):
        print("Cat meows")
        
animals={Dog(),Cat()}
for obj in animals:
    obj.sound()