# This code will return all the elements from the list with their indexes. 

tasks = ["python", "AI and law", "AI tools", "cloud"]

for number, task in enumerate(tasks, start = 1):
    print(f"{number}. {task}")

# This code is a simple multiplication table for numbers from 1 to 10. 

def multiplication_table(scope):        # we define our function and say what it will do
  
  for i in range(1, scope + 1):
    for j in range(1, scope + 1):
      result = i * j
      print(f"{i} x {j} = {result}")

multiplication_table(10)        # here we call out our function for the numbers in range 1-10 

# This code counts number of the list's elements(without using sum function for training purposes).

numbers = [4, 2, 9, 1, 6]

summ = 0

for i in numbers: 
    summ = summ + i

print(summ)

# And this one checking how many of elements are greater than 5. 

numbers = [4, 2, 9, 1, 6]

greater = 0

for i in numbers:
    if i > 5:
        greater = greater + 1

print(greater)

# This program will return the names from the list, which contain more than 4 characters and create a new list from them. 

names = ["Katarzyna", "Friso", "Klaudia", "Lars", "Mateusz"]

longer = []

for name in names: 
    if len(name) > 4:
        longer.append(name)         # Method "append" adds element to the end of the list 

print(longer)

# This code will ask user for the sentence and count how many vowels are there and what is the frequency for each of them. Result will be return as a dictionary.

vowels = "aeyuio"      # We use here only small letters, so later when we lower the letters in user's sentence there will be no difference between A and a

dict = {}       # We create an empty dictionary

sentence = input("Please enter a short sentence: \n")

for char in sentence.lower():
    if char in vowels:
        if not char in dict:
            dict[char] = 1                # If the vowel is not in the dictionary, we add it and it's count is set up on "1"
        else:
            dict[char] += 1           # If the vowel is already in the dictionary, we add +1 to it's counter. 

if dict:               # We check if dictionary is not empty
    print("\nThe numbers of vowels in your sentence: \n")      
    for vowel, count in dict.items():
        print(f"'{vowel}' : {count} times.")
else: 
    print("There was no vowels in your sentence.")
        
# In this program we will use function zip() to "connect" both lists. It creates pairs - tuples from first element of the first list with first from second etc. 

names = ["Katarzyn", "Friso", "Tofik"]

scores = [30, 100, 90]

for name, score in zip(names, scores):
    print(f"{name} got {score} points.")

# This program will take the sentence from the user, extract the letters from it and return them as a list. 

sentence = input("Plese enter the sentence: \n").lower()    # We ask for the sentence and change it to lower case. 

sentence_without_punctuation = ""    # Create empty variable, in which we will store our charakters from the sentence without any punctuation. 

for sign in sentence:       # This loop will check if the sign is letter, number or space. 
    if ('a' <= sign <= 'z' or
        '0' <= sign <= '9' or
        sign == " "):
        sentence_without_punctuation += sign

letters = []     # Empty list for our letters

for sign in sentence_without_punctuation:         # This loop will check if each sign is a letter and if it is and it is not in our list yet, adds it - append
    if 'a' <= sign <= 'z' and sign not in letters:
        letters.append(sign)

n = len(letters)            # This is bubble sort algorithm, which will sort our letters alphabetically. 
for i in range(n):
    for j in range(0, n-i-1):
        if letters[j] > letters[j+1]:
            letters[j], letters[j+1] = letters[j+1], letters[j]

if len(letters) > 0:
    print("\nLetters from your sentence:")
    print(letters)
else:
    print("\nThere are no letters in your sentence.")

# This program will analyze the content of the dictionary. 

products = [              # This is a list with dictionary inside. 
    {"name": "eggs", "price": 2.5},
    {"name": "milk", "price": 1.8},
    {"name": "bread", "price": 2.0}
]

print("List of the products with prices: \n")
for product in products:
    print(product["name"] , product["price"])

# Here we are going to sum the price of all the products, advanced way is to use sum() function, which you can see below, but we will leave 
# it under the comments, since the oint is to learn how to use for loop. 

# total_price = sum(product["price"] for product in products)

# print(f"\nTotal price of the products: {total_price}")

total_price = 0

for product in products:
    total_price = total_price + product["price"]

print(f"\nTotal price of the products: {total_price}")

expensive = []       

for product in products:          # Here we checking which products cost more than 2$ and add them to our first empty "expensive" list. 
    if product["price"] > 2.0:
        expensive.append(product)

print("\nProducts that cost more than 2$:\n")
for product in expensive:
    print(product["name"] , product["price"])

# For numbers in range 1-30 the program will print certain word if the number meets the condition, otherwise will print just that number. Result is printed as a list.

numbers = []

for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        numbers.append("FizzBuzz!")
    elif i % 3 == 0:
        numbers.append("Fizz!")
    elif i % 5 == 0:
        numbers.append("Buzz!")
    else:
        numbers.append(i)

print(numbers)

# This code will generate the emails for each name and print it as a new list. 

names = ["Ala", "Tomek", "Ola"]

emails =[]

for name in names: 
    name = name.lower() + "@example.com"
    emails.append(name)

print(emails)
