# ________________________________________________________________________Python - Unpack Tuples
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
# Extracting the values back into variables is called "unpacking"
# Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.

print("__________________________________________________________Python - Unpack Tuples")
fruits = ("apple", "banana", "cherry")
(item_one, item_two, item_three) = fruits
print(item_one)
print(item_two)
print(item_three)

# _______________________________Using Asterisk *
# If the number of variables is less than the number of values, you can add 
# an * to the variable name and the values will be assigned to the variable as a list:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(item_one, item_two, *item_rest) = fruits
print(item_one)
print(item_two)
print(item_rest)

#  NOTE: If the asterisk is added to another variable name than the last, 
# Python will assign values to the variable until the number of values
# left matches the number of variables left.
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(item_first, *item_rest, item_last) = fruits
print(item_first)
print(item_rest)
print(item_last)