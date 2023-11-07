
#_____________________________________________________________________________________________________________INSERT ITEMS
print("#___________________________________________________________________________________________INSERT ITEMS")
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.
# The insert() method inserts an item at the specified index:
#_________________________________________________________
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
print("")
#_________________________________________________________

#_____________________________________________________________________________________________________________ADD LIST ITEMS
print("#__________________________________________________________________________________________ADD LIST ITEMS")
# To add an item to the end of the list, use the append() method:
#_________________________________________________________Append()
thislist = ["apple", "banana", "oranges"]
thislist.append("Berry")
print(thislist)
print("")
#_________________________________________________________Extend()
# To append elements from another list to the current list, use the extend() method
print("#__________________________________________________________________________________________EXTEND LIST ITEMS")
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
print("")
#__________________________________________________________Add Any Iterable
print("#__________________________________________________________________________________________EXTEND ANY ITETABLE")
#The extend() method does not have to append lists, you can add any iterable objects: tuples, sets, dictionaries, etc
thislist = ["apple", "banana", "cherry"]
thistuple = ["kiwi", "orange"]
thislist.extend(thistuple)
print(thislist)
print("")