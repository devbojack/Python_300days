# Copy Lists
# You cannot copy a list simply by typing list2 = list1, 
# because: list2 will only be a reference to list1, and 
# changes made in list1 will automatically also be made in list2.
# There are ways to make a copy, one way is to use the built-in List method copy().
print("_________________________Using Copy()")
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print("This List")
print(thislist)
print("My List")
print(mylist)

print("___________________________USING list()")
# Another way to make a copy is to use the built-in method list().
thislist = ["Mango", "Lemon", "cherry"]
print("thislist")
print(thislist)
mylist = list(thislist)
print("mylist")
print(mylist)

