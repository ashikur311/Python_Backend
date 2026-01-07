#In Python, a function is defined using the def keyword, followed by a function name and parentheses:

def my_function():
      print("Hello from a function")

#Calling a Function
my_function()

#Function with Parameters
def greet(name):
      print("My name is:",name)

#Calling the function with an argument
greet("Ashikur Rahman")


#Function with Return Value
def add(num1,num2):
      return num1+num2

sum=add(5,10)

#Function definitions cannot be empty. If you need to create a function placeholder without any code, use the pass statement:
def placeholder_function():
      pass
#Calling the placeholder function
placeholder_function()

#Function with Default Parameter Value
def greet_with_default(name="Guest"):
      print("Hello,",name)
#Calling the function without an argument
greet_with_default()
#Calling the function with an argument
greet_with_default("Ashikur")