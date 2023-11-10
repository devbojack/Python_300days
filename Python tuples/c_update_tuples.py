#________________________________________________________________PYTHON UPDATE TUPLES
# Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created
#________________________________________________________________Change Tuple Values
# You can convert the tuple into a list, change the list, and convert the list back into a tuple.
print("________________________________________________________________PYTHON UPDATE TUPLES")
x = ("apple", "banana", "cherry")
print("Original tuple: {} ".format(x))
# Convert to list
y = list(x)
# Update list
y[1] = "kiwi"
x = tuple(y)
print("Update tuple: {} ".format(x))

#________________________________________________________________PYTHON APPEND TUPLES
# ___________________________________________Method 1 - Convert into a list
print("________________________________________________________________PYTHON APPEND TUPLES: Convert into a list")
thistuple = ("mango", "melon", "pawpaw")
print("Original tuple: {} ".format(thistuple))
# Convert to list
y = list(thistuple)
# Append item
y.append("orange")
thistuple = tuple(y)
print("Appended tuple: {} ".format(thistuple))

# ___________________________________________Method 2 - Add tuple to a tuple
#       You are allowed to add tuples to tuples, so if you want to add one item, 
#       (or many), create a new tuple with the item(s), and add it to the existing tuple:
print("________________________________________________________________PYTHON APPEND TUPLES: Add tuple to a tuple")
thistuple = ("melon", "mango", "cherry")
print("Original tuple: {} ".format(thistuple))
# NOTE: Add the comma after the item if the tuple contains only one item
newtuple = ("apple",)
# Add tupple to tupple
thistuple += newtuple
print("Appended tuple: {} ".format(thistuple))

#________________________________________________________________PYTHON REMOVE ITEMS IN A TUPLE
# Convert the tuple into a list, remove "apple", and convert it back into a tuple:

print("#________________________________________________________________PYTHON REMOVE ITEMS IN A TUPLE")
thistuple = ("mango", "melon", "oranges", "apples")
print("Original tuple: {} ".format(thistuple))
# Convert to tupple to list
thislist = list(thistuple)
# Remove item
thislist.remove("apples")
# Convert list to tupple
thistuple = tuple(thislist)
print("Updated tuple after removing 'apple': {}".format(thistuple))

#________________________________________________________________PYTHON DELETE TUPPLE COMPLETELY 
# The del keyword can delete the tuple completely:
print("________________________________________________________________PYTHON DELETE TUPPLE COMPLETELY ")
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists
