#public memebers

class Public:
    def __init__(self):
        self.name="john"   #public attribute
    def display_name(self):
        print(self.name)  #public method\
obj=Public()
obj.display_name()
print(obj.name)





class protected :
    def __init__(self):
        self._age=30  #protected members 
        
class Subclass(protected):
    def display_age(self):
        print(self._age)  #accessing protected members in subclass
obj=Subclass()
obj.display_age()
print(obj._age)


class private :
    def __init__(self):
        self.__salary=50000   #private members
    def display_salary(self):
         return self.__salary   #accessing thorough public methods
obj=private()
print(obj.display_salary()) #access
print(obj.__salary)
