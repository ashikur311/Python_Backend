#The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
#elif is short for "else if".
age=18
if age<18:
      print("You are a minor.")
elif age==18:
      print("You just became an adult!")
else:
      print("You are an adult.")


#Short Hand If...Else
#You can also write the above code using a short hand if...else statement.
a=5
b=10
print("A is greater than B") if a>b else print("B is greater than A")

#You can also use a one-line if/else to choose a value and assign it to a variable:
max_value =a if a>b else b
print("Maximum value is:",max_value)

#You can also have multiple else statements on the same line:
num=15
result="Even" if num%2==0 else "Odd"
print("The number is",result)


#You can also have multiple elif statements on the same line:
score=85
grade="A" if score>=90 else "B" if score>=80 else "C" if score>=70 else "D" if score>=60 else "F"
print("Your grade is:",grade)


#Nested If...Else
num2=20
if num2>=0:
      if num2==0:
            print("Zero")
      else:
            print("Positive Number")
else:
      print("Negative Number")


#Logical Operators:
#-----------------------
#You can use the logical operators (and, or, not) to combine conditional statements.

number=85
if number<90 and number<=84:
      print("You passed the exam with A- grade.")

username = "Tobias"
password = "secret123"
is_verified = True
#Multiple conditions with and
if username and password and is_verified:
  print("Login successful")
else:
  print("Login failed")

#Mixed conditoions with or and and
age = 25
has_permission = False
if age >= 18 or has_permission:
  print("Access granted")
else:
      print("Access denied")

#Using not , it is used to reverse the result, returns False if the result is true
is_student = True
if not is_student:
  print("You are not a student")
else:
      print("You are a student")


#Pass Statement, it is used when a statement is required syntactically but you do not want any command or code to execute.
age2=16
if age2<18:
      pass  # Placeholder for future code
else:
      print("You are an adult.")