# Sequence Data Types: str - list - tuple


# List and Tuple
# Lists are changeable (mutable) but tuples are unchangeable (immutable).
# Both are ordered collections.
# Both can contain repeatable values.
# Lists are defined with [] while tuples are defined with ().






# Creating a tuple
my_tuple = (1, 2, 3, 4, 5, 5)



# Print the tuple
print(my_tuple)  # Output: (1, 2, 3, 4, 5, 5)



# Check the type of my_tuple
print(type(my_tuple))  # Output: <type 'tuple'>



# Get the length of the tuple
print(len(my_tuple))  # Output: 6



# Creating a single-element tuple
teachers = ("mona",)
print(type(teachers))  # Output: <type 'tuple'>



# Accessing an element in the tuple
print(my_tuple[3])  # Output: 4 (indexing starts from 0)


# Attempting to update a tuple (this will raise an error)
# my_tuple[2] = 8  # This line would cause an error because tuples are immutable



# Converting a tuple to a list to modify it

temp_list = list(my_tuple)  # Convert tuple to list
temp_list[2] = 8             # Update the third element (index 2)
my_tuple = tuple(temp_list)   # Convert back to tuple


# Built-in functions for type conversion
# int(), float(), str(), list(), tuple()





our_tuple = (1, 2, 3, 4, 5, 5)

number = 4
for i in range(len(our_tuple)):
    if number in our_tuple:         # Check if number is in the tuple
        print(our_tuple[number])    # Print the value at index 'number'

# Concatenating two tuples
total = my_tuple + our_tuple
print(total)  # Output: Combined tuple of my_tuple and our_tuple