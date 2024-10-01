def get_maximum(l):
    maximum = 0
    for i in range(len(l)):
        if maximum < l[i]:
            maximum = l[i]
    return maximum        

l = [1, 9, 6, 4]
m = get_maximum(l)
print(m)        
