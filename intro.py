# ===== STRINGS =====
# Strings in Python are surrounded by either single quotation marks, or double quotation marks
# 'hello' is the same as "hello"

# You can display a string literal with the print() function
print("Hello, World!")
print('Hello, World!')  
# print("Hello World!")

# This is a comment
# This is another comment
# print("Hello World!")  # This is a comment

# ===== VARIABLES =====
# Variables are used to store data values
# Variables are created when a value is assigned to it
x = 5
y = "Hello, World!" 
print(x)
print(y)

name = "Koiree"
last_name = "Koiree"
cohort = 55
is_active = True
print(name + " " + last_name + " " + str(cohort))
# f-string
# f-string is a way to format strings in Python
# f-string is a way to embed expressions inside string literals
# f-string is a way to evaluate expressions inside string literals
# f-string is a way to evaluate variables inside string literals
# f-string is a way to evaluate functions inside string literals
# f-string is a way to evaluate methods inside string literals  
print(f"{name} {last_name} {cohort}")
print(f"1 + 1 = {1 + 1}")
print(f"{name.upper()} {last_name.upper()} {cohort}")
print(f"{name} {last_name} {cohort} {is_active}")

# ===== TYPE CONVERSION =====
num = 9.75
print(num)# 9.75 covert the number to a string
print(type(num))# covert the number to a float
print(int(num))# 9 converts the number to an integer
print(type(int(num))) # convert the number to a string
print(float(int(num))) # convert the number to a float
print(str(num)) #converts the number to a string
print(type(str(num))) # covert the number to a string
print(float(num)) #converts the number to a float
print(type(float(num))) #converts the number to a float
price = "9.75" #converts the string to a float
print(price) #converts the string to a float
print(type(price)) #converts the string to a float
print(float(price)) #converts the string to a float
print(type(float(price))) #cover the string to a float
print(int(float(price))) #converts the string to an integer
print(type(int(float(price)))) #converts the string to an integer

# ===== CHALLENGE =====
# Create some variables called: name, age, height, and city, show them in a print statement
# Step 1: Create the variables
# Step 2: Print the variables
# Step 3: Use different methods to format the string
# Step 4: Use different methods to concatenate the string
# Step 5: Use different methods to convert the variables to a string
# Step 6: Use different methods to convert the variables to an integer
# Step 7: Use different methods to convert the variables to a float
# Step 8: Use different methods to convert the variables to a boolean
# Step 9: Use different methods to convert the variables to a list
name = "Koiree"
age = 37
height = 5.5
city = "Seattle"
print(f"My name is {name}. I am {age} years old. I am {height} tall. I live in {city}") #f-string
print("My name is " + name + ". I am " + str(age) + " years old. I am " + str(height) + " tall. I live in " + city) #concatenation
print("My name is", name, ". I am", age, "years old. I am", height, "tall. I live in", city) #comma-separated
print("My name is {} . I am {} years old. I am {} tall. I live in {}".format(name, age, height, city)) #format()
print("My name is %s. I am %d years old. I am %f tall. I live in %s" % (name, age, height, city)) # % operator
print(str(age) + " " + str(height)) #concatenation
print(str(age) + " " + str(height) + " " + city) # concatenation
print(str(age) + " " + str(height) + " " + city + " " + name) #
print(str(age) + " " + str(height) + " " + city + " " + name + " " + str(age) + " " + str(height) + " " + city + " " + name) # CONCATENATION
print(f"{age} {height} {city} {name} {age} {height} {city} {name}") # f-string
print(f"{age} {height} {city} {name} {age} {height} {city} {name} {age} {height} {city} {name}") # f-string
print(f"{age} {height} {city} {name} {age} {height} {city} {name} {age} {height} {city} {name} {age} {height} {city} {name}") #f-string

# ====== ARITHMETIC OPERATORS =====
# Arithmetic operators are used with numeric values to perform common mathematical operations
# Addition +
# Subtraction -
# Multiplication *
# Division /
# Modulus %
# Exponentiation **
# Floor division //
x = 5
y = 2
print(x + y) # Addition is a normal addition operation
# returns an integer
# Addition is a normal addition operation
print(x - y) # Subtraction is a normal subtraction operation
# returns an integer
print(x * y) # Multiplication is a normal multiplication operation
print(x / y) # Division is a normal division operation       
# returns a float
# Division always returns a float 
print(x % y) # Modulus is the remainder of the division of the first operand by the second
# The modulus operator returns the remainder of the division of the first operand by the second
print(x ** y) # Exponentiation operator returns the first operand raised to the power of the second
# The exponentiation operator returns the first operand raised to the power of the second    
print(x // y) # Floor division operator returns the largest possible integer
# The floor division operator returns the largest possible integer
# The floor division operator returns the largest possible integer that is less than or equal to the division of the first operand by the second
print(5 + 2) # Addition 
print(5 - 2) # Subtraction # Subtraction is the same as 5 - 2
print(5 * 2) # Multiplication is the same as 5 x 2
print(5 / 2) # Division is always returns a float
print(5 % 2) # Modulus # Modulus is the remainder of the division of the first operand by the second
print(5 ** 2) # Exponentiation # Exonentiation is the same as 5 * 5
print(5 // 2) # Floor division is a normal division operation except that it returns the largest possible integer    

# ====== ASSIGNMENT OPERATORS =====
# Assignment operators are used to assign values to variables
# Assignment operators are used to assign values to variables
# Assignment operators are used to assign values to variables

# x = 5

# x = 5 is an assignment operation
# x is a variable
# = is an assignment operator
# 5 is a value
# x = 5 assigns the value 5 to the variable x

# ====== BOOLEAN OPERATORS =====
# Boolean operators are used to evaluate expressions
# Boolean operators are used to evaluate expressions and return a boolean value
# Write a program that uses boolean operators to evaluate expressions


# ====== LOGICAL OPERATORS =====
# Logical operators are used to combine conditional statements
# Logical operators are used to combine conditional statements and return a boolean value
x = 5
y =10

print(x > 3 and x < 10) # and operator returns True if both statements are true
# and operator returns True if both statements are true
# and operator returns False if one of the statements is false
print(x > 3 or x < 15) # or operator returns True if one of the statements is true
# or operator returns True if one of the statements is true
# or operator returns False if both statements are false
print(not(x > 3 and x < 10)) # not operator returns False if the result is true

# ====== COMPARISON OPERATORS =====
# Comparison operators are used to compare two values
# Comparison operators are used to compare two values and return a boolean value
# 
# Equal ==
# Not Equal !=
# Greater Than >
# Less Than <
# Greater Than or Equal To >=
# Less Than or Equal To <=
# Equal
x = 5       
y = 3
print(x == y) # Equal
# Not Equal
print(x != y) # Not Equal
# Greater Than
print(x > y) # Greater Than     
# Less Than
print(x < y) # Less Than
# Greater Than or Equal To
print(x >= y) # Greater Than or Equal To
# Less Than or Equal To
print(x <= y) # Less Than or Equal To
print(5 == 3) # Equal
print(5 != 3) # Not Equal
print(5 > 3) # Greater Than
print(5 < 3) # Less Than
print(5 >= 3) # Greater Than or Equal To
print(5 <= 3) # Less Than or Equal To   






