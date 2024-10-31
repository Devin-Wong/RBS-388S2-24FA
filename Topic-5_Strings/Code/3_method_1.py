# ask user to input name
name = input("Please input your name: ")

# remove white spaces from the string
name = name.strip()

# Capitalize the first letter of each word
name = name.title()

# print out 
print(f"Hello, {name}!")