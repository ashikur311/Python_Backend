# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

print("For Loop For List:")
fruits=["apple", "banana", "cherry"]
for x in fruits:
      print(x)


print("For Loop For String:")
for x in "Ashikur":
      print(x)


print("For Loop For Dictionary:")
thsdict={
      "name":"Ashikur",
      "age":26,
      "department":"CSE"}
for x,y in thsdict.items():
      print(x,y)

# We can also use break and contunue statements in for loops 
print("For Loop with Break Statement:")
for x in fruits:
      if x=="banana":
            break # Exit the loop when x is "banana"
      print(x)
print("For Loop with Continue Statement:")
for x in fruits:
      if x=="banana":
            continue # Skip the rest of the loop when x is "banana"
      print(x) 

#Using the range() function
print("For Loop with Range Function:")
for x in range(5):
      print(x)

print("For Loop with Range Function (Start and End):")
for x in range(2, 5):
      print(x)

print("For Loop with Range Function (Start, End and Step):")
for x in range(2, 10, 3):
      print(x)


#The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

print("For Loop with Else Statement:")
for x in range(6):
  print(x)
else:
  print("Finally finished!")
#Note: The else block will NOT be executed if the loop is stopped by a break statement.

#for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.

print("For Loop with Pass Statement:")
for x in [0, 1, 2]:
      pass  # Placeholder for future code


#Nested Loops:
print("Nested For Loop Example:")
adj=["red", "big", "tasty"]
fruits=["apple", "banana", "cherry"]
for x in adj:
      for y in fruits:
            print(x, y)