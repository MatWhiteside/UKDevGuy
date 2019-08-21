# Define our class
class a:
    static_var = 1
    
    def __init__(self):
        self.non_static_var = 5
    
# Create two objects of our class
class_one = a()
class_two = a()


# If we change non_static_var of class_one,
# it won't affect class_two
print("Before:", class_two.non_static_var)
class_one.non_static_var = 999
print("After:", class_two.non_static_var)


# If we change the static_var it will affect
# both objects as it belongs to the class, not
# the object
print("Before:", class_two.static_var)
a.static_var = 999
print("After:", class_two.static_var)