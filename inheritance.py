# # # class Animal:
# # #     def eat(self):
# # #         print("All animals do eat")
        
# # # class Dog(Animal):
# # #     def Bark(self):
# # #         print("Dogs barking")

# # # obj=Dog()
# # # obj.Bark()    #own method 
# # # obj.eat()    #inherited method



# # class Animal:
# #     def eats(slef):
# #         print("root class , all animals do eat")
        
# # class Mammal(Animal):
# #     def brest_feeding(self):
# #         print("node class, all mammals do feeds to thier offsprings")
    
# # class Dog(Mammal):
# #     def bark(self):
# #         print("Leaf class, all dogs do barks")
        
# # obj=Dog()
# # obj.bark()  #own method
# # obj.brest_feeding()  #inherited from mammals class 
# # obj.eats()  #inherited from super class 


# # class Father:
# #     def skills(self):
# #         print("carpenter,Driver")
        
# # class Mother:
# #     def skills(self):
# #         print("chief,caring")
        
# # class Child(Father,Mother):
# #     def skills(self):
# #         Father.skills(self)
# #         Mother.skills(self)
# #         print("sports")
        

# # obj=Child()
# # obj.skills()




# class parent:
#     def show(self):
#         print("parent method")
        
# class child1(parent):
#     pass 

# class child2(parent):
#     pass 

# c1=child1()
# c2=child2()
# c1.show()



class Animal:
    def sound(self):
        print("some sound")
    
class Dog(Animal):
    def sound(self):
        print("barks")
        
obj_dog=Dog()
obj_dog.sound()