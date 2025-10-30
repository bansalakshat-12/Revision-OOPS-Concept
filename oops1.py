# Initiate a class
class Employee:
    # Constructor (special method that runs automatically when object is created)
    def __init__(self):
        print("Started executing Data/Attribute")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("Attributes/Data have been initiated")
        
    # Method (function defined inside the class)
    def travel(self, destination):
        print("This travel method was called manually")
        print(f"Employee is travelling to {destination}")
        
        
# Create an object of the class (this automatically calls the constructor)
sam = Employee()

# Calling a method manually using the object
#sam.travel("Aligarh")

# Printing an attribute
# print(sam.salary)

print(type(sam))