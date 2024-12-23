# Looping Concepts
# start = Start
# stop = End
# step = Step



# Break and Continue
# break = Exit the loop and do not continue
# continue = Check the condition and skip the rest of the loop's statements



# 1 - While Loop


# Print numbers from 1 to 10

number = 1
while number <= 10:
    print(number)
    number = number + 1 
    # If this is not included, it will create an infinite loop
print("end")
# "end" is printed when the loop is finished




# Medicine Reminder

day = 1
while day <= 30:
    print("Day", day, "eat tablet")  
    # Reminder to take medicine for 30 days
    day += 1
print("END")






# While True Loop

while True: # This will run until we break out of it
          
    a = int(input("Enter a number (0 to exit): "))  # Prompt user for input
    if a == 0:
        break  # Exit the loop if input is 0

print("0") 
# Prints "0" when the loop is exited
