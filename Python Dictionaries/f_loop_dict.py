# ____________________________________________________________ Python - Loop Dictionaries
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

# You can loop through a dictionary by using a for loop.
# When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
print("\n_______________________________________________ loop using for; prints the key")
for x in thisdict:
    print(x)


print("\n_______________________________________________ print all values, one by one")
for x in thisdict:
    print(thisdict[x])

# ______________________________________________________________ Using values() method
# The values() method to return values of a dictionary
print("\n_______________________________________________ print all values using values() method")
for x in thisdict.values():
    print(x)

# ______________________________________________________________ Using keys() method
# You can use the keys() method to return the keys of a dictionary
print("\n_______________________________________________ print all keys using keys() method")
for x in thisdict.keys():
  print(x)

print("\n_______________________________________________ print all values using keys() method and []")
for x in thisdict.keys():
    print(thisdict[x])

# Loop through both keys and values, by using the items() method:
print("\n_______________________________________________ loop through both keys and values ")
for x, y in thisdict.items():
    print("{} : {}".format(x, y))
