# Pip packages are very useful, because they contain ready blocks f the code to use, for various tasks. To use them, we need to first install 
# desired ones via terminal, using pip commands. 

# Below package pyfiglet, which we can use for creating ASCII art from the text. 

import pyfiglet

def save_users_output():

    user_text = input("Please enter text you would like to change for ASCII art: \n")

    ascii_art = pyfiglet.figlet_format(user_text)         # Generates ASCII art according to the user output. 

    file_name = input("Please enter the name of the file (for example my_ascii.txt): \n")
    try:             # We using block try - except for saving the content in the file, in case of the errors during saving. 
        with open(file_name, "w") as file:     # It openes the file named by the user in write "w" mode nad assignes it to the variaible "file". 
            file.write(ascii_art)    # Saves generated ASCII art to the opened file. 
        print(f"ASCII art has been saved sucessfully as '{file_name}'.")         
    except IOError as e:       # In case of the error "e" occured
        print(f"Error occured: {e}")     # It will return the informaition about the error. 

save_users_output()

# Below simple weather forecasting using API, and it saves the result in the file. 

import requests       # Request library anables to fetch the data. 

def weather():
    location = input("Please enter location for weather forecast: ")
    response = requests.get(f"https://wttr.in/{location}?format=3")    # Fetch the weather forecast from the wttr API. We use specific format to gather basic info. 
    
    weather_data = response.text     # We use atribute .text to get actual HTTP response, so weather forecasting. Otherwise it would be something like "response[200]
    file_name = input("Please enter the name of the file you would like to save the weather forecast: ")
    try:
        with open(file_name, "w") as file:
            file.write(weather_data)
        print("Your weather forecast has been saved sucessfully.")
    except IOError as e:
        print(f"Error occured: {e}")
 
weather()