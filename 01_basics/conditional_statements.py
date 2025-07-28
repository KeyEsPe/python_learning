# This program will ask the user for ther age and return a message based on the age. 
# We will protect the code from invalid inputs. 
# In this program we will use the following conditional statements: if, elif, else. 

while True:

    try:
        age = int(input("Please enter your age: \n"))

        if age < 0:                      # IF age is negative than...
            print("Age cannot be negative. Please try again.")
            continue
        elif age == 0:                   #  We use elif instead of if, becasue we want to check the next condition if the first one is not true.     
            print("You are a newborn.")
        elif age < 18:
            print("You are a minor.")
        elif age < 65:
            print("You are an adult.")
        elif age > 100:
            print("Impressive! Are you a dinosaur?")
        else:                           # Else serving as a catch-all for any other age.
            print("You are a senior citizen.")
        break
    except ValueError:
        print("Age has to be a number. Please try again.")


# Following code will validate the password. 
# The password has to be at least 8 characters long, contain at least one uppercase letter, one lowercase letter, one digit, and one special character.

while True:
        
        password = input("Please enter your password: \n")

        if len(password) < 8:
            print("Password must be at least 8 characters long.")
        elif not any(char.isupper() for char in password):
            print("Password must contain at least one uppercase letter.")
        elif not any(char.islower() for char in password):
            print("Password must contain at least one lowercase letter.")
        elif not any(char.isdigit() for char in password):
            print("Password must contain at least one digit.")
        elif not any(char in "!@#$%^&*()-_=+[]{};:,.<>?/" for char in password):
            print("Password must contain at least one special character.")
        else:
            print("Password is valid.")
            break

# The program will ask the user for exam score and return a message based on the score.

while True: 
    try:
        score = float(input("Please enter your exam score: \n"))

        if score < 0 or score > 100:
            print("Score must be between 0 and 100.")
            continue
        elif score >= 90:
            print("You got an A.")
        elif score >= 80:
            print("You got a B.")
        elif score >= 70:
            print("You got a C.")
        elif score >= 60:
            print("You got a D.")
        else:
            print("You got an F.")
        break
    except ValueError:
        print("Score has to be a number. Please try again.")

# This program will ask the user for a number and check if: 
# The number is even or odd. Of couse we will protect the code from invalid inputs.

while True: 
    try:
        number = int(input("Please enter a number: \n"))
        if number % 2 == 0:
            print("The number is even.")
        else:
            print("The number is odd.")
        break
    except ValueError:
        print("The input has to be a number. Please try again.")
        
# The number is divided by 3 and/or 5. 

while True:
    try: 
        number = int(input("Please enter a number: \n"))    
        if number % 3 == 0 and number % 5 == 0:
           print("You number is divided by both 3 and 5.")
        elif number % 3 == 0: 
            print("Your number is divided by 3. ")
        elif number % 5 == 0: 
            print("You number is divided by 5.")
        else:
            print("Your number is not divided by 3 or 5.")
    except ValueError:
        print("Input invalid. ")
 
 # Using this code we will simulate coffee machine. 

while True: 

    try:

        drink = int(input("Please pick up the number for coffee: \n\n 1. Espresso \n 2. Cappuccino \n 3. Latte \n\n"))    

        if drink == 1:
            print("Espresso costs 1$")
            break
        elif drink == 2: 
            print("Cappuccino costs 2$")
            break
        elif drink == 3: 
            print("Latte costs 3$")
            break
        else:
            print("Please enter the number from 1-3.")
    except ValueError:
        print("Please enter the number of the drink. ")

# This code is a simple logging system, which will block the access after three failed password entry attempts. 

attempts_left = 3 

while True:

    login = "admin"
    password = "password"

    user_login = input("Please enter login: ")
    user_password = input("Please enter password: ")

    attempts_left -= 1 

    if user_login != login and user_password != password: 
        if attempts_left > 0:
           print(f"Login or password incorrect. Please try again. Attempts left: {attempts_left}")
        else:
            print("Access denied.")
            break
    else: 
        print("You are logged in successfully.")
        break

# This program will ask the user to answear 3 questions and return feedback about the amount of correct answers. 

score = 0

while True: 

    A = "Amsterdam"
    B = "Paris" 
    C = "Warsaw" 

    while True:
         
        answer_1 = input("What is the capital of the Netherlands? \n")

        if answer_1.isalpha():
            break
        else:
            print("Invalid input. Please try again. \n")

    while True:

        answer_2 = input("What is the capital of France? \n")

        if answer_2.isalpha():
            break
        else: 
            print("Invalid input. Please try again. \n")

    while True: 
        
        answer_3 = input("What is the capital of Poland? \n")

        if answer_3.isalpha():
            break
        else: 
            print("Invalid input. Please try again. \n")


    if answer_1.lower() == A.lower():
        score += 1
    if answer_2.lower() == B.lower():
        score += 1
    if answer_3.lower() == C.lower():
            score += 1 

    if score == 3:
        print("3 from 3 correct. Excellent job!")
        break
    elif score == 2: 
        print("2 form 3 correct. Good job!")
        break
    elif score == 1: 
        print("1 from 3 correct. Not bad.")
        break
    else:
        print("0 from 3 correct. Good luck next time!")
        break

# This code will ask user about the day of the week and return information about it accordingly. 

while True: 

    weekdays = ["monday" , "tuesday" , "wednesday" , "thursday" , "friday" , "saturday" , "sunday"]
    day = input("Please enter the day of the week: ")

    if not day.isalpha():
        print("Invalid day of the week. Please try again.")
        continue
    elif day.lower() in weekdays:
        if day.lower() == "monday":
            print("Should be banned.")
            break
        elif day.lower() == "tuesday" or day.lower() == "wednesday" or day.lower() == "thursday":
            print("Working day.")
            break
        elif day.lower() == "friday":
            print("Amlost weekend!")
            break
        else:
            print("WEEKEND!")
            break
    else: 
        print("Please choose valid weekday.")
        continue
    














