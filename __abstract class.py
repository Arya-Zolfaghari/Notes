from abc import ABC, abstractmethod, abstractproperty
# Import modules for abstract classes


# Define an abstract class
class Animal(ABC):  # Inherit from ABC to make this an abstract class

    @abstractmethod  # Declare move as an abstract method
    def move(self):  # This method must be implemented in any subclass
        pass

    @abstractproperty  # Declare legs as an abstract property
    def legs(self):  # This property must be implemented in any subclass
        pass


# Define a concrete subclass of Animal
class Lion(Animal):  # Lion inherits from Animal
    def move(self):  # Implement the abstract method move
        print("lion is moving")  # Specific behavior for Lion

    @property  # Implement the abstract property legs as a read-only property
    def legs(self):
        return 8  # Return the number of legs for Lion (intentionally wrong for demonstration)


# Define another concrete subclass of Animal
class Dog(Animal):  # Dog inherits from Animal
    def move(self):  # Implement the abstract method move
        print("dog is moving")  # Specific behavior for Dog

    @property  # Implement the abstract property legs as a read-only property
    def legs(self):
        return 2  # Return the number of legs for Dog


# Instantiate objects of the concrete classes
l1 = Lion()  # Create a Lion object
d1 = Dog()  # Create a Dog object

# Call methods and access properties of the objects
l1.move()  # Output => "lion is moving"
d1.move()  # Output => "dog is moving"

print(l1.legs)  # Output => 8 (value from Lion class)
print(d1.legs)  # Output => 2 (value from Dog class)
