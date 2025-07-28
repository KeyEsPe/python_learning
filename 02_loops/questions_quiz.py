# This program will ask the user some questions and return the answear and type of variable provided by the user. 

while True: 
    answer = input("Is the Python programming language easy to learn? (yes/no): \n")
    if answer.lower() == "yes":      # Method 'lower()' is used to convert the string to lowercase, so it doesn't matter what case the user types.
        break
    elif answer.lower() == "no":
        break
    else:
        print("Please answer with 'yes' or 'no'.")
              
print(f"\nYour answer is: {answer}")
print(f"Type of your answer is: {type(answer)}")


while True:
    try:
        answer1 = int(input("How many programming languages do you know? (1, 2...): \n"))
        if answer1 < 0:
            print("Number of languages cannot be negative. Please try again.")
        else:
            break
    except ValueError:
        print("Please enter a number.")

print(f"\nYour answer is: {answer1}")
print(f"Type of your answer is: {type(answer1)}")

