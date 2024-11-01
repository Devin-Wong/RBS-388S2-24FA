def calculation(a, b, c):
    d = add(a, b) * c
    return d

def add(x, y):
    z = x + y
    return z

# __main__
rst = calculation(10, 5, 3) # (10 + 5) * 3
print(rst)