# ______________________________________________________ Python - Remove Dictionary Items
thisdict = {
  "brand": "Porsche",
  "model": "Cayenne GTS",
  "year": 2023,
  "color": "black",
  "bought": True,
  "owner": "Bojack",
  "drives": True
}

print("Original dictionary:")
print(thisdict)

# _____________________________________________________ Using Pop()
# The pop() method removes the item with the specified key name:
print("\n_________________________________________________Remove using pop()")
thisdict.pop("model")
print(thisdict)

# _____________________________________________________ Using popitem()
# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
print("\n_________________________________________________Remove using popitem()")
thisdict.popitem()
print(thisdict)

# _____________________________________________________ Using clear()
# The clear() method empties the dictionary:
thisdict.clear()
print(thisdict)

# _____________________________________________________ del
# The del keyword removes the item with the specified key name:
print("\n_________________________________________________Remove using del")
del thisdict
print(thisdict) # This will cause an error because "thisdict" no longer exists












