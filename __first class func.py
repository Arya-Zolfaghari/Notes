# first class function 

# the func is an instance of the Object type
# we can save them in a variable
# we can send the func as a prometr to another func
# fe can return the func from the function
# You can store them in data structures such as tables, lists, …



# Python program to illustrate functions 
# can be treated as objects 
def shout(test): 
    return test.upper() 
  
print (shout('Hello')) 
  
yell = shout 
  
print (yell('Hello'))


# so we can rename the func with saving in the variable







def test1(text) : 
          print(text , " !!!!!!!")


def test2(number):
          print(number*2 , " is my number !!!!!")
          
c = test2
b = test1
b("ali ab dad")
a = test2
a(12)

