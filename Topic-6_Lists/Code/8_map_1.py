def square(l):
    res = []
    for i in range(len(l)):
        squared_value = l[i]**2
        res.append(squared_value)
    return res    

l = [1, 2, 5]
squared_list = square(l)

print(squared_list)