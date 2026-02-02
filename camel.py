enter_variable_name = input("Enter variable name: ")

for letter in enter_variable_name:
    if letter.isupper():
        print("_"+letter.lower(),end="")
    else:
        print(letter,end="")
print()