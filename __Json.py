import json 



# json
try:
          x = {
                    "name" : "arya",
                    "age" : 12,
                    "ismarried" : ".",   #false = . ,
                    "isteacher" : ".",   #true = . ,
                    "lastname" : "."      #null = .
                    

          }
except:
          print("Eror")


# dictionary
try:
          x = {
                    "name" : "arya",
                    "age" : 12,
                    "ismarried" : False ,
                    "isteacher" : True ,
                    "lastname" : None
                    
          }
except:
          print("Eror")



#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ =================================

#                         Pars json
#                  conver from json to python
  
  
  
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x) # switch the str(x) to dict(x)
# If you have a JSON string, you can parse it by using the json.loads() method.

# the result is a Python dictionary:
print(y["age"])


#  ((((((((((((((((((((((((((((((((((((((()))))))))))))))))))))))))))))))))))))))


# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x) # switch the dict(x) to str(x)
# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method

# the result is a JSON string:
print(y)



###################################################################################

# You can convert Python objects of the following types, into JSON strings:
dict
list
tuple
str
int
float
True
False
None

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))



# dict => Object
# list => Array 
# tuple => Array
# str => String
# int => Number
# float => Number
# True => true
# False => false
# None => null


# ==================================================================================
# Example:
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))




# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

