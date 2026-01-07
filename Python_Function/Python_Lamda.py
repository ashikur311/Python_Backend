#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.


#Syntax
#lambda arguments : expression


#Add 10 to argument a, and return the result:

x=lambda a:a+10
print(x(5)) #We share the value of a

#Multiply argument a with argument b and return the result:
multiplication=lambda a,b:a*b
print(multiplication(5,6))

#Why Use Lambda Functions?
#The power of lambda is better shown when you use them as an anonymous function inside another function.

def myfunction(n):
      return lambda a:a*n

mydoubler=myfunction(2) # here 2 is the parameter value of myfunction

print(mydoubler(4)) #here 4 is the lambda value which we want to double

# Lambda with Built-in Functions

#The map() function applies a function to every item in an iterable:

#The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.

# Syntax: map(function, iterables)
#function: 	Required. The function to execute for each item
#iterable:  Required. A sequence, collection or an iterator object. You can send as many iterables as you like, just make sure the function has one parameter for each iterable.
numbers=[1,2,3,4,5,6,7,8,9,10]
doubled=list(map(lambda x:x*2 , numbers))
print(doubled)


#The filter() function creates a list of items for which a function returns True:

odd_numbers=list(filter(lambda x:x%2!=0,numbers))
print("Odd Numbers: ",odd_numbers)


# The sorted() function can use a lambda as a key for custom sorting:
# Eaxh tupple :("Emil", 25) here Name is x and age is x[1]
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students=sorted(students,key=lambda x:x[1])
print(sorted_students)