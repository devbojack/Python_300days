# _______________________________________________Python - Access Dictionary Items
# You can access the items of a dictionary by referring to its key name, inside square brackets
print("\n______________________________________Using curly braces []")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["model"])

# ________________________________________________ Using get()
print("\n______________________________________Using the get() method")
print(thisdict.get("model"))


# Get Keys
# The keys() method will return a list of all the keys in the dictionary.

print("\n______________________________________Get all dict keys using key()")
print(thisdict.keys())
# OR
x = thisdict.keys()
for k in x:
    print(k)

# Get Values
# The values() method will return a list of all the values in the dictionary.
print("\n______________________________________Get all dict values using values()")
print(thisdict.values())
# OR 
x = thisdict.values()
for v in x:
    print(v)

# Get Items
# The items() method will return each item in a dictionary, as tuples in a list
print("\n______________________________________Get a list of the key:value pairs")
print(thisdict.items())
# OR 
x = thisdict.items()
for v in x:
    print(v)


# ______________________________________________ Changes to the get
# The returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list.
print("\n______________________________________Changes to items")
x = thisdict.items()
thisdict["year"] = 2023

print(x)


# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword:
print("\n______________________________________Check if key exists")
if "model" in thisdict:
    print("Model is one of the keys")