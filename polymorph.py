# class Bird:
#     def fly(self):
#         print("birds fly by flapping thier wings")
# class Drone:
#     def fly(self):
#         print("Drones Using motore thursts and roter")

# class Airplane:
#     def fly(self):
#         print("Airplanes using runway and engine thursts")
        
# #list of flying objects

# flying_objects=[Bird(),Drone(),Airplane()]

# #polymorphic loop

# for obj in flying_objects:
#     obj.fly()
    
    
    
# class Animal:
#     def speak(self):
#         return "some sound"
    
# class Bird(Animal):
#     def speak(self):
#         return "chirps"
# obj1=Animal()
# obj=Bird()

# print(obj1.speak())
# print(obj.speak())





# class Animal:
#     def speak(self):
#         print("aNIMAL MAKE SOME SOUNDS")
        

# class Cat(Animal):
#     def speak(self):
#         print("Cat meaows")
        
# class Dog(Animal):
#     def speak(self):
#         print("Dogs  barks")
        
# speaking_animals=[Animal(),Cat(),Dog()]

# for obj in speaking_animals:
#     obj.speak()
    
    
    
    
    
class public:
    def __init__(self):
        self.name='john'       # public attributes 
    def display_name(self):
        print(self.name)       #inside the class access 

obj=public()
obj.display_name()
print(obj.name)    #outiside the class access 



class protected:
    def __init__(self):
        self._age=30

class subclass(protected):
    def display_age(self):
        print(self._age)    #accessing age info in sub class 

ob=subclass()
ob.display_age()

class private:
    def __init__(self):
        self.__salary=60000    #private attribute
        
    def salary(self):
        return self.__salary   #using public method to access private attributes
    
pri=private()
print(pri.salary())


class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return point(self.x+other.x,self.y+other.y)
p1=point(2,3)
p2=point(4,1)
p3=p1+p2

print(p3.x,p3.y)