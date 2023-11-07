# _____________________________________________________________________________SORT LIST
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
print("________________Alpabetically")
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
print(thislist)
thislist.sort()
print(thislist)
print("")
print("________________Numerically")
thislist = [100, 50, 65, 82, 23]
print(thislist)
thislist.sort()
print(thislist)


# ___________ SORT DESCENDING
print("________________Alpabetically DESC")
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
print("")

print("________________Numerically DESC")
thislist = [100, 50, 65, 82, 23]
print(thislist)
thislist.sort(reverse=True)
print(thislist)
print("")

# ___________ CUSTOMIZE SORT FUNCTION
# You can also customize your own function by using the keyword argument key = function.
# The function will return a number that will be used to sort the list (the lowest number first):
print("________________Sort the list based on how close the number is to 50:")
def myfunc(n):
    return abs(n - 70)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# ____________Case Insensitive Sort
print("____________Case sensitive Sort")
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

print("____________Case Insensitive Sort")
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# _____________Reverse Order
print("_______________Reverse Order")
# Reverse the order of a list, regardless of the alphabet?
# The reverse() method reverses the current sorting order of the elements.
thislist = ["banana", "Orange", "Kiwi", "cherry"]
print("Before reverse")
print(thislist)
thislist.reverse()
print("After reverse")
print(thislist)
