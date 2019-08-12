# Example 1
if True:
    print("This is the first line of the block")
    print("This is the second line of the block")
    print("This is the third line of the block")
    
print("This is outsite of the if statement")


# Example 2
if False:
    print("This is the first line of the block")
    print("This is the second line of the block")
    print("This is the third line of the block")
    
print("This is outsite of the if statement")

# Example 3
if True:
    print("Before inner block")
    
    if False:
        print("Inner block executed")
        
    print("After inner block")

print("Outside of if statement")