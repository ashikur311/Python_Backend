#Tuples are used to store multiple items in a single variable.
#Tuples are ordered and unchangeable. Tuples allow duplicate values.
#Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
#Tuples are written with round brackets.
#Create a Tuple:

fruits=("apple", "banana", "cherry","apple","cherry","orange","kiwi","mango","papaya")
print(fruits)

print(fruits[5]) # Outputs 'orange'
#Negative Indexing
print(fruits[-4]) # Outputs 'kiwi'
#Range of Indexes
print(fruits[2:5]) # Outputs ('cherry', 'apple', 'cherry')

#Tuples are unchangeable, meaning that you cannot change, add, or remove items after the tuple has been created.
#But we can convert the tuple into a list, change the list, and convert the list back into a tuple.
#Convert the tuple into a list to be able to change it:

fruit_list=list(fruits)
print("Conver tupple to list:",fruit_list)
fruit_list[1]="strawberry"
print("List after change:",fruit_list)
#Convert the list back into a tuple:
fruits=tuple(fruit_list)
print("Convert list back to tuple:",fruits)


#When we create a tuple we normally assign values to it.This is called "packing"
cars=("BMW","Audi","Ford","Tata")

#But in python ,we are also allowed to extract the values back into variables.This is called "unpacking"
print("Unpacking Tuple:")
car1,car2,car3,car4=cars
print(car1)
print(car2)
print(car3)
print(car4)

#We can use an asterisk (*) to collect the remaining values as a list.

print("Using Asterisk to collect remaining values:")
car1,car2,*car3=cars
print(car1)
print(car2)
print(car3)


#Joining Tuples
tuple1=("A","B","C")
tuple2=(1,2,3)
tuple3=tuple1+tuple2
print("Joining Tuples:",tuple3)

#Multiply Tuples
tuple4=("Hello",)*3
print("Multiply Tuples:",tuple4)
