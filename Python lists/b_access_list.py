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