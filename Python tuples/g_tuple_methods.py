# __________________________________________________________________Tuple Methods
# Python has two built-in methods that you can use on tuples.

# 1. count()	Returns the number of times a specified value occurs in a tuple
# 2. index()	Searches the tuple for a specified value and returns the position of where it was found

# ____________________________________________________________________Tuple count()
print("____________________________________________________________Tuple count()")
# Syntax
# tuple.count(value)
thistuple = (1,3,4,56, 33, 30,7,86,3)
# Return the number of times the value 5 appears in the tuple:
tuple3count = thistuple.count(3)
print("count of 3 is {}".format(tuple3count))


# ____________________________________________________________________Tuple index()
print("____________________________________________________________Tuple index()")
# Syntax
# tuple.index(value)
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
# Search for the first occurrence of the value 8, and return its position:
tuple8index = thistuple.index(8)
print("8 occurs at index {} in thistuple".format(tuple8index))