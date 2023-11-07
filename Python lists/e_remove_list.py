# Python - Remove List Items
# Remove specifies items
# Use remove()
# If there are more than one item with the specified value, the remove() method removes the first occurance:
print("______________________________________________________________________REMOVE LIST ITEMS")
thislist = ["apple", "banana", "cherry", "banana"]
print(thislist)
print("Remove banana")
thislist.remove("banana")
print(thislist)
print("")
#______________________________________________________________________REMOVE SPECIFIED INDEX
print("______________________________________________________________________REMOVE SPECIFIED INDEX USING POP")
# The pop() method removes the specified index.
# If you do not specify the index, the pop() method removes the last item.
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.pop(1)
print("Pop index 1")
print(thislist)
print("")
print("______________________________________________________________________REMOVE SPECIFIED INDEX USING DEL")
# The del keyword also removes the specified index:
# The del keyword can also delete the list completely.
thislist = ["Mango", "Oranges", "Melon"]
print(thislist)
del thislist[0]
print("DEL index 0")
print(thislist)
# delete list completely
del thislist
print("")

#______________________________________________________________________CLEAR THE LIST
print("______________________________________________________________________CLEAR THE LIST")
# The clear() method empties the list.
# The list still remains, but it has no content.
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.clear()
print("Clear the list")
print(thislist)