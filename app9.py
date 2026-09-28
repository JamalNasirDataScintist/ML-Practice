class Mobile:
    def __init__(self, brand, model, price,storage):
        self.brand=brand
        self.model=model
        self.price=price
        self.storage=storage
    def mobile_info(self):
        print(f"the brand is {self.brand}")
        print(f"the model is {self.model}")
        print(f"the price is {self.price}")
        print(f"the storage is {self.storage}GB")
mob1=Mobile("Apple","Iphone-15",150000,256)
    
mob1.mobile_info()    
    
mob2=Mobile("samsung","s21",120000,128)
mob2.mobile_info()







class Bird:
    def fly(self):
        print("The bird is flying by flapping its wings")
class Airplane:
    def fly(self):
        print("The airplane is flying by using its engines")
    
class Drone:
    def fly(self):
        print("The drone is flying by using its rotors using thursts")
flying_objects=[Bird(),Airplane(),Drone()]
for obj in flying_objects:
    obj.fly()
    
    
def add(x,y,z=1):
    return x+y+z
print(add(5,6,30))

print(add(12,23))


print(3+5)
print("Hello" + "World")



