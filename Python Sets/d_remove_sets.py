# ____________________________________________________________________ Python - Remove Set Items
# To remove an item in a set, use the remove(), or the discard() method.

# __________________________________________________ remove()
# Note: If the item to remove does not exist, remove() will raise an error.
print("__________________________________________________ remove()")
thisset = {"apple", "banana", "cherry"}
print("Before remove() : {}".format(thisset))
thisset.remove("banana")
print("After remove() : {}".format(thisset))


# __________________________________________________ discard()
# If the item to remove does not exist, discard() will NOT raise an error.
print("__________________________________________________ discard()")
thisset = {"mango", "apple", "banana", "cherry", "kiwi"}
print("Before discard() : {}".format(thisset))
thisset.discard("banana")
print("After discard() : {}".format(thisset))

# __________________________________________________ pop()
# You can also use the pop() method to remove an item, but this method 
        # will remove a random item, so you cannot be sure what item that
        # gets removed.
# The return value of the pop() method is the removed item.
print("__________________________________________________ pop()")
thisset == {"apple", "cherry", "kiwi", "mango"}
print("Before pop() : {}".format(thisset))
removed_item = thisset.pop()
print("Poped item: {}".format(removed_item))
print("After pop() : {}".format(thisset))

# __________________________________________________ clear()
# The clear() method empties the set
print("__________________________________________________ clear()")
thisset = {"apple", "banana", "cherry",  "kiwi", "mango"}
print("Before clear() : {}".format(thisset))
thisset.clear()
print("After clear() : {}".format(thisset))


# __________________________________________________ del()
# The del() will delete the set completely
thisset = {"apple", "banana", "cherry",  "kiwi", "mango"}
print("Before del() : {}".format(thisset))
del thisset
print("After del() : {}".format(thisset)) # Returns an error as the set is completelty deleted and no longer exists