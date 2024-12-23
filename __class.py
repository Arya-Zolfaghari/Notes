# Define a simple class with a property

class MyClass:
    x = 5  # Class-level property (shared by all instances)

# Create an object of MyClass
p1 = MyClass()
print(p1.x)  # Access the class-level property, output ==> 5

# Define a class with an __init__ method for initializing object attributes
class Person:
    def __init__(self):  # The __init__ method initializes object properties
        self.name = "amir"  # Instance-level property for name
        self.lastname = "amiri"  # Instance-level property for last name

# Create an object of Person
a1 = Person()  # a1.name ==> "amir", a1.lastname ==> "amiri"

#####################################################################

# Define a class with parameters in __init__
class Adam:
    def __init__(self, name, lname):  # Initialize with two parameters
        self.myname = name  # Assign the value of 'name' to instance property 'myname'
        self.mylname = lname  # Assign the value of 'lname' to instance property 'mylname'

# Create an object of Adam with specific values
a11 = Adam("Arya", "Zolfaghari")
print(a11.myname)  # Output ==> Arya
print(a11.mylname)  # Output ==> Zolfaghari

######################################################################

# Define a class with calculations in __init__
class Mosbat:
    def __init__(self, fnum, snum):  # Accept two numbers
        self.num = fnum + snum  # Perform addition and assign result to 'num'

# Create an object with specific values
o1 = Mosbat(7, 7)
print(o1.num)  # Output ==> 14

######################################################################

# Define a class with methods for calculations
class Method:
    def __init__(self, n1, n2):  # Initialize with two numbers
        self.n1 = n1
        self.n2 = n2

    def menha(self):  # Method to perform subtraction
        print(self.n1 - self.n2)

    def jama(self):  # Method to perform addition
        print(f"{self.n1 + self.n2}")

# Create an object and call its methods
o2 = Method(12, 8)
o2.menha()  # Output ==> 4
o2.jama()  # Output ==> 20

######################################################################

# Define a class with a method for printing a full name
class Person:
    def __init__(self, name, lname, age):  # Initialize with name, last name, and age
        self.name = name
        self.lname = lname
        self.age = age

    def fullname(self):  # Method to print full details
        print(f"My name is {self.name} {self.lname} and I am {self.age} years old")

# Create an object and use the method
i1 = Person("Arya", "Zolfaghari", 12)
print(i1.fullname())

# Update properties of the object
i1.name = "Mahdi"  # Change the name to "Mahdi"
i1.lname = "Alavi"  # Change the last name to "Alavi"

# Delete a property of the object
del i1.age  # Remove the 'age' property

######################################################################
#                       Inheritance
######################################################################

# Define a parent class and child classes (Inheritance)
class Person:  # Parent class
    def __init__(self, fname, lname):  # Initialize with first and last names
        self.fname = fname
        self.lname = lname

    def printname(self):  # Method to print the full name
        print(self.fname, self.lname)

class Students(Person):  # Child class inheriting from Person
    def __init__(self, fname, lname, age):
        Person.__init__(self, fname, lname)  # Call the parent class's __init__
        self.age = age  # Add an additional property for age

class Arya(Students):  # Another child class inheriting from Students
    def drink(self):  # Define a specific method
        print("Arya is drinking")

# Create objects of child classes
s1 = Students("Arash", "Kashfi", 12)
s1.printname()  # Output the full name

arya = Arya("Arya", "Zolfaghari", 12)
arya.printname()  # Output the full name from the inherited method

######################################################################
#                       super()
######################################################################

# Using super() to call the parent class's methods
class Person:  # Parent class
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):  # Method to print the full name
        print(self.fname, self.lname)

class Students(Person):  # Child class
    def __init__(self, fname, lname, age):
        super().__init__(fname, lname)  # Use super() to call the parent's __init__
        # for name , it use the parents name
        self.age = age  # Add an age property

    def printage(self):  # Method to print the full details
        print(self.fname, self.lname, self.age)

# Create an object of Students
s1 = Students("Arash", "Kashfi", 12)
s1.printage()  # Output ==> Arash Kashfi 12



# Final Conclusion:
# - Classes allow structured organization of code by grouping related properties and methods.
# - Object-oriented programming (OOP) concepts like encapsulation, inheritance, and polymorphism
#   make code more reusable and maintainable.
# - Using `__init__`, inheritance, and


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Anisa


class Person1 :
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def drink(self):
        print(self.fname, "drinking")

    def eat(self):
        print(self.fname, "eating")

    def talk(self):
        print(self.fname, "talking")

arya1= Person1("Arya", "Zolfaghari")


# polymorphism


class Shape:
    
    def __init__(self,kind,name):
        self.kind = kind
        self.name = name
        
    def area(self):
        raise NotImplementedError("All students should redefine the area method")
    
    def env(self):
        raise NotImplementedError("All students should redefine the area method")

    


class Squer(Shape):
    
    def __init__(self, kind, name, width):
        super().__init__(kind, name)
        self.width = width
        
        
        
        def area(self):
            return self.width **2 
        
        def env(self):
            return self.width * 4
        
        
class Regtengle(Shape):
    
    def __init__(self, kind, name,width,height):
        super().__init__(kind, name)
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def env(self):
        return (self.width + self.height) *2
    
    
class Circle(Shape):
    def __init__(self, kind, name,radius):
        super().__init__(kind, name)
        self.radius = radius
        
    def area(self):
        return 3.14*self.radius**2
    
    def env(self):
        return self.radius*2*3.14
    

shape = Shape("shape","a")
shape.area()# eror

# we cant ake a object of Shape because its a parent 
# but we can use the childes of this parent class

squer = Squer("squer","a1",20)
print(squer.area())
print(squer.env())

reg = Regtengle("rectengle","a2",10,20)
print(reg.area())
print(reg.env())

# the child class can inhertanc of the parent class but we can't use the object of the parent class


circle = Circle("circla","a3",5)
print(circle.area())
print(circle.env)



