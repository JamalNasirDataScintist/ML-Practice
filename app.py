# def greet(name="Muhammad"):    #defining a func and name is a parameter 
#     print(f"Hello {name}")
# greet("Ahmed")        #function calling and arguments

# greet()


# def student(name,age):
#     print(f"name is:{name},\n age is:{age}")
# student("sam",20)




# def show_details(**info):
#     print(info)
# show_details(name="Sunny",Age=30,city="RWP")   




# def square(x):
#     return x*x
# print(square(8))



# def add_sub(a,b):
#   return a+b,a-b
# add,sub=add_sub(18,10)
# print(add,sub)





#lambda function

squares=lambda z: z*z
print(squares(9))








# def is_number_pallendrome(n):
#     return str(n)==str(n)[::-1] 
# print(is_number_pallendrome(1221)) 
# print(is_number_pallendrome("ma'am")) 





def even_number(n):
    if n%2==0:
     return True
    else:
       return False
print(even_number(13))
    