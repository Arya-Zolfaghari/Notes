     

#####################################################


class Myiter :
          def __iter__(self): # it do the iter() function
            self.a = 1  # its the number that my iter will start with
            return self
  
  
          def __next__(self): # it do the next() function
                    x = self.a
                    self.a += 1   # its the number that it will plus after next()
                    return x
          
          
o1 = Myiter() # make an object 

myiter = iter(o1)

print(next(myiter)) # 1
print(next(myiter)) # 2
print(next(myiter)) # 3
print(next(myiter)) # 4
print(next(myiter)) # 5
print(next(myiter)) # 6
print(next(myiter)) # 7


# better
for n in o1 :
          print(n)
          
          
          
          

