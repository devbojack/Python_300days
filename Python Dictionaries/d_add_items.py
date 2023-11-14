# _________________________________________________________ Python - Add Dictionary Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("Original dict:")
print(thisdict)

# Adding an item to the dictionary is done by using a new index key and assigning a value to it:
print("\n_____________________________________________________ Add Dictionary Items")
thisdict["color"] = "red"
print(thisdict)


# Update Dictionary
# The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.
# The argument must be a dictionary, or an iterable object with key:value pairs.
print("\n_____________________________________________________ Update Dictionary")
thisdict.update({"color": "blue"})
print(thisdict)



