# With this code we will do basic operations on the lists. 

tasks = ["learning", "gym", "shower"]

print(f"\nThis is our primary list: {tasks}")

tasks.append("cooking")     # Method append adds the new element on the end of the list. 
tasks.remove("gym")         # Method remove takes the element from the list. 
tasks.sort()

print(f"\nThis is our modified list: {tasks}")

print("\nThis is our enumerated list:")
for i, task in enumerate(tasks):
    print(f"{i + 1}. {task}")

# This code will operate on the numbers on the list. 

grades = [3.5, 4.0, 2.0, 5.0, 4.5]
print(f"Your grades are: {grades}")

sum = 0

for grade in grades:
    sum = sum + grade

n = len(grades)

average = sum / n 

print(f"Your average grade is {average}.")

high_grades = []

for grade in grades:
    if grade > 4.0:
        high_grades.append(grade)

print(f"Grades higher that 4: {high_grades}")

lowest_grade = min(grades) 
highest_grade = max(grades)

print(f"Your lowest grade is {lowest_grade}")
print(f"Your highest grade is {highest_grade}")

# This program will show us how to operate on tuples. 

person_primary = ("Anna", "Nowak", 1995)        # Here we have a tuple

name = person_primary[0], person_primary[1]     # To print out the certain information, we using indexes, so the spots in which the information is in the tuple. 

print(f"Name of the person: {name}")

age = 2025 - person_primary[2]         # Math operations are allowed on tuples. 

print(f"Age of the person: {age}")

person_for_modification = list(person_primary)        # We change our tuple into the list

person_for_modification[1] = ("Kowalska")         # Here we change the surname of the person, which is possible only after modification from tuple to list. 

person_modified = tuple(person_for_modification)   # Back to tuple

print(f"Person after modification: {person_modified}")

# Below you can find some operations on coordinates of points. 

import math       # We import mah module, os we can use some functions from it, like square root. 

points = [(0, 0), (3, 4), (1, 1), (5, 12)]

distances = []

for point in points:
    distance_current = math.sqrt(point[0]**2 + point[1]**2)
    distances.append(distance_current)

max_distance = max(distances)    

index_of_max_distance = distances.index(max_distance)        # We using index method to find the index of our max distance. 

farthest_point = points[index_of_max_distance]       # We using that index to take the farthest point form our list. 

print(f"The distance of each point from zero is: {distances}")
print(f"The farthest point form zero is the point {farthest_point}")

# Code below presents basic operations on the dictionary. 

contacts = {                      # This is our dictionary. 
    "Ala": "123-456-789",
    "Tomek": "987-654-321"
}

contacts["Ola"] = "365-518-963"        # This is how we add new couple to the dictionary. 
contacts["Ala"] = "123-456-965"        # And this is how we can change the existing argument. 

for name, number in contacts.items():       # We use foor loop to nicely print out our dictionary content. 
    print(f"{name}: {number}")

stock = {                    
    "milk": 5,
    "bread": 2,
    "butter": 0
}

unavailable_products = [product for product, quantity in stock.items() if quantity == 0]

for product in unavailable_products:
    print(f"Not in stock:\n {product}")

stock["eggs"] = 12

del stock["bread"]

for product, quantity in stock.items():
    if quantity >= 3:
        print(f"High in stock: \n {product}")


# Below we can train the sets. 

text = "Python is good programming language and Python is easy to learn"

words = text.split()     # Split function allows you to split a sentence into individual words that appear in it.

unique_words = set(words)    # We create set from unique the words from the sentence. Order is always random, duplicats are removed. 

num_unique_words = len(unique_words)   # We checking the numbers of unique words. 

print(f"All the words in the sentence: {words}") 
print(f"Unique words in the sentence: {unique_words}")
print(f"Number of the unique words in the sentence is: {num_unique_words}")
                            
list1 = ["apple", "banana", "cherry"]
list2 = ["banana", "kiwi", "apple", "melon"]

set1 = set(list1)     # We would like to convert our lists to sets. 
set2 = set(list2)

common_elements = set1.intersection(set2)       # Intersection() method is used to find common elements in the sets. 

only_in_set1 = set1.difference(set2)       # Difference() method return new set with the elements which are only in set1. 

all_unique_fruits = set1.union(set2)    # Union() method returns new set with unique elements frm both of the sets. Duplicates are not allowed in sets. 

print(f"Those are our sets: \n {set1} \n {set2}")
print(f"Common elements from both sets: {common_elements}")
print(f"Elements only from the first set: {only_in_set1}")
print(f"Common elements from both of the sets: {all_unique_fruits}")