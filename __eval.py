# Using eval to evaluate expressions from strings


# Define variables as strings

a = "1"  # First number as a string

b = "2"  # Second number as a string

c = "+"  # Operator as a string



# Create an expression by concatenating the strings

d = a + c + b  # d becomes "1+2"



# Evaluate the expression and print the result

print(eval(d))  # Output: 3




# Note: eval works only with strings that represent valid Python expressions