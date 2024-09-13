def outerfun(a, b):
    square = a ** 2
    # inner function
    def addition(a, b):
        return a + b
    
    add = addition(a, b)
    return add + 5

result = outerfun(5, 10)
print(result)