#Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# Create and print a dictionary:
thisdict={
      "name":"Akash",
      "age":24,
      "department":"CSE",
      "ID":101
}
print(thisdict)

#Accressing Items
print(thisdict["name"])  # Accessing via key
print(thisdict.get("age"))  # Accessing via get() method

#The values in dictionary items can be of any data type:
thisdict2={
      "name":"John",
      "age":30,
      "isStudent":False,
      "marks":[85,90,88],
      "address":{"city":"New York","zip":"10001"}
}
print(thisdict2)


#It is also possible to use the dict() constructor to make a dictionary.
thisdict3=dict(name="Alice",age=28,department="ECE",ID=102)
print(thisdict3)

# Change Values:
#----------------------
thisdict3["age"]=29
print("Dictionary after changing age:",thisdict3)

#The update() method will update the dictionary with the items from the given argument
thisdict3.update({"department":"EEE"})
print("Dictionary after updating department:",thisdict3)



# Adding Items:
#----------------------
thisdict3["email"]="ashikur@gmail.com"
print("Dictionary after adding email:",thisdict3)
#The update() method can also be used to add items to a dictionary.
thisdict3.update({"phone":"123-456-7890"})
print("Dictionary after adding phone:",thisdict3)



#Removing Items:
#----------------------
#The pop() method removes the item with the specified key name:
thisdict3.pop("ID")
print("Dictionary after popping ID:",thisdict3)

#The popitem() method removes the last inserted item:
thisdict3.popitem()
print("Dictionary after popping last item:",thisdict3)


#The del keyword removes the item with the specified key name:
del thisdict3["email"]
print("Dictionary after deleting email:",thisdict3)

#The clear() method empties the dictionary:
thisdict3.clear()
print("Dictionary after clearing all items:",thisdict3)
#The del keyword can also delete the dictionary completely:
del thisdict3
# print(thisdict3)  # This will raise an error because the dictionary no longer exists.


#Loops:
#-----------------------
#You can loop through a dictionary by using a for loop.
thisdict4={
      "name":"Emma",
      "age":27,
      "department":"ME",
      "ID":103
}

#Print all key names in the dictionary, one by one:
for x in thisdict4:
      print(x)

#Print all values in the dictionary, one by one:
for x in thisdict4:
      print(thisdict4[x])

#You can also use the values() method to return values of a dictionary:
for x in thisdict4.values():
      print(x)
#You can use the keys() method to return the keys of a dictionary:
for x in thisdict4.keys():
      print(x)

#********************************#
#You can use the items() method to return each item in a dictionary, as a tuple:

for x,y in thisdict4.items():
      print(x,":",y)



#Make a copy of a dictionary with the copy() method:

thisdict5=thisdict4.copy()
print("Copied Dictionary:",thisdict5)

#You can also use the dict() function to make a copy of a dictionary.
thisdict6=dict(thisdict4)
print("Copied Dictionary using dict():",thisdict6)

