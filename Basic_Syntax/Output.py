"""
File Name: python_print_output_cheat.py
Purpose  : Complete Python print() & output formatting cheat sheet
Author   : Ashikur Rahaman 
"""

#---------------------------------------------------------
# 1. BASIC PRINT
#---------------------------------------------------------

print("Hello, World!")


# print() displays text or values to the console.
""" Used for output, debugging, and logging.
| Escape | Description     | Example            | Output       |
| ------ | --------------- | ------------------ | ------------ |
| `\n`   | New line        | `"A\nB"`           | A<br>B       |
| `\t`   | Tab             | `"A\tB"`           | A B          |
| `\\`   | Backslash       | `"C:\\path"`       | C:\path      |
| `\"`   | Double quote    | `"He said \"Hi\""` | He said "Hi" |
| `\'`   | Single quote    | `'It\'s OK'`       | It's OK      |
| `\r`   | Carriage return | `"Hi\rBye"`        | Bye          |
| `\b`   | Backspace       | `"AB\bC"`          | AC           |
"""

#---------------------------------------------------------
# 2. NEW LINE USING \n
#---------------------------------------------------------

print("Line 1\nLine 2\nLine 3")

#'\n' creates a new line inside a string.
#Useful for multi-line formatted output.


#---------------------------------------------------------
# 3. TAB SPACE USING \t
#---------------------------------------------------------

print("Name\tAge\tCity")
print("Akash\t23\tDhaka")

#'\t' adds horizontal spacing.
#Common for table-like output.


#---------------------------------------------------------
# 4. BACKSLASH USING \\
#---------------------------------------------------------

print("C:\\Users\\Akash\\Documents")

#'\\' prints a single backslash.
#Required because '\' is an escape character.


#---------------------------------------------------------
# 5. SINGLE QUOTE USING \'
#---------------------------------------------------------

print('It is a \'beautiful\' day!')

# Escaping allows quotes inside strings.
# Prevents syntax errors.


#---------------------------------------------------------
# 6. DOUBLE QUOTE USING \"
#---------------------------------------------------------

print("He said, \"Hello!\"")

#Escaped double quotes allow quoted speech in strings.


#---------------------------------------------------------
# 7. PRINTING VARIABLES
#---------------------------------------------------------

name = "Akash"
age = 23
print("Name:", name, "Age:", age)

#Multiple variables can be printed using commas.
#Python adds spaces automatically.


#---------------------------------------------------------
# 8. SEPARATOR (sep PARAMETER)
#---------------------------------------------------------

print("Apple", "Banana", "Cherry", sep="---")
print("2024", "06", "15", sep="/")

#'sep' controls how values are separated.
#Common in dates, logs, and structured output.


#---------------------------------------------------------
# 9. END PARAMETER (PRINT WITHOUT NEW LINE)
#---------------------------------------------------------

print("Ashik is a ", end="")
print("good boy.")

#'end' replaces the default newline.
# Used for same-line output.


#---------------------------------------------------------
# 10. COMBINING sep AND end
#---------------------------------------------------------

print("Python", "Java", "C++", sep=" | ", end=" <<< End of Languages\n")

#Allows full control over formatting.
# Useful in CLI tools and logging.


#---------------------------------------------------------
# 11. STRING CONCATENATION USING +
#---------------------------------------------------------

first_name = "Ashikur"
last_name = "Rahaman"
print("Full Name: " + first_name + " " + last_name)

#'+' joins strings.
#Numbers must be converted using str().


#---------------------------------------------------------
# 12. F-STRING (RECOMMENDED)
#---------------------------------------------------------

height = 5.5
weight = 70
print(f"Name: Ashikur Rahaman\nHeight: {height} feet\nWeight: {weight}")

#f-strings allow direct variable embedding.
#Best readability and performance.


#---------------------------------------------------------
# 13. format() METHOD
#---------------------------------------------------------

Department = "CSE"
Batch = 2022
print("University: {}\nBatch: {}\nDepartment: {}".format("UIU", Batch, Department))

#Older formatting style.
#Still found in legacy codebases.


#---------------------------------------------------------
# 14. RAW STRING
#---------------------------------------------------------

print(r"C:\new\test")
print("C:\\new\\test")

# Raw strings ignore escape sequences.
# Best for file paths and regex.


#---------------------------------------------------------
# 15. ASCII VALUE USING ord()
#---------------------------------------------------------

print("ASCII value of A is:", ord('A'))

#ord() returns ASCII/Unicode value of a character.


#---------------------------------------------------------
# 16. CHARACTER FROM ASCII USING chr()
#---------------------------------------------------------

print(chr(65))

#chr() converts ASCII/Unicode value to character.


#---------------------------------------------------------
# 17. MULTI-LINE TEXT USING TRIPLE QUOTES
#---------------------------------------------------------

print("""Hello
This is
Multi-line
Text""")

#Triple quotes allow multi-line strings.
# Common in documentation and templates.


#---------------------------------------------------------
# 18. LOOP OUTPUT (SAME LINE)
#---------------------------------------------------------

for i in range(1, 6):
    print(i, end=" ")
print()

#Useful for counters, progress display, CLI output.

#---------------------------------------------------------
# 19. NUMBER FORMATTING
#---------------------------------------------------------

pi = 3.1415926
print(f"Pi value: {pi:.2f}")

#  Controls decimal precision.
# Important for finance & analytics.


#---------------------------------------------------------
# 20. EMOJI / UNICODE OUTPUT
#---------------------------------------------------------

print("Python 🚀 Backend ❤️")

#Python supports Unicode by default.
