# Function Definition


def total():  # Define a function named 'total'
    
    # Get user input for two numbers
    
    num1 = int(input("Enter a number: "))  # Prompt user for the first number
    
    num2 = int(input("Enter a number: "))  # Prompt user for the second number
    
    # Calculate the sum of the two numbers
    
    sum = num1 + num2  
    
    # Print the result
    
    print("The sum is:", sum)



# Call the function to execute its code
total()  # This line runs the 'total' function







# OR







# Function Definition that Returns a Value

def total(num1, num2):  # Define a function that takes two parameters
          
    # Calculate the sum of the two numbers
    sum = num1 + num2
    return sum  # Return the sum tothe main



# Call the function and store the result in a variable
result = total(5, 10)  # This line runs the 'total' function and stores the returned value
#  num1 = 5       num2 = 10



# Print the result
print("The sum is:", result)