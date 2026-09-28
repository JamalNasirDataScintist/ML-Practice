my_list=[1,2,3,4,54,56,7,"Apple","mango",34.00,True]
#        0 1 2 3 4   5 6   7       8      9     10
print(my_list)
print(my_list[8])
my_list[9]="Banana"
my_list[10]="pineapple"
print(my_list)

my_list.append("cherry")     # to add something at the end of the list 
print(my_list)

my_list.insert(7,"Avocado")  #a method to add something at a specific location 
print(my_list)

new_list=["jam","Milk","butter",120,340,560,"butter"]

print(new_list)
new_list.remove("butter")  # discard the first matching item from the list

print(new_list)

new_list.pop()    #remove an item from the end of the list 
print(new_list)


num_list=[1,256,63,4233,555,6768,9,753,4,23,2321,334,5,56]

print(num_list)

num_list.sort()
print(num_list)
num_list.reverse()
print(num_list)



my_tuple=(1,2,3,4,5,"Banana","apple","cherry","apple","mango","apple","apple","apple")

print(my_tuple)

print(my_tuple[6])

print(my_tuple.count("apple"))

print(my_tuple.index('apple'))


new_tuple=(1,2,3,12,13,15,67,75,98,4,3,2)
print(new_tuple)




my_dictionary={"name":"Ali","age":26,"city":"ISB"}
print(my_dictionary)

my_dictionary["age"]=30
print(my_dictionary)

print(my_dictionary.get('age'))  #return a value for a specific key

print(my_dictionary.keys())     #return all the keys

print(my_dictionary.values())   #return all the values 

print(my_dictionary.items())   #return key-vlaues pair 
my_dictionary.update({"city":"London"})  #update the vlaues 
print(my_dictionary)

my_dictionary.pop('age')
print(my_dictionary)