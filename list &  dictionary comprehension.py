# list comprehension   =    a way to create a new list with less syntax
#                           can mimic cartain lambda functions, easier to read
#                           list = [expression for item in iterable]
#                           list = [expression (if/else) for item in iterable]
#                           list = [expression for item in iterable if conditional]






squares = []                        # create an empty list
for i in range(1,11):               # create a for loop
    squares.append(i * 1)           # define what each loop iteration should do
print(squares)
# Output :
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



# with less syntax :



squers = [i*1 for i in range(1,11)]
print(squers)
# Output :
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


###################################################################




students = [100,90,80,70,60,50,40,30,0]


passed_students = list(filter(lambda x : x >= 60,students))
print(passed_students)
# Output :
# [100, 90, 80, 70, 60]


#                list = [expression for item in iterable if conditional]

passed_students = [i for i in students if i >= 60]
print(passed_students)
# Output:
# [100, 90, 80, 70, 60]



#                list = [expression (if/else) for item in iterable]


passed_students = [i if i >= 60 else "FAILED" for i in students ]
print(passed_students)
# Output:
# [100, 90, 80, 70, 60, 'FAILED', 'FAILED', 'FAILED', 'FAILED']

print("\n \n \n \n \n \n \n ")
#___________________________________________________________________________________________


# dictionary comprehension =         create dictionaries  using an expression
#                                     can replace for loops and certain lambda functions

#                   dictionary = {key: expression for (key,value) in iterable}
#                   dictionary = {key: expression for (key,value) in iterable if conditional}
#                   dictionary = {key: (if/else) for (key,value) in iterable}
#                   dictionary = {key: (if/else) for (key,value) in iterable}
#                   dictionary = {key: function() for (key,value) in iterable}





cities_in_f = {"New York":32, "Boston":75, 'Los Angles':100, "Chicago": 50}

cities_in_c ={key: round((value-32)*(5/9)) for (key,value) in cities_in_f.items()}
print(cities_in_c)
# Output :
# {'New York': 0, 'Boston': 24, 'Los Angles': 38, 'Chicago': 10}


##########################################################################################

weather = {"New York":"snowing" , "Boston" : "sunny", "Los Angles":"sunny", "Chicago":"cloudy"}

sunny_weather = {key:value for (key,value) in weather.items() if value == "sunny"}
print(sunny_weather)
# Output:
# {'Boston': 'sunny', 'Los Angles': 'sunny'}


#########################################################################################

cities = {"New York":32, "Boston":75, 'Los Angles':100, "Chicago": 50}

desc_cities = {key: ("WARm" if value >= 40 else "COLD") for (key,value) in cities.items()}
print(desc_cities)
# Output :
# {'New York': 'COLD', 'Boston': 'WARm', 'Los Angles': 'WARm', 'Chicago': 'WARm'}

#########################################################################################

def check_temp(value):
    if value >= 70:
        return "HOT"
    elif 69>=value >= 40:
        return "WARM"
    else:
        return "COLD"
cities = {"New York":32, "Boston":75, 'Los Angles':100, "Chicago": 50}


desc_cities = {key: check_temp(value) for (key,value) in cities.items()}
print(desc_cities)
# Output :
# {'New York': 'COLD', 'Boston': 'HOT', 'Los Angles': 'HOT', 'Chicago': 'WARM'}





















