# __________________________________________________________________Python - Loop Tuples
# You can loop through the tuple items by using a for loop.
thistuple = ("apple", "banana", "mango", "cherry")
for x in thistuple:
    print(x)

# ________________________________________________________________Loop Through the Index Numbers
# Use the range() and len() functions to create a suitable iterable.
print("_____________________________________________Loop Through the Index Numbers")
for i in range(len(thistuple)):
    print(thistuple[i])

# _________________________________________________________________Loop Using a While Loop
print("_____________________________________________Loop Using a While Loop")
# Use the len() function to determine the length of the tuple, then start at 
# 0 and loop your way through the tuple items by referring to their indexes.
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i += 1