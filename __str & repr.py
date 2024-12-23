# str :

s = 'Hello, Geeks.'
print (str(s))
print (str(2.0/11.0))

# Otput :
# Hallo, Geeks.
# 0,181818181818

# {{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}

# repr :
s = 'Hello, Geeks.'
print (repr(s))
print (repr(2.0/11.0))

# Output :
# „Hallo, Geeks.“
# 0,18181818181818182


#################################################################
# diffrents :
# repr has the "" or '' in the text but str does'nt
# repr has the longer and exactly number but str has simpler and notexactly number

# str is for users
# repr is for programmers

# [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]

# Python program to demonstrate writing of __repr__ and
# __str__ for user defined classes
 
# A user defined class to represent Complex numbers
class Complex:
 
    # Constructor
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
 
    # For call to repr(). Prints object's information
    def __repr__(self):
        return 'Rational(%s, %s)' % (self.real, self.imag)    
 
    # For call to str(). Prints readable form
    def __str__(self):
        return '%s + i%s' % (self.real, self.imag)    
 
 
# Driver program to test above
t = Complex(10, 20)
 
# Same as "print t"
print (str(t)) # => 10 + i20
print (repr(t)) # => Rational(10, 20)



