# ________________________________________________________________________________ Python - Add Set Items
# Once a set is created, you cannot change its items, but you can add new items.
# To add one item to a set use the add() method.
print("____________________________________________________ Add items to set")
thisset = {"apple", "melon", "oranges", "banana"}
thisset.add("kiwi")
print(thisset)

# ________________________________________________________________ Add Sets
# To add items from another set into the current set, use the update() method.
print("____________________________________________________ Add Sets to sets")
thisset = {"apple", "mango","kiwi"}
newset = {"oranges", "cherry", "melon", "banana", "kiwi"}
thisset.update(newset)
print(thisset)

# ________________________________________________________________ Add Any Iterable
# The object in the update() method does not have to be a set, it can
# be any iterable object (tuples, lists, dictionaries etc.).
print("____________________________________________________ Add Any Iterable")
thisset = {"apple", "banana", "cherry", "kiwi"}
mylist = ["mango", "oranges", "kiwi"]
thisset.update(mylist)
print(thisset)

