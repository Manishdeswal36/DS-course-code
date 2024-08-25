#  OOP
## object 
## class digram
## function vs method
## Bank demo
## Constructor --> magic method
## self
## Class
- Blueprint for creating objects

### Constructor
- whenever you make variables they are inside Consructor

### Attributes (Data)
- Definition: Variables that store information about the object
- Examples: `color`, `make`, `model`, `year` for a `Car` class
- Purpose: Define the state of the object
- Synonyms: Properties, data, variables

### Methods (Behavior)
- Definition: Functions that describe the actions or operations an object can perform
- Examples: `drive()`, `brake()`, `honk()` for a `Car` class
- Purpose: Define what actions the object can perform
- Synonyms: Functions, behaviors, actions

### Code Example
```python
class Car:
    # Attributes
    def __init__(self, color, make, model, year):
        self.color = color
        self.make = make
        self.model = model
        self.year = year
    
    # Methods
    def drive(self):
        print(f"The {self.color} {self.make} {self.model} is driving.")

    def brake(self):
        print(f"The {self.color} {self.make} {self.model} is braking.")

    def honk(self):
        print("Honk! Honk!")

# Create an object (instance) of the Car class
my_car = Car("red", "Toyota", "Corolla", 2020)

# Access attributes
print(my_car.color)  # Output: red

# Call methods
my_car.drive()  # Output: The red Toyota Corolla is driving.
my_car.brake()  # Output: The red Toyota Corolla is braking.
my_car.honk()   # Output: Honk! Honk!

#