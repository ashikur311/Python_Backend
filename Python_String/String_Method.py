Str="this is a Sample string for demonstrating string methods in Python."

#Capitalize the first character of the string
print(Str.capitalize())

#Convert the entire string to uppercase
print(Str.upper())

#Convert the entire string to lowercase
print(Str.casefold())

#Convert the string to tittle case
print(Str.title())

#Print a centered string in return of width x 
print(Str.center(100)) 

#Count the occurrences of a substring in the string
print("Count of 'string': " + str(Str.count("string")))

#Encode the string using the specified encoding
print(Str.encode(encoding="utf-8", errors="strict"))

#Check if the string ends with a specific substring
print(Str.endswith("Python."))

#Find the first occurrence of a substring in the string
print(Str.find("string"))

#Expand tabs in the string to spaces
Str_with_tabs = "this\tis\ta\tsample\tstring"
print(Str_with_tabs.expandtabs(tabsize=6))

#Find the last occurrence of a substring in the string
print(Str.rfind("string"))

# Searches and returns the first position of value 
print(Str.find("string"))
print(Str.index("string"))


# Join elements of an iterable to the end of the string
print(Str.join([" Join ", " these ", " words."]))
sep = " | "
result = sep.join(["Join", "these", "words"])
print(result)


#The strip() method removes any whitespace from the beginning or the end:
Str_with_spaces = "   Hello, World!   "
print(Str_with_spaces.strip())

#Replace a substring with another substring
print(Str.replace("Sample","Example"))

#Split the string into a list where each word is a list item
fruits="apple, banana, cherry"
print(fruits.split(","))


