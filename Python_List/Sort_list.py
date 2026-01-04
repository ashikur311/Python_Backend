fruits=["apple", "Banana", "cherry", "kiwi", "mango","orange","grape","pear"]
numbers=[1, 5, 3, 2, 8, 6, 10, 8]
print("Original fruits list:",fruits)
print("Original numbers list:",numbers,"\n")

# Sort the list ascending, by default sort() method sorts the list ascending and case sensitively ,So uppercase letters come before lowercase letters
fruits.sort()
numbers.sort()
print("Shorting Sccending: ",fruits)
print("Short Accending Numbers: ",numbers)

#The reverse() method reverses the current sorting order of the elements.
fruits.reverse()
numbers.reverse()
print("Reversing the sorted list: ",fruits)
print("Reversing the sorted numbers: ",numbers)



# Make a copy of a list with the copy() method 
product=["laptop","tablet","smartphone","desktop"]
new_product=product.copy()
print("Original product list:",product)
print("Copied product list:",new_product)

# Make a copy of a list with the list() method:
new_product2=list(product)
print("Copied product list using list() method:",new_product2)

# Use slicing to make a copy of a list:
new_product3=product[:]
print("Copied product list using slicing:",new_product3)



# Join two lists using the + operator
list1=["a","b","c"]
list2=[1,2,3]
joined_list=list1+list2
print("Joined list using + operator:",joined_list)


# Join two lists using the extend() method
list1.extend(list2)
print("Joined list using extend() method:",list1)
# Join two lists using a for loop
list3=["a","b","c"]
for item in list2:
      list3.append(item)
print("Joined list using for loop:",list3)