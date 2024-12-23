# numeric        int,flout
# boolean        True/False
# sequence       str,tuple,list
# dictiunary     
# set





# colection  ->  Array :  -> have index
########################################################################
# str
# list              changeble , ordred , allows duplicate    [ $ , $ , $]
# tuple             unchangeble , ordred , allows duplicate  ( $ , $ , $)
# set               unordred / unidexed / unchangeable / not allow duplicate   { $ , $ , $}

######
# dictiunary        changeble , ordred , no allows duplicate   { $ : $, $ : $ , $ : $}
# dictiunary => dict 






# dictiunary = { key: value , key1 : value1,  : value}

students={
            "name": "Arya",
            "family": "zolfaghari",
            "age": 12 , 
            "status":True 
          
}


#############################################

# access  => دسترسی
# key  -  value 





#  1.
print(students["name"])   # output     ==> Arya
          #print the value of the *name*
          
       
          
# 2.
print(students.get("age"))
          #print the value of the *name*



# 3.
print(students.keys())   # ==> list of key
print(students.values())   # ==> list of value



# 4.
print(students.items())  # ==>   list(tuple,tuple)
          # all thing in students


# check if a key exist in dict
if "name" in students:
          print(students["name"])
else:
          print("the key does not exist")


########################################################




# change

# 1.
students["family"] = "asghari"
print(students["family"])



# 2.
students.update({"family": "asghari"})
print(students["family"])


###################################################


# add



# 1.
students["level"] = 7
          # add Level in my dict

# 2.
students.update({"level":12})






#############################################################


# remove



# 1.     .pop(key)
students.pop("name")
# delete the key from dict



# 2.     .popitem()
students.popitem()
# delete the last one


# 3.      del
del students["name"]
# delete name in the dict


# 4.     .clear
students.clear()
# clear the dict but we have that in memory



# 5.    del
del students
# delete the all dict and it will not be in the memori







####################################################################


# coppy



# 1.      .coppy
new_students = students.copy()
print(new_students)







# 2. dict()

new_students2 = dict(students)
print(new_students2)



##################################################

# loop

statesAndCapitals = {
    'Gujarat': 'Gandhinagar',
    'Maharashtra': 'Mumbai',
    'Rajasthan': 'Jaipur',
    'Bihar': 'Patna'
}
print('List Of given states:\n')

# Iterating over keys
for state in statesAndCapitals:
    print(state)
# it will just show the keys


# (((((((((((((((((((((((((((())))))))))))))))))))))))))))
statesAndCapitals = {
    'Gujarat': 'Gandhinagar',
    'Maharashtra': 'Mumbai',
    'Rajasthan': 'Jaipur',
    'Bihar': 'Patna'
}
map_keys = map(statesAndCapitals.get, statesAndCapitals)
for key in map_keys:
    print(key)

# ((((((((((((((((((((((((((((()))))))))))))))))))))))))))))


statesAndCapitals = {
    'Gujarat': 'Gandhinagar',
    'Maharashtra': 'Mumbai',
    'Rajasthan': 'Jaipur',
    'Bihar': 'Patna'
}
print('List Of given states:\n')

# Iterating over keys
for state in statesAndCapitals.values():
    print(state)
# it will just show the values





################################
# nested dict


#  dict in dict


cars={
          "car1":{
                    "name":"207",
                    "company" : "peugeot",
                    "color" : "black",
                    "speed":200
          },
          "car2":{
                    "name":"206",
                    "company" : "peugeot",
                    "color" : "black",
                    "speed":220
          },
          "car3":{
                    "name":"2008",
                    "company" : "peugeot",
                    "color" : "black",
                    "speed":300
          }
                    
}



#  access to nested dict

print(cars["car1"]["name"])
# outpot ==> 207




# (((((((((((((((((((((((((())))))))))))))))))))))))))

# list of dict

# create a list of dictionaries with 
# student id as key and name as value
data = [{7058: 'sravan', 7059: 'jyothika', 
         7072: 'harsha', 7075: 'deepika'},
         
        {7051: 'fathima', 7089: 'mounika', 
         7012: 'thanmai', 7115: 'vasavi'},
         
        {9001: 'ojaswi', 1289: 'daksha', 
         7045: 'parvathi', 9815: 'bhavani'}]
 
print(type(data)) # ==> list
print(data[1][7051])
# outpot = fathima



# ((((((((((((((((((((((((((((()))))))))))))))))))))))))))))
# speradet nested dict

a = {'a': "b", 'b' : 'c', 'c' : 'd'}
b = {'a': "b", 'b' : 'c', 'c' : 'd'}
c = {'a': "b", 'b' : 'c', 'c' : 'd'}

alldict = {
          "a" : a,
          "b" : b,
          "c" : c
}



