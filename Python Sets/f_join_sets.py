# _________________________________________________________ Python - Join Sets
# You can use:
#   union() method that returns a new set containing all items from both sets
#   update() method that inserts all the items from one set into another:
# Note: Both union() and update() will exclude any duplicate items.
# Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:
print("______________________________________________________ Join Sets using union()")
set1 = {"a", "b", "c"}
set2 = {1, 2, 3, 4}

set3 = set1.union(set2)
print("set1 {}".format(set1))
print("set2 {}".format(set2))
print("combined set1 and set2 {}".format(set3))


# ________________________________
print("______________________________________________________ Join Sets using update()")
set1 = {"z", "y", "w"}
set2 = {10, 21, 22, 3}
print("set1 {}".format(set1))
print("set2 {}".format(set2))

set1.update(set2)
print("combined set1 and set2 {}".format(set1))



# ___________________________________________________________Keep ONLY the Duplicates
# The intersection_update() method will keep only the items that are present in both sets.
# The intersection() method will return a new set, that only contains the items that are present in both sets.
print("\n______________________________________________________ Join duplicate Sets items using intersection_update() and intersection()")
# _____________________________________WITHOUT DUPLICATE
print("________________________________________NO DUPLICATE")
x = {"apple", "banana", "cherry"}
y = {"google", "tesla", "APPLE", "X"}

print("x {}".format(x))
print("y {}".format(y))

z = x.intersection(y)
x.intersection_update(y)

print("intersection update of x and y {}".format(z))
print("intersection of x and y {}".format(x))

# _____________________________________WITH DUPLICATE
print("\n________________________________________WITH DUPLICATE")
x = {"apple", "banana", "X", "TESLA", 1}
y = {"banana", "tesla", "apple", "X", True}

print("x {}".format(x))
print("y {}".format(y))

z = x.intersection(y)
x.intersection_update(y)

print("intersection update of x and y {}".format(x))
print("intersection of x and y {}".format(z))


# ___________________________________________________________Keep All, But NOT the Duplicates
# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
print("\n______________________________________________________ Join NOT duplicate Sets items using symmetric_difference_update() and symmetric_difference()")
# _____________________________________WITHOUT DUPLICATE
print("________________________________________NO DUPLICATE")
x = {"apple", "banana", "cherry"}
y = {"google", "tesla", "APPLE", "X"}

print("x {}".format(x))
print("y {}".format(y))

z = x.symmetric_difference(y)
x.symmetric_difference_update(y)

print("symmetric_difference_update of x and y {}".format(x))
print("symmetric_difference of x and y {}".format(z))
# _____________________________________WITH DUPLICATE
print("\n________________________________________WITH DUPLICATE")
x = {"apple", "banana", "X", "TESLA", True}
y = {"banana", "tesla", "apple", "X", 1}

print("x {}".format(x))
print("y {}".format(y))

z = x.symmetric_difference(y)
x.symmetric_difference_update(y)


print("symmetric_difference_update of x and y {}".format(x))
print("symmetric_difference of x and y {}".format(z))
