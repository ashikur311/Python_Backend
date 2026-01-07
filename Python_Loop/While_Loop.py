#With the while loop we can execute a set of statements as long as a condition is true.
print("While Loop Example:")
i=5
while i>0:
      print("Value of i is:",i)
      i-=1  #Decrement i by 1 

#With the break statement we can stop the loop even if the while condition is true:
print("\nUsing break statement:")
j = 1
while j < 6:
  print(j)
  if j == 3:
    break
  j += 1 # It will print only 1,2,3

#With the continue statement we can stop the current iteration, and continue with the next:

print("\nUsing continue statement:")
k=0
while k<6:
      k+=1
      if k==3:
          continue
      print("Value of k is :",k) # It will print all values except 3


#With the else statement we can run a block of code once when the condition no longer is true:
print("\nUsing else statement with while loop:")
m=1
while m<6:
      print("Value of m is:",m)
      m+=1
else:
      print("m is no longer less than 6")