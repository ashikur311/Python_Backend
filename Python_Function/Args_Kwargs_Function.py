# By default, a function must be called with the correct number of arguments.
# However, sometimes you may not know how many arguments that will be passed into your function.
#*args and **kwargs allow functions to accept a unknown number of arguments.

#If you do not know how many arguments will be passed into your function, add a * before the parameter name.

def my_function1(*kids):
  print("The youngest child is " + kids[2])

my_function1("Emil", "Tobias", "Linus")

#The *args parameter allows a function to accept any number of positional arguments.
def my_function2(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function2("Emil", "Tobias", "Linus")