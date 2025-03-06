# Simple Python Excercise

# Please deliver the python scripts where you demonstrate practicing python, the user of variables, functions (test.py)
# 1. Used the Addtion, Subtraction, Multiplication, and Division operators
# 1 - Sum
# 2 - Subtract
# 3 - Multiplication
# 4 - Division
# 5 - Guess my age

# Step 1: Perform basic arithmetic operations

# Define two numbers
num1 = 10
num2 = 5

# Addition
sum_result = num1 + num2
# Subtraction
sub_result = num1 - num2
# Multiplication
mul_result = num1 * num2
# Division
div_result = num1 / num2  # Division always returns a float

# Print results
print(f"Sum: {sum_result}")
print(f"Subtraction: {sub_result}")
print(f"Multiplication: {mul_result}")
print(f"Division: {div_result}")

# Step 2: "Guess My Age" Game
def guess_my_age():
    my_age = 37  # Change this to your actual age
    guess = int(input("Guess my age: "))  # Take user input and convert to integer

    # Compare guess with actual age
    if guess == my_age:
        print("Correct! You guessed my age.")
    elif guess > my_age:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")

# Tutor Practice
# Create a variable named carname and assign the value Volvo to it.
# Step 3: Assign values to variables
carname = "Volvo"
age = 22
height = 1.75
city = "Paris"

# Step 4: Print the variables
print(f"Car Name: {carname}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"City: {city}")


# Step 5: Use different methods to format the string
print("Car Name: {}, Age: {}, Height: {}, City: {}".format(carname, age, height, city))  # format()
print("Car Name: " + carname + ", Age: " + str(age) + ", Height: " + str(height) + ", City: " + city)  # Concatenation
print("Car Name:", carname, "Age:", age, "Height:", height, "City:", city)  # Comma-separated
print(f"Car Name: {carname}, Age: {age}, Height: {height}, City: {city}")  # f-string (modern)
print("Car Name: %s, Age: %d, Height: %.2f, City: %s" % (carname, age, height, city))  # % operator

# Step 6: Different ways to format strings
concat_1 = "Car: " + carname + " | City: " + city
concat_2 = "Car: {} | City: {}".format(carname, city)
concat_3 = f"Car: {carname} | City: {city}"

# Print concatenated strings
print(concat_1)
print(concat_2)
print(concat_3)

# Step 7: Convert variables to string, integer, float, and boolean

# 8. Use different methods to convert the variables to a string.
# Convert to string
str_age = str(age)
str_height = str(height)
print("String conversion:", str_age, str_height)

# 9. Use different methods to convert the variables to an integer.
# Convert to integer
int_height = int(height)  # Converts 1.75 to 1
print("Integer conversion:", int_height)

# 10. Use different methods to convert the variables to a float.
# Convert to float
float_age = float(age)  # Converts 22 to 22.0
print("Float conversion:", float_age)

# 11. Use different methods to convert the variables to a boolean.
# Convert to boolean
bool_age = bool(age)  # True because age is non-zero
bool_height = bool(height)  # True because height is non-zero
bool_city = bool(city)  # True because city is a non-empty string
print("Boolean conversion:", bool_age, bool_height, bool_city)

# 12. Use different methods to convert the variables to a list.
# Convert to list
list_city = list(city)  # Converts "Paris" -> ['P', 'a', 'r', 'i', 's']
print("List conversion:", list_city)
