# my_dictionary={"name":"Alice","age":30,"city":"islamabad", "grades":"A"
# }

# print(my_dictionary)

# my_dictionary["city"]="London"
# print(my_dictionary)

# print(my_dictionary.get("grades"))

# print(my_dictionary.keys())
# print(my_dictionary.values())


# print(my_dictionary.items())

# my_dictionary.update({"city":"paris"})
# print(my_dictionary)

# my_dictionary.pop("grades")
# print(my_dictionary)



# my_set={1,23,45,5,6,67,8,9,5,5,10}
# print(my_set)
# my_set.add(100)
# print(my_set)

# my_set.add(100)
# print(my_set)

# my_set.remove(45)
# print(my_set)
# my_set.discard(23)
# print(my_set)

# my_set.clear()
# print(my_set)


# set_1={12,2,3,3,6,7,8,9}
# set_2={10,20,30,405,60,12,13,14,2,3,4,5}
# print(set_1,set_2)

# Resultant_set=set_1.union(set_2)
# print(Resultant_set)

# intersection_result=set_1.intersection(set_2)
# print(intersection_result)



#Create and open a new file 
file=open("filehandling.txt","w")
file.write("This is my file i have writtern in python")
file.close()

#now open file to read
file=open("filehandling.txt","r")
content=file.read()
print(content)

#now to close the file 
file.close()          