# We will import from "datetime" library two modules: datetime and timedelta. 

from datetime import datetime, timedelta  

current_time = datetime.now()        # We create object datetime.now which will return currrent date and time. 

print(f"Current date and time: {current_time} \n")

my_birthday = datetime(2025, 8, 6)    # Here we create my birthday date. 

time_left = my_birthday - current_time    # And we checking how many days left to my birthday. 

print(f"Birthday countdown: {time_left.days} days left. \n")         # Adding .days we limit the output to days only. 

print("Dates for 7 following days:")

for i in range(1,8):                                       # We use loop with timedelta() to count date for 7 following days ffrom today. 
    next_day = current_time + timedelta(days = i)
    
    print(f"{i} : {next_day.strftime('%y-%m-%d')}")

# We use random library for drawing elements. First we will simply draw the number. 

import random            # We have to import random library first to be able to use it. 

random_digit = random.randint(1, 49)      # Function random.randint() allows to draw int from the selected range. 

print(f"Random number draw is: {random_digit}")

# We also can draw elements from the lists. 

random_name = random.choice(["Katarzyn", "Friso", "Dean"])

print(f"Random name from your list is: {random_name}")

# We can also shuffle the elements of our list. Every run of the program will return different output - shuffle. 

list = ["Ace", "King", "Queen", "Jack"]

print(f"This is your list before shuffle: {list}")

random.shuffle(list)

print(f"This is your list after shuffle: {list}")

# Below some operations from statistics library. 

import statistics

def output(mean, median, std):
    print(f"Mean of your grades is {mean:.2f}")             # :.2f we use if we want to have 2 decimal only. 
    print(f"Median of your grades is {median:.2f}")
    print(f"Standard deviation of your grades is {std:.2f}")

grades = [3.5, 4.0, 5.0, 4.5, 3.0, 5.0]

mean = statistics.mean(grades)

median = statistics.median(grades)

std = statistics.stdev(grades)

output(mean, median, std)

grades_above_mean = 0

for grade in grades: 
    if grade > mean:
        grades_above_mean +=1 

print(f"Number of grades above the mean: {grades_above_mean}")