my_str = "injected variable"
fstr_one = f"This is a string with an {my_str}"
fstr_two = f"This is a string with a modified {my_str.upper()}"

print(fstr_one)
print(fstr_two)