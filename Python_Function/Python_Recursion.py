#Recursion is when a function calls itself.
#A simple recursive function that counts down from 5:

def count_down(n):
      if n<=0:
            print("Count Down Complete")
      else:
         print(n)
         count_down(n-1)

#Call the main function
count_down(5)

#Base Case and Recursive Case
#A base case - A condition that stops the recursion
#A recursive case - The function calling itself with a modified argument

# Identifying base case and recursive case:
print("\n Factoria: ")
def factorial(n):
     if n==0 or n==1:
          return 1
     else:
          return n*factorial(n-1)
          
print(factorial(5))

#Fibonacci Sequence
print("\nFibonacci Series")
def fibonacci(n):
     if n<=1:
          return n
     else:
          return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(7))



# Find the maximum value in a list:
def find_max(numbers):
     if len(numbers)==1:
          return numbers[0]
     else:
          max_of_the_rest=find_max(numbers[1:])
          return numbers[0] if numbers[0]>max_of_the_rest else max_of_the_rest

my_list=[1,2,55,45,12,100,4545]
print("Max Valur from the List: ",find_max(my_list))