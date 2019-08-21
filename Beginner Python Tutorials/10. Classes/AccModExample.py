# Define our class
class ExampleClass:
    number_of_inst = 0
    
    def __init__(self, val):
        self.var = val
        ExampleClass.number_of_inst += 1
     
# Create two objects
obj_one = ExampleClass(5)
obj_two = ExampleClass(10)

# See how many objects we have
print("Number of objects:", ExampleClass.number_of_inst)

# Change a variable within object one
obj_one.var = 200
print("Updated variable:", obj_one.var)

# Delete both objects
del obj_one
del obj_two

# Manually set the number_of_objs back to 0
ExampleClass.number_of_inst = 0
print("Number of objects:", ExampleClass.number_of_inst)


