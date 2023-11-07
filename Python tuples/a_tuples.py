# ________________________Tuple
# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.
# Tuple items are ordered, unchangeable, and allow duplicate values.
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple
# Tuple items can be of any data type: A tuple can contain different data types
mytuple = ("apple", "bacon", "cain", "cherry", "banana")
print(mytuple)

print("________________Tuple length")
print(len(mytuple))


print("________________Tuple with 1 item")
onetuple = ("apple",)
print(onetuple)

print("________________Tuple with different types")
diftuple = ("apple", True, 42, 2.22, "male")
print(diftuple)


# _____________________________________type()
print("_____________________________________type()")
# From Python's perspective, tuples are defined as objects with the data type 'tuple':
# <class 'tuple'>
diftuple = ("apple", True, 42, 2.22, "male")
print(type(diftuple))
# _____________________________________the tuple constructor
print("_____________________________________Creating a tuple using the tuple constructor")
# Its  possible to use the tuple() constructor to make a tuple
thistuple = tuple("mango", "bacon", True, 2)
print(thistuple)