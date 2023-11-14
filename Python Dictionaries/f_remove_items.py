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
print("\n_______________________________________________ loop using for")
for x in thisdict:
    print(x)



