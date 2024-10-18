def square(x):
    return x**2

l = [1, 2, 5]

squared_list = map(square,l)
squared_list = list(squared_list)
print(squared_list)