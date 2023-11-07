# Loop Through a List
# You can loop through the list items by using a for loop:
print("_____________________________________________________LOOP THROUGH A LIST USING FOR")
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

print("_____________________________________________________LOOP THROUGH A LIST THROUGH THE INDEX NUMBERS")
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

print("_____________________________________________________LOOP THROUGH A LIST USING A WHILE LOOP")
thislist = ["Apple", "Mango", "Cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

print("_____________________________________________________Looping Using List Comprehensio")
# Looping Using List Comprehension
# List Comprehension offers the shortest syntax for looping through lists
thislist = ["BMW", "Toyota", "Mercedes", "Volvo"]
[print(x) for x in thislist]
