# Uppercase and lowercase
my_str = "UPPER AnD lower"
print(my_str.upper())
print(my_str.lower())

# Split
my_str = "This is a test string!"
print(my_str.split())
print(my_str.split("t"))
print(my_str.split("t", 1))

# Join
my_list = ["We", "want", "to", "join", "this!"]
print(" ".join(my_list))
print("SPACER".join(my_list))

# Strip
my_str = "    lots of white space!    "
print(my_str.strip())
print(my_str.strip("! "))

# Replace
my_str = "This is my rubbish string"
print(my_str.replace("rubbish", "amazing"))
print(my_str.replace("rubbish ", ""))