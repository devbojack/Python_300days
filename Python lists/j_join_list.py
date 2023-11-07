# JOIN Lists
# There are several ways to join, or concatenate, two or more lists in Python.
# One of the easiest ways are by using the + operator
print("________________________Using the + operator")
list1 = ["a", "b", "c", "d"]
list2 = [1, 2, 3, 5]
 
list3 = list1 + list2
print(list3)

# Another way to join two lists is by appending all the items from list2 into list1, one by one:
print("________________________Appending one by one")
list1 = ["d", "t", "c", "d"]
list2 = [1, 24, 3, 11]

for x in list2:
    list1.append(x)

print(list1)
 
# You can use the extend() method, where the purpose is to add elements from one list to another list:
print("_________________________Using extend() method")
list1 = ['e', 'z', 'q']
list2 = [90, 34, 2, 43]

list1.extend(list2)
print(list1)