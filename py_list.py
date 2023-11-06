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


#___________________________________________________________________________________ACCESS LIST ITEMS
print("#___________________________________________________________________________________ACCESS LIST ITEMS")
#List items are indexed and you can access them by referring to the index number:
#_________________________________________________________
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[1])
#_________________________________________________________
# Negative indexing means start from the end
# -1 refers to the last item, -2 refers to the second last item etc.
#_________________________________________________________
print(thislist[-1])
#_________________________________________________________
# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with the specified items.
# 1 example will return the third, fourth, and fifth item:
# 2nd example returns the items from the beginning to, but NOT including, "kiwi":
# 3rd example returns the items from "cherry" to the end:
#_________________________________________________________
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
#_________________________________________________________
# Range of Negative Indexes
# Specify negative indexes if you want to start the search from the end of the list:
# This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
#_________________________________________________________
print(thislist[-4:-1])
#_________________________________________________________
# Check if Item Exists
# To determine if a specified item is present in a list use the in keyword:
#_________________________________________________________
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


#_________________________________________________________________________________________CHANGE LIST ITEMS
print("________________________________________________________________________________________CHANGE LIST ITEMS")
# To change the value of a specific item, refer to the index number:
#_________________________________________________________
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#_________________________________________________________
# Change a Range of Item Values
# To change the value of items within a specific range, define a list with the new values,
# and refer to the range of index numbers where you want to insert the new values:
# The example changes the values "banana" and "cherry" with the values "blackcurrant" and "watermelon"
#_________________________________________________________
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
#_________________________________________________________
thislist = ["apple", "banana", "cherry"]
thislist[0:1] = ["blackcurrant", "watermelon"]
print(thislist)
#_________________________________________________________
# If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
#_________________________________________________________
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
#_________________________________________________________


#_____________________________________________________________________________________________________________INSERT ITEMS
print("#_____________________________________________________________________________________________________________INSERT ITEMS")
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.
# The insert() method inserts an item at the specified index:
#_________________________________________________________
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
#_________________________________________________________

#_____________________________________________________________________________________________________________ADD LIST ITEMS
print("#_____________________________________________________________________________________________________________ADD LIST ITEMS")
# To add an item to the end of the list, use the append() method:

