#_________________________________________________________________________________________CHANGE LIST ITEMS
print("________________________________________________________________________________________CHANGE LIST ITEMS")
# To change the value of a specific item, refer to the index number:
#_________________________________________________________
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#_________________________________________________________
# Change a Range of Item Values
# To change the value of items within a specific range, define a list with the new values,
# and refer to the range of index numbers where you want to insert the new values:
# The example changes the values "banana" and "cherry" with the values "blackcurrant" and "watermelon"
#_________________________________________________________
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
#_________________________________________________________
thislist = ["apple", "banana", "cherry"]
thislist[0:1] = ["blackcurrant", "watermelon"]
print(thislist)
#_________________________________________________________
# If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
#_________________________________________________________
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
#_________________________________________________________
