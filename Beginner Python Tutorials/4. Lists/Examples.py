# Create a basic list
my_list = ["Item 1", 42, "Hello!"]

# Use list comprehension to get all even numbers
# out of a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [n for n in numbers if n%2 == 0]
print(even_numbers)

# Example of accessing list elements
access_list = ["Element 1", "Element 2", "Element 3", "Element 4"]
print("Access the first element of list: ", access_list[0])
print("Access the second element of list: ", access_list[1])
print("Access the last element of list using minus: ", access_list[-1])
print("Access the second to last element of list using minus: ", access_list[-2])

# Example of inserting elements into a list
insertion_list = ["Element 1", "Element 2", "Element 4"]
insertion_list.insert(0, "Element 0")
insertion_list.insert(3, "Element 3")
print(insertion_list)

# Example of appeneding element to the end of a list
append_list = ["Element 1", "Element 2", "Element 3", "Element 4"]
append_list.append("Element 5")
print(append_list)

# Example of using the del keyword
remove_list = [34, 12, 65, 777, 44, 34, 234, 767]
del remove_list[1]
print(remove_list)

# Example of using the remove function
remove_list_two = [34, 12, 65, 777, 44, 34, 234, 767]
remove_list_two.remove(777)
print(remove_list_two)

# Example of modifying an element of a list
modify_list = [1, 2, 3]
modify_list[0] = 42
print(modify_list)

# List slicing examples
slicing_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Slice list between elements 2 and 4
print("slicing_list[2:4]: ", slicing_list[2:4])
# Slice whole list up to the 4th index
print("slicing_list[:4]:  ", slicing_list[:4])
# Slice whole list from the 4th index to the end
print("slicing_list[4:]:  ", slicing_list[4:])
# Take every other element of the list
print("slicing_list[::2]: ", slicing_list[::2])
# Reverse the list
print("slicing_list[::-1]:", slicing_list[::-1])

# Clear example
clear_list = [1, 2, 3]
clear_list.clear()
print(clear_list)

# Count example
count_list = [1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 4]
print(count_list.count(1))

# Len example
len_list = [1,2,3]
print(len(len_list))