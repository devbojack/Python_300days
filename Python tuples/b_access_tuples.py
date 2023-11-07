# __________________________________ ACCESS TUPLE ITEMS
# You can access tuple items by referring to the index number, inside square brackets
# Negative indexing means start from the end.
print("________________________________ Accessing using Indexes")
thistuple = ("apple", "cherry", "mango", True)
print(thistuple[3])

print("________________________________ Negative Indexing")
print(thistuple[-2])

print("________________________________ Range of indexes")
print(thistuple[1:3])


# By leaving out the start value, the range will start at the first item:
print("________________________________Range of indexes leaving the first start value")
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])


# By leaving out the end value, the range will go on to the end of the list:
print("________________________________Range of indexes leaving the end value")
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])


# Range of Negative Indexes
print("________________________________Range of Negative Indexes")
# Specify negative indexes if you want to start the search from the end of the tuple:
# This example below returns the items from index -4 (included) to index -1 (excluded)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

# Check if Item Exists
print("________________________________ Check if Item Exists")
# To determine if a specified item is present in a tuple use the in keyword:
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")