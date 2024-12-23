# Comparative Operators
# These operators are used to compare values.


# Equality and Inequality
# a == b    : True if a is equal to b
# a != b    : True if a is not equal to b



# Comparison
# a < b     : True if a is less than b
# a > b     : True if a is greater than b
# a <= b    : True if a is less than or equal to b
# a >= b    : True if a is greater than or equal to b



# Additional Operators
# % = modulus operator (returns the remainder of division)
# // = floor division operator (returns the quotient without the remainder)




# Example of Modulus and Floor Division
a = 10
b = 3

remainder = a % b  # Remainder of 10 divided by 3, which is 1
quotient = a // b  # Quotient of 10 divided by 3, which is 3

print("Remainder:", remainder)  # Output: Remainder: 1
print("Quotient:", quotient)      # Output: Quotient: 3

# Increment and Decrement Operators
# These are shorthand for updating variable values.

# Incrementing and Decrementing
a = 5

a += 1   # Equivalent to a = a + 1; Now a is 6
a -= 1   # Equivalent to a = a - 1; Now a is back to 5
a *= 2   # Equivalent to a = a * 2; Now a is 10
a /= 2   # Equivalent to a = a / 2; Now a is back to 5.0 (note that it becomes float)

print("Final value of a:", a)  # Output: Final value of a: 5.0