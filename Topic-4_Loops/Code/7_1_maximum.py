def get_maximum(l):
    maximum = l[0]
    for i in range(len(l)):
        if maximum < l[i]:
            maximum = l[i]
    return maximum        

l = [-1, -9, -6, -4]
m = get_maximum(l)
print(m)        
