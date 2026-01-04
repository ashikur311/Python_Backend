#You can return a range of characters by using the slice syntax.
#Specify the start index and the end index, separated by a colon, to return a part of the string.
# name[start:end]
Name = "Ashikur Rahaman Akash"
print(Name[0:6])  # Outputs 'Ashiku'
print(Name[7:14]) # Outputs 'Rahaman'
print(Name[15:20]) # Outputs 'Akash'

#Note: The character at the end index is NOT included.

#You can also specify a step value after the second index, separated by another colon.
# name[start:end:step]
print(Name[0:20:2]) # Outputs every second character from index 0 to 19

#If you omit the start index, the slice starts from the beginning of the string.
print(Name[:6])  # Outputs 'Ashiku'

#If you omit the end index, the slice goes to the end of the string.
print(Name[7:])  # Outputs 'Rahaman Akash'

#If you omit both the start and end index, the slice includes the whole string.
print(Name[:])   # Outputs 'Ashikur Rahaman Akash'

#You can use negative indexing to slice from the end of the string.

"""
Character:   P   Y   T   H   O   N
Positive:    0   1   2   3   4   5
Negative:   -6  -5  -4  -3  -2  -1
"""
X="PYTHON"
print(X[-5:])  # Outputs 'YTHON'

print(X[-3:-1]) # Outputs 'HO'

print(X[:-3])  # Outputs 'PYT'

#[::-1] Reverse string

print(X[::-1]) # Outputs 'NOHTYP'