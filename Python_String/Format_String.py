#To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.

name="Ashikur Rahaman Akash"
age=27
print(f"My Name is {name} and I am {age} years old")

#Display the price with 2 decimals:
price=49.99
print(f"The fruit price is ${price:.2f}")

#You can also use expressions inside the curly brackets:
width=54
height=29

print(f"The area of the rectangle which width={width} and height={height} is = {width*height} square units ")

#You can call functions inside the curly brackets:
import math
radius=7
print(f"The area of a circle with radius={radius} is = {math.pi*radius**2:.2f} square units")

#You can use format() method to format strings.
quantity=3
itemno=567
price=49.99
my_order="I want to pay {2} dollars for {0} pieces of item number {1}."
print(my_order.format(quantity,itemno,price))


# The "is" operator returns True if both variables point to the same object:
# The "is not" operator returns True if both variables are not the same object
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

#Difference Between is and ==
# is - Checks if both variables point to the same object in memory
# == - Checks if the values of both variables are equal