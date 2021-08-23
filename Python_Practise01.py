# #.format method 
# print("The {q} {b} {f}".format(f="fox", q="quick", b="brown"))

# # Using the .format method to show 4 places past the floating point 1 is the white space always keep at one
# result = 100/777
# print("The result was {r:1.4f}".format(r = result))
# print(f"The result was {result:1.4f}")

#List Section Start
my_list = [1,2,3]
print(len(my_list))

my_list = ["one", "Two", "Three"]
print(my_list[0])

another_list = ["four", "five", "six"]

new_list = my_list + another_list

print(new_list)

new_list[0] = "Null"



other_list = new_list.pop(3)
print(other_list)