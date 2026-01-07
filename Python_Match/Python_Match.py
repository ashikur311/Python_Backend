#Instead of writing many if..else statements, you can use the match statement.

#The match statement selects one of many code blocks to be executed.
#it is similar to switch case statements in C,Java etc.
day=3
match day:
      case 1:
            print("Monday")
      case 2:
            print("Tuesday")
      case 3:
            print("Wednesday")
      case 4:
            print("Thursday")
      case 5:
            print("Friday")
      case 6:
            print("Saturday")
      case 7:
            print("Sunday")
      case _: #Default case if no case matches it will be executed.
            print("Invalid day")


#You can use the pipe symbol (|) to separate multiple values in a single case.
letter="B"
match letter:
      case "A" | "E" | "I" | "O" | "U":
            print(letter, "is a vowel.")
      case _:
            print(letter, "is a consonant.")

#You can add if statements in the case evaluation as an extra condition-check:

month=5
day=7
match month:
      case 1|2|3|4|5 if month==4:
            print("A weekday in April.")
      case 6|7 if month==4:
            print("A weekend in April.")
      case _:
            print("Another month.")


#Another One
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")