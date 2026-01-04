# Lists are used to store multiple items in a single variable.

fruits=["apple", "banana", "cherry"]
print(fruits)

# List items are ordered, changeable, and allow duplicate values.

# List Allow Duplicate Value
students=["Ak","Aj","Ak"]
print(students)

#A list with strings, integers and boolean values:
list1 = ["abc", 34, True, 40, "male"]

#Access List Items:
print(list1[0]) # Outputs 'abc'

#Negative Indexing
print(fruits[-2]) # Outputs 'banana'


#You can specify a range of indexes by specifying where to start and where to end the range.

fruit_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(fruit_list[2:5]) # Outputs ['cherry', 'orange', 'kiwi']

# Use "in" keyword to check if an item exists in the list
if "apple" in fruit_list:
      print("Yes,apple is present in the fruit list")
else:
      print("No,apple is not present in the fruit list")


# Change List Items 
#To change the value of a specific item, refer to the index number:
fruit_list[1]="strawberry"
print(fruit_list)

#You can also use a range of indexes to change the values of multiple items.
fruit_list[2:4]=["blackcurrant"]
print(fruit_list)

#To add an item to the end of the list, use the append() method:
phone_list = ["iPhone", "Samsung", "OnePlus"]
phone_list.append("Nokia")
print(phone_list)


# To insert a new list item, without replacing any of the existing values, we can use the insert() method
#The insert() method inserts an item at the specified index:
fruit_list.insert(2,"watermelon")

# Extend List
# To append elements from another list to the current list, use the extend() method.
export_fruits = ["mango", "papaya", "pineapple"]
tropical_fruits = ["banana", "kiwi", "orange"]
export_fruits.extend(tropical_fruits)
print(export_fruits)