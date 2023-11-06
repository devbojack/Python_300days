# Start from below the list

# ________________________________________________________ ESCAPE CHARACTERS
# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.

# ________________________________________________________ STRING FORMAT
# We can combine strings and numbers by using the format() method!
# age = 29
# gold = 30000
# happiness = 100
# txt = "My name is Bojack, and I am {}"
# myOrder = "I want {} pieces of gold and {}% pieces of happiness"
# print(txt.format(age))
# print(myOrder.format(gold, happiness))
# # You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
# newOrder = "I want {1} pieces of gold and {0}% pieces of happiness"
# print(newOrder.format(happiness, gold))

# ________________________________________________________ STRING CONCATENATION
# a = "Hello"
# b = "World"
# c = a + " " + b
# print (c)

#_______________________________________MODIFY STRINGS
# # The upper() method returns the string in upper case:
# a = "Hello, World!"
# print(a.upper())
# # The lower() method returns the string in lower case:
# print(a.lower())
# # The strip() method removes any whitespace from the beginning or the end:
# a = "  Hello, World!"
# print(a.strip())
# # The replace() method replaces a string with another string:
# print(a.replace("H", "J"))
# # The split() method returns a list where the text between the specified separator becomes the list items.
# print(a.split(","))

#________________________________________PYTHON - SLICING STRINGS
#You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.
# b = "Hello World"
# print(b[2:8:])
# Start from the start or index 0
# print(b[:5])
# Slice To the End
# print(b[5:])

# Negative Indexing
# Use negative indexes to start the slice from the end of the string:
# print(b[-5:-2])

# ________________________________String Length - Use len()
# a = "Hello World"
# print(len(a))
# ____________Check string
# _______using in
# txt = "Plan and prioritize"
# print("Plan" in txt)
# print("PLAN" in txt)
# print("free" in txt)
#________________
# if "Plan" in txt:
    # print("Yes, plan plan")
# else:
    # print("Add plan")
# _______using NOT
# print("Plan" not in txt)

# if "Flan" not in txt:
    # print("Add plan manze")
#_____________________________
#__________________________________STRINGS ARE ARRAYS
# a = "Hello World"
# print(a[0])
# for x in a:
#     print(x)
# _________________________________MULTILINE STRING
# _______Use triple double or single quotes
# _______The line breaks and the spaces are reserved as they are.
# __________
# x = """This is awesome,
# this is wonderful,
# this is the best."""
# print(x)
# ____________