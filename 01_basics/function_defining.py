# Accoring to good programing practices, we should define funkcions to re-use them in a couple places in our code rather than 
# repiting the same block of code manually in every spot we need to use it. 

# There is a classic case to check if digit is a prime digit: 


def is_prime(n: int) -> bool:     # It means that function "is_prime" will take n arguments in intiger type and will return bool type of variable. 
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for digit in range(1,100):
    print(f"{digit} : {is_prime(digit)}")

# This program si a simple BMI calculator. 

def calculate_bmi(weight_kg: float, height_m: float) -> float:

    if weight_kg/height_m**2 < 18.5:
        print("Underweight.")
    elif weight_kg/height_m**2 >= 18.5 and weight_kg/height_m**2 <= 24.9:
        print("Normal weight.")
    else:
        print("Overweight.")

while True:

  try:
    weight_kg = float(input("Please enter your weight in kg: \n"))
    height_m = float(input("Please enter your height in m: \n"))
    break
  except ValueError:
    print("Invalid input. Weight and height must be a number. Try again: \n")
    continue

calculate_bmi(weight_kg, height_m)

# This is really simple function, for greeting the user. 

def greet_user(name):
    print(f"Hello {name}!")

user_name = input("Hi, what is your name? \n")

greet_user(user_name)

# Below we define function to check the length of the word. 

def word_length(word):
    return len(word)

words = ["Python", "is", "easy"]

for w in words:
    print(f"Word '{w}' got {word_length(w)} characters.")

# Below we define a function to check if the number is even or odd. 

def is_even(number):
    return number % 2 == 0


for n in [4, 7, 12]:
    if is_even(n):
        print(f"Digit {n} is even.")
    else:
        print(f"Digit {n} is odd.")
