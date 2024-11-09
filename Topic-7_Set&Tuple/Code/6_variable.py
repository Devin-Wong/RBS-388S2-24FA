def square(x):
    return x**2
a = 2
square_value = square(a)

# --------------------
def square_list(x):
    # rst = []
    # for i in x:
    #     rst.append(i**2)
    # return rst 

    return [i**2 for i in x]
       
    
a = [2, 4, 10, 12]
square_value = square_list(a)
print(square_value)