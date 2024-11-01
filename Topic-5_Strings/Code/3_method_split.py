# ask user to input name
# remove white spaces from the string
# Capitalize all letters of each word
name = input("Please input your first name and last name: ").strip().upper()

# split the name into two parts
x = name.split()

# print out first name and last name
print(f"First name: {x[0]}")
print(f"Last name: {x[1]}")