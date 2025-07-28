# We can convert for example between celsius and fahrenheit.

while True:

    C = input("Enter the temperature in Celsius: \n")
    if C.isdigit():              # We use method isdigit() to check if the input is a number.
        break
    else:
        print("Temperature must be a number. Please try again.")

F = (float(C) * 9/5) + 32

print(f"{C} Celsius is equal to {F} Fahrenheit.")


# And between for example cm and inches.

while True:

    try:          # We using try-except block to catch non-integer values and negative values. 
        cm = float(input("Enter the height in cm: \n"))
        if cm < 0:          # We changing the type of variable cm to float, because operation of division is not possible with string.
            print("Height cannot be negative. Please try again.")
        else:
            break
    except ValueError:
        print("Height has to be a number. Please try again.")

inches = float(cm) / 2.54
print(f"{cm} cm is equal to {inches: .2f} inches.")             # We use format specifier to limit the number of decimal places to 2.








