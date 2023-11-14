# __________________________________________________________ Python - Change Dictionary Items

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("Original dict\n{}".format(thisdict))

# You can change the value of a specific item by referring to its key name:
print("\n_______________________________________________ CHANGE ITEMS")

thisdict["year"] = 2018
print(thisdict)

# Update Dictionary
# The update() method will update the dictionary with the items from the given argument.
# The argument must be a dictionary, or an iterable object with key:value pairs.
print("\n_______________________________________________Update dict")
thisdict.update({"year": 2020})
print(thisdict)