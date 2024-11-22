def get_minimum(l):
    minimum = l[0]
    for i in range(len(l)):
        if minimum > l[i]:
            minimum = l[i]
    return minimum        

l = [3, 2, -3, 10]
rst = []
for i in range(len(l)):
    m = get_minimum(l)
    rst.append(m)
    l.remove(m)

print(rst)