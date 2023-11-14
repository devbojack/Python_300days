# Python Dictionaries

```
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
```
 <br>

Dictionaries are used to store data values in `key:value` pairs.<br>
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

Dictionaries are written with curly brackets {}, and have keys and values:

```
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
```

## Dictionary Items
Dictionary items are `ordered, changeable`, and `does not allow duplicates`. <br>
Dictionary items are presented in `key:value` pairs, and can be referred to by using the `key` name.

```
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
```
 <br>

## Ordered or Unordered?
**NOTE**: As of `Python version 3.7`, dictionaries are ordered. In `Python 3.6 and earlier`, dictionaries are unordered.

When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.<br>
Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.

 <br>

## Changeable
Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

 <br>

## Duplicates Not Allowed
Dictionaries cannot have two items with the same key: <br>
Duplicate values will overwrite existing values:

 <br>

## Dictionary Length
To determine how many items a dictionary has, use the len() function:

```
print(len(thisdict))
```

 <br>

## Dictionary Items - Data Types
The values in dictionary items can be of any data type:

```
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
```
 <br>

## type()
From Python's perspective, dictionaries are defined as objects with the data type 'dict':

> <class 'dict'>

```
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))
```
 <br>

## The dict() Constructor
It is also possible to use the `dict()` constructor to make a dictionary.

```
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
```










