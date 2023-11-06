# ____________________________________________________ BOOLEANS
# __________________________________ NORMAL FLOW
# Booleans represent one of two values: True or False.
a = 200
b = 102

print(a > b)
print(a == b)
print(a < b)

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# The bool() function allows you to evaluate any value, and give you True or False in return,
print(bool("Hello"))
print(bool(15))
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.
#____________________________________
# If you have an object that is made from a class with a __len__ function that returns 0 or False:
# class my_class():
#     def __len__(self):
#         return 0

# myobj = my_class()
# print(bool(myobj))
#____________________________________
# FUNCTION CAN RETURN A BOOLEAN
# def my_func():
#     return True

# print(my_func())

# You can execute code based on the Boolean answer of a function:
# if my_func():
#     print("Yes")
# else:
#     print("No")

 #____________________________________
#Python also has many built-in functions that return a boolean value,
#       like the isinstance() function, which can be used to determine if an object is of a certain data type:
x = 200
print(isinstance(x, int))
