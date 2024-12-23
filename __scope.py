def test():
          x = 200
          print(x)
          
# print(x)  # ==>  Eror


def test():
          x = 200
          def myfunc():
                    b = 70
                    print(x)
                    
          # print(b) # ==> Eror
                    
# if we make a var in a function it just work at the child of the function
# and it will'nt work at the parent block             
test()


#  (((((((((((((((((((((((((((((((((((((())))))))))))))))))))))))))))))))))))))

# global variables

x = 500

def test():
          x = 700
          print(x)
          
test() # ==> 700
print(x) # ==> 500





# (((((((((((((((((((())))))))))))))))))))'

def test():
          global x
          x = 200
          # we can use it out of the func
          
test() #  it shold call before using the [ x ]
print(x)