# my_dictionary={"name":"Ali", "age":25, "city":"RWp"}
# print(my_dictionary)
# print(type(my_dictionary))
# my_dictionary["city"]="London"
# print(my_dictionary)
# my_dictionary["age"]=35
# print(my_dictionary)

# print(my_dictionary.get('city'))

# print(my_di(101)ctionary.keys())
# print(my_dictionary.values())

# print(my_dictionary.items())

# print(my_dictionary.pop('age'))

# print(my_dictionary.items())


# my_dictionary.update({"city":"paris"})
# print(my_dictionary)
# \





my_set={1,23,4,5,6,7,8,9,11,1,3,4,5}
print(my_set)
my_set.add(100)
print(my_set)
my_set.add(100)
print(my_set)

my_set.remove(100)
print(my_set)
my_set.discard(101)
print(my_set)

set_1={1,20,30,4,50,6,7,8,9,10}
set_2={20,30,40,50,60,70}

resultant_set=set_1.union(set_2)
print(resultant_set)

intersection_result=set_1.intersection(set_2)
print(intersection_result)





#file Handling in python 
#open a file and write
file=open("dummy.txt","w")

file.write("Hello it is a dummy file")
#after writing i want to close the file 
file.close()

#open same file in reading mode
file=open("dummy.txt","r")

content=file.read()
print("File content")
print(content)

#now to close the file 
file.close()


