# This code cannot be run as one piece, becasue the variables are defined in the same name for different purposes!!! Isolate first part of the code and run it.

# Type int = intiger for the numbers. 

int = 10 
print(type(int))         # Type function is used to check the type of variable. 

# Type float = float for the decimal numbers.

float = 10.5
print(type(float))

# Type str = string for the text. 

str = "Hello, World!"
print(type(str))

# Type bool = boolean for the true or false.

bool = True
print(type(bool))

# You also can use isinstance() function to check the type of variable. This funcion return True or False.

i = 10 

print(isinstance(i, int))      # We using isinstance() function to check if variable i is intiger.
print(isinstance(i, float))     
print(isinstance(i, str))        
print(isinstance(i, bool))        

# You can convert the type of variable using type casting. 

text = "123"           # This is a string, becase it is in quotes.

print(isinstance(text, str))        # We can check the type of variable using isinstance() function, to be sure it is string.
print(isinstance(text, int))  

digit = int(text)      # Now we convert the string to intiger using int() function.

print(isinstance(digit, str))   
print(isinstance(digit, int))

k = 10

print(isinstance(k, int))   

j = float(i)      # Now we convert the intiger to float using float() function.

print(j)
print(isinstance(j, float))

# What is interesting, we can convert also boolean to intiger. 

b = True

a = int(b) 

print(a)         
print(isinstance(a, int))   

# Let's look what will happen if we try add string and intiger. 

a = "10"
b = 5
c = a + b
print(c)         # This will not work, becasue we cannot add string and intiger.

# But if we convert string to intiger, it will work.

a = "10"
b = 5
c = int(a) + b   # We can commit the conversion in the same line, directly working with the variable a.   
print(c)         







