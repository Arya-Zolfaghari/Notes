# zip(*iterables) =     aggregate elements from 2 or more iterables (list , tuple , sets , etc.)
#                       creates a zip object with paired elements stored in tuples for each element


usernames = ["Dude", "Bro", "Mister"]
passwords = {"password", "abc123", "gust"}

users = zip(usernames, passwords)

print(type(users))
# Output :
# <class 'zip'>

for i in users:
    print(i)

# Output :
# ('Dude', 'password')
# ('Bro', 'abc123')
# ('Mister', 'gust')


users = list(zip(usernames, passwords))
print(users)
# Output:
# [('Dude', 'password'), ('Bro', 'abc123'), ('Mister', 'gust')]



users = dict(zip(usernames, passwords))

for key,value in users.items():
    print(key, value)

# Output:
# Dude password
# Bro abc123
# Mister gust



print("\n \n \n \n")
#______________________________________________________________

usernames = ["Dude", "Bro", "Mister"]
passwords = {"password", "abc123", "gust"}

login_date = ["1/1/2024","1/2/2024","1/3/2024","1/4/2024","1/5/2024"]


users = zip(usernames, passwords, login_date)


for i in users:
    print(i)

# Output :
# ('Dude', 'gust', '1/1/2024')
# ('Bro', 'password', '1/2/2024')
# ('Mister', 'abc123', '1/3/2024')


















