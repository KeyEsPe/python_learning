# This is a simple Python script that takes user input for name, age, and height,
# and then prints a greeting message along with the user's age in 10 years.

# name = input("Enter your name: \n")
# age = int(input("Enter your age: \n"))
# height = int(input("Enter your height: \n"))

# print(f"\n\nHello {name}, you are {age} years old and your height is {height} cm.")

# aging = age + 10 
# print(f"\nIn 10 years you will be {aging} years old.")

# But what if the user enters a number instead of a string for the name? 
# We can add a check to ensure that the name is a string and contains only alphabetic characters.
# We use while loop with the isalpha() method to check if the input is valid. If yes, we go to the next input,
# otherwise we ask the user to try again.

# while True:
#     name = input("Enter your name: \n")
#     if name.isalpha():
#         break
#     else:
#         print("This does not look like a name. Please try again.")

# Now we can add a check for the age input to ensure that it is a valid integer. We use while loop with 
# try-except block to catch any ValueError exceptions that may occur if the user enters a non-integer value.
# Also we can add a check to ensure that the age is not negative.

# while True:
#     try:
#         age = int(input("Enter your age: \n"))
#         if age < 0:
#             print("Age cannot be negative. Please try again.")
#         else:
#             break
#     except ValueError:
#         print("Age has to be a number. Please try again.")

# # Same we can do for the height input. 

# while True: 
#     try: 
#         height = int(input("Enter your height: \n"))
#         if height < 0:
#             print("Height cannot be negative. Please try again.")
#         else:
#             break
#     except ValueError:
#         print("Height has to be a number. Please try again.")



# Than finally we have a complete code that takes user input for name, age, and height,
# check whether the inputs are valid, and then prints a greeting message along with the user's age in 10 years.

while True:
     name = input("Enter your name: \n")    # Variable has to be defined from the input inside the loop, than it will ask for the valid input till the user gives it. 
     if name.isalpha():    # Method isalpha() checks if the string contains only alphabetic characters.
         break
     else:
        print("This does not look like a name. Please try again.")


while True:
     try:
         age = int(input("Enter your age: \n"))
         if age < 0:
             print("Age cannot be negative. Please try again.")
         else:
             break
     except ValueError:
         print("Age has to be a number. Please try again.")

while True: 
     try: 
         height = int(input("Enter your height: \n"))
         if height < 0:
             print("Height cannot be negative. Please try again.")
         else:
             break
     except ValueError:
         print("Height has to be a number. Please try again.")

print(f"\n\nHello {name}, you are {age} years old and your height is {height} cm.")
aging = age + 10
print(f"\nIn 10 years you will be {aging} years old.")

