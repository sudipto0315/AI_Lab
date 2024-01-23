list=[1,2,3,4,5,6]
print (type(list))
for i in range(len(list)):
    print list[i],
print
for i in range(2,len(list)):
    print list[i],
print
# Inserting element 40 into the middle of the list
middle_index = len(list) // 2
list.insert(middle_index, 40)

# Appending element 100 to the end of the list
list.append(100)

# Printing the updated list
print("Updated List:", list)

# Print the 3rd, 4th and 5th element of the list.
print("the 3rd, 4th and 5th element are: ", list[2:6])