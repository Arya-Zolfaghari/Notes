# Lambda Functions





# Characteristics of lambda functions:

# - Anonymous: No name is assigned to the function.

# - One line: Defined in a single line.

# - No return statement: The expression is returned implicitly.

# - Unlimited arguments: Can take any number of arguments but only one expression.


# Syntax: lambda arguments: expression



# Example of a regular function
def calculate(a, b):
    print(a + b)  # Prints the sum of a and b



# Function to get user input and call calculate
def number():
    a = int(input("Enter first number: "))  # Get first number from user
    b = int(input("Enter second number: "))  # Get second number from user
    calculate(a, b)  # Call the calculate function with user inputs



# Alternative way to define a function that returns the sum
# def number(a, b):
#     sum = a + b 
#     return sum


# Lambda function to calculate the sum of two numbers
total = lambda a, b: a + b  
# This lambda function takes two arguments and returns their sum



# Example usage of the lambda function
result = total(5, 10)  
# Call the lambda function with arguments 5 and 10

print("The total is:", result)  # Print the result