"""
While loop syntax is as follows:
while <condition>:
    Code block
    
Example of an infinite loop...
while True:
    print("Hello")
"""

# Example while loop
list_of_numbers = []

while len(list_of_numbers) < 5:
    user_input = input("Add a number: ")
    list_of_numbers.append(user_input)
   
   
"""
For loops have the following syntax:
for <var> in <sequence>:
    Code block
    
We can then use the <var> variable within our code block
to access the elements of the sequence.
"""
# Example of looping through a list
my_list = [5, 2, 10, 12]
for elem in my_list:
    print(elem)

# Example of iterating over even numbers
for num in range(0, 11, 2):
    print(num)
    
    
"""
Examples of using break
"""
# Basic example
while True:
    print("Oh no this loop might run forever!")
    break

print("Few, it's ok!")

# Example using nexted loops
for outer in range(0, 10):
    for inner in range(0, 5):
        print("Inner")
        break
    print("Outer")
    break

"""
Example of using continue
"""
num = 1
while num < 5:
    print("My number is:", num)
    num += 1
    continue
    print("I don't want this line to run...")
    
    
# Be careful... This could look unclear!
num = 1
while num < 5:
    print(num)
    num += 1
    break