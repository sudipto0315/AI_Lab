def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b


a = 10
b = 5
print("Before: ", a, b)
# code to swap 'a' and 'b' without using a temp variable
a = a + b  # a now becomes 15
b = a - b  # b becomes 10
a = a - b  # a becomes 5
print("After: ", a, b)
# with temp variable
a, b = swap(a, b)
print("After using swap func with temp variable: ", a, b)