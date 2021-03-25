mychoice = {
    1: "ADD",
    2: "SUBTRACT",
    3: "MULTIPLY",
    4: "DIVIDE",
    5: "FACTORIAL",
}

print(type(mychoice))

choice = int(input("Please enter your choice ( 1 - 5) : "))
print("You entered ",mychoice.get(choice, "Invalid choice"))

