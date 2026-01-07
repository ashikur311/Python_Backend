#A variable is only available from inside the region it is created. This is called scope.

# Local Scope: A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

def myfunc1():
  x = 300 # x can only access inside the myfunction
  print(x)

myfunc1()

#The local variable can be accessed from a function within the function:
def myfunc2():
  x = 300
  def my_inner_func():
    print(x) # my inner function can access the value of "x", because the function is also inside the my_function.
  my_inner_func()

myfunc2()

# Global Scope:A variable created in the main body of the Python code is a global variable and belongs to the global scope.

# Global variables are available from within any scope, global and local.


x = 300

def myfunc3():
  print(x)

myfunc3()

print(x) # "x" can be access from anywhere of the same file


# If you need to create a "global" variable, but are stuck in the local scope, you can use the "global" keyword.
def myfunc4():
  global x
  x = 300

myfunc4()

print(x) # because of "global" keyword now we can access value of "x"

#Nonlocal Keyword: The "nonlocal" keyword is used to work with variables inside nested functions.

#If you use the nonlocal keyword, the variable will belong to the outer function:
def myfunc5():
  x = "Jane"
  def myfunc6():
    nonlocal x
    x = "hello"
  myfunc6()
  return x

print(myfunc5())