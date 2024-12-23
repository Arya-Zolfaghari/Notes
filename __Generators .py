# If the body of a def contains yield, the function automatically 
# becomes a Python generator function. 

# yield is sth like return but we can coding in the func after yield
# but in return if we have a code in that block => Eror

# yield will not save but return saved


# A generator function that yields 1 for first time,
# 2 second time and 3 third time
def simpleGeneratorFun():
    yield 1     
    yield 2            
    yield 3            
 
# Driver code to check above generator function
for value in simpleGeneratorFun(): 
    print(value)
    
    
# OR

x = simpleGeneratorFun() # iterator

print(next(x)) # 1
print(next(x)) # 2
print(next(x)) # 3


print(type(x)) # ===> generation




# [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]

# Fibonacci Numbers

def fib(limit):
    a, b = 0, 1
    while b < limit:
        yield a
        a = b
        b = a + b

# Create a generator object
x = fib(200)

# Iterate over the generator object and print each value
for i in x:
    print(i)










