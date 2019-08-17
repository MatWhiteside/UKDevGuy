"""
Function syntax:
    def <function_name>(<params>):
        Code block
        return <data>
"""
def add_numbers(num_one, num_two):
    return num_one + num_two

# Test our function
result = add_numbers(5, 6)
print(result)


"""
Function that uses default parameters.
"""
def welcome(name, blog="UKDevGuy"):
    print("Hey,", name, "! Welcome to", blog)
    
welcome("Matthew")
welcome("James", blog="a mystery blog")


"""
Example of returning multiple values.
"""
def return_three():
    var_one = 10
    var_two = 20
    var_three = 30
    return var_one, var_two, var_three

one, two, three = return_three()