# # class Car:
# #     def __init__(self, model, year):

# #         self.model = model  public attributes
# #         self.year = year
        
# # c=Car("Toyota", 2020)
# # print(c.model)  




# class Car:
#     def __init__(self):
#         self._speed=120   #protected attributes
        
#     def get_speed(self):
#         return self._speed
    
# c=Car()
# print(c.get_speed())



# class BankAccount:
#     def __init__(self,balance):
#         self.__balance = balance   #private attributes
        
#     def deposit(self, amount):
#         self.__balance += amount

#     def withdrwan(self, amount):
#         if amount <= self.__balance:
#             print("Withdrawing:", amount)
#         else:
#             print("Insufficient balance")
#             return
#         self.__balance -= amount
        
#     def get_balance(self):
#         return self.__balance

# acc=BankAccount(10000)
# acc.deposit(5000)
# acc.withdrwan(30000)
# print(acc.get_balance())

# from abc import ABC, abstractmethod


# class Animal(ABC):     #abstract class
#     @abstractmethod
    
#     def sound(self):
#         pass


# class Cat(Animal):
#     def sound(self):
#         return "Meow"
    
# class Dog(Animal):
#     def sound(self):
#         return "Bark"
    
# d=Dog()
# print(d.sound())
# c=Cat()
# print(c.sound())


from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass
class CreditCardPayment(Payment):
    def process_payment(self, amount):
        return f"Processing credit card payment of {amount}"
class PayPalPayment(Payment):
    def process_payment(self, amount):
        return f"Processing PayPal payment of {amount}"
c=CreditCardPayment()
print(c.process_payment(150))
    