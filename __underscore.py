# _

for_ = "for"
# no eror

# for = "arya"
# eror


_name = "amir"  # protected

__name = "ali"  # privete





class Person:
          def __init__(self):
                  self.a = 7 # puublic
                  
                  self._b = 15 # protected
                  # you can use _b just in this class and the classes thet use it 
                  
                  
                  self.__c = 18 # privete
                  # we can use it in just this class
                  
p1 = Person()
print(p1.__c)  # Eror

print(p1._b) # no Eror but wrong

print(p1.a) # no eror and correct



#  (((((((((((((((((((((((((((((((((((((((((((((((((())))))))))))))))))))))))))))))))))))))))))))))))))

# getter & setter

class Person:
    def __init__(self):
        self.a = 7
        self._b = 15
        self.__age = 20
        
        
    def get_age(self):
        return self.__age


    def set_age(self , value):
        self.__age = value
p1 = Person()
a = p1.get_age()
p1.set_age(12)
a = p1.get_age()
print(a)






class Person:
    def __init__(self):
        self.a = 7
        self._b = 15
        self.__age = 20
        
        
    def get_age(self):
        return self.__age


    def set_age(self , value):
        self.__age = value
        
        
    def delete(self):
        del self.__age
    age = property(get_age , set_age , delete)
        
        

# BETTER :




class Person:
    def __init__(self):
        self.a = 7
        self._b = 15
        self.__age = 20
        
        
        
        
    @property
    def age(self):
        return self.__age

    @age.setter
    def set_age(self , value):
        self.__age = value
        
    @age.dleter
    def delete(self):
        del self.__age
        
p1 = Person()
print(p1.get_age)
        
        
        
        
        
        
        
        