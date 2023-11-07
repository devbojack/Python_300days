# Python - List Comprehension
# List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.


# The Syntax
# newlist = [expression for item in iterable if condition == True]


# Example:
# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
# Without list comprehension you will have to write a for statement with a conditional test inside:
print("_______________________________________WITHOUT LIST COMPREHENSION")
thislist = ["apple", "banana", "oranges", "melon", "cherry", "mango", "lemon"]
newlist = []

for x in thislist:
    if 'a' in x:
        newlist.append(x)
print(newlist)


print("_______________________________________WITH LIST COMPREHENSION")
fruits = ["Melon", "Cherry", "banana", "orange", "apple","kiwi"]
newlist = [x for x in fruits if 'a' in x]
print(newlist)

print("________________________________________WITHOUT IF CONDITION")
newlist = [x for x in fruits]
print(newlist)

print("_________________________________________ITERABLE")
# The iterable can be any iterable object, like a list, tuple, set etc.
newlist = [x for x in range(10)]
print(newlist)

print("_________________________________________ITERABLE WITH A CONDITION")
# Accept only numbers lower than 5:
newlist = [x for x in range(10) if x < 5]
print(newlist)


# _________________________________________________________Expression
print("_________________________________________Expression")
# The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:
fruits = ["Mango", 'apple', "kiwi", "lemon"]
newlist = [x.upper() for x in fruits]
print(newlist)

# Set all to 'hello'
newlist = ['hello' for x in fruits]
print(newlist)
print("")
# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome
print("Return orange instead of banana")
newlist = [x if x != 'apple' else 'orange' for x in fruits]
print(newlist)
