"""
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
Example:
Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
"""

fruit_list=["apple", "banana", "cherry", "kiwi", "mango"]
newfruit_list=[]

for fruit in fruit_list:
      if "a" in fruit:
            newfruit_list.append(fruit)
print(newfruit_list)

#Advanced List Comprehension We can do all the above with list comprehension syntax:
# newlist = [expression for item in iterable if condition == True]


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# Now create a new list that did not contain apple
newlist2=[x for x in fruits if x!='apple']
print(newlist2)

# Now create a new list with numbers between 1 and 10
numbers=[x for x in range(10)]
print(numbers)

# Now create a new list with even numbers between 1 and 10
even_numbers=[x for x in range(10)if x%2==0]
print(even_numbers)

# We can perform a function on each list item, like in the example below where we square each number in the list:
squared_numbers=[x**2 for x in range(10)]
print(squared_numbers)

uppercase_fruits=[x.upper() for x in fruits]
print(uppercase_fruits)

#The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
newlist3=[x if x!="banana" else "orange" for x in fruits]
print(newlist3)
