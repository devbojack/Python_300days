# __________________________________________________________________________ Python Sets
# A set is a collection which is unordered, unchangeable*, and unindexed.
# Unordered means that the items in a set do not have a defined order.
        # Set items can appear in a different order every time you use
        # them, and cannot be referred to by index or key.
# Unchangeable, meaning that we cannot change the items after the set has been created.
# Sets cannot have two items with the same value.
# Set items are: unchangeable, but you can remove items and add new items.
# Sets are written with curly brackets.
# A set can contain different data types:

print("______________________________________________________ Sets")
myset = {"apple", "banana", "cherry"}
print(myset)

# ___________________________________________________________________________ True and 1
# The values True and 1 are considered the same value in sets, and are treated as duplicates:
print("______________________________________________________ True and 1")
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

# ___________________________________________________________________________ False and 0
# The values False and 0 are considered the same value in sets, and are treated as duplicates:
print("______________________________________________________ False and 0")
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

# ___________________________________________________________________________ Length of a Set
# To determine how many items a set has, use the len() function.
print("______________________________________________________ Length of a Set")
thisset = {"mango", "banana", "oranges", "melon", "banana", "apple"}
print(thisset)
print(len(thisset))

# ____________________________________________________________________________ type()
# From Python's perspective, sets are defined as objects with the data type 'set':
print("______________________________________________________ Set type()")
myset = {"apple", "banana", "cherry"}
print(type(myset))

# ____________________________________________________________________________ set() Constructor
# It is also possible to use the set() constructor to make a set.
print("______________________________________________________ set()")
thisset = set(("apple", "banana", "cherry", "melon"))
print(thisset)


