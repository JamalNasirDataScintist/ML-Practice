# # # cars=["Bm","audi","mercedez"]
# # # colors=["white","silver","black"]

# # # print(cars)
# # # print(colors)



# # # for car in cars:
# # #     for color in colors:
# # #         print(f"{car},{color}")




# # # for i in range(1,7):
# # #     for j in range(1,7):
# # #         print(f"{i}x{j}={i*j:2}",end=" ")
# # #     print()

# # for x in range(5):
# #     if x==3:
# #       continue
# #     print(x)


# name=''
# while name!='Ali':
#     print('Please type your name')
#     name=input()
#     print("Thank you!")


# i=1
# while i<=5:
#     print(i)
#     i+=1



my_list=[1,2,3,4,"apple","cherry",True]

print(my_list)
print(type(my_list))
print(my_list[5])
my_list[6]="banana"
print(my_list)

my_list.append('mango')
print(my_list)



my_tuple=(1,2,2,3,4,"kiwi","kiwi","grapes","false")
print(type(my_tuple))

print(my_tuple.count("kiwi"))
print(my_tuple)