
# Decorators are the functions that change the behavior of the function



def hello(name):
          def hello_name():
                    print(f"hello {name}")
                    
          return hello_name


new = hello("Reza") # we should type () 
# because we have return in our function



new() # ==> hello Reza



###########################################
# decorator
def hello_dec(func):
          
          
          # wrapper function
          def inner(name):
                    print("Hello")
                    func(name) #mits the func that we reseve ==> hi user
                    print("good bye")
                    

          return inner
@hello_dec
def hello(name):
          print(f"im {name}")
          
#      hello = hello_dec(hello) # inner  #  ==  @hello_dec

hello("Arya")



# call the main function in the function
# Outpot ==>
#         Hello
#         im user
#         good bye



#################################################################################


def upperdac(func):
          def inner(*args , **kwargs):
                    x = func(*args, **kwargs)
                    return x.upper()
          
          return inner
          
@upperdac
def test(name):
          return f"hello {name}"


x = test("arya")
print(x)


###############################################################################

# EXAMPLE :

# importing libraries
import time
import math

# decorator to calculate duration
# taken by any function.
def calculate_time(func):
    
    # added arguments inside the inner1,
    # if function takes any arguments,
    # can be added like this.
    def inner1(*args, **kwargs):

        # storing time before function execution
        begin = time.time()
        
        func(*args, **kwargs)

        # storing time after function execution
        end = time.time()
        print("Total time taken in : ",end - begin)

    return inner1

time.sleep

# this can be added to any function present,
# in this case to calculate a factorial
@calculate_time
def factorial(num):

    # sleep 2 seconds because it takes very less time
    # so that you can see the actual difference
    time.sleep(2)
    print(math.factorial(num))

# calling the function.
factorial(10)



