#_______________________________________________________________________________________ PYTHON LISTS
print("________________________________________________________________________________________ PYTHON LISTS")
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# Lists are used to store multiple items in a single variable
# Lists are created using square brackets:
# If you add new items to a list, the new items will be placed at the end of the list.
# The list is changeable: we can change, add, and remove items in a list after it has been created.
# lists can have items with the same value:
#_________________________________________________________
this_list = ["Apple", "Banana", "Man", "Man", "Lemon"]
print(this_list)
#_________________________________________________________
# To determine how many items a list has, use the len() function:
#_________________________________________________________
print(len(this_list))
#_________________________________________________________
# List items can be of any data type: String, integers, booleans
# A list can contain different data types:
# From Python's perspective, lists are defined as objects with the data type 'list':
# <class 'list'>
#_________________________________________________________
print(type(this_list))
#_________________________________________________________
# It is also possible to use the list() constructor when creating a new list.
#_________________________________________________________
new_list = list(("Apple", "Lemon", "Orange"))
print(new_list)
#_________________________________________________________
