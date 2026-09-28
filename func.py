print("Hello")

print(len([1,2,3]))
print(sum([3,5,6,7]))

#built in functions 

#now lets start with user defined function

def greet(name):   #function def
    print(f"hello{name}")   # function body 
greet("Ali")   #function calling 
     
     
greet("Sam")
greet("Sunny")  #Just to make the reuseability of code easier 

def addition(x,y,z):  # parameters
    print("the sum value is",x+y+z)

addition(12,34,56) #arguments


def greets(name="Guest"):    #default parameters 
    print(f"Hello {name}")
greets()


def student(name,age):
    print(f"name is {name} and {age} years old")
student(name="Rehman",age=45)   #keyword arguments



def add(*numbers):
    print(sum(numbers))
add(1,2,34,4)

def student_details(**info):
    print(info)
student_details(name="Sami",age=24,address="ISB",marks=90)


def pallindrome(n):
    return str(n)==str(n)[::-1]

print(pallindrome("CIVIC"))
print(pallindrome("madam"))

print(pallindrome("mom"))
print(pallindrome("level"))
print(pallindrome("12321"))
