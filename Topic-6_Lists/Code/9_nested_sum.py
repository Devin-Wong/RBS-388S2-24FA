def nested_sum(t):
    s = 0
    for i in t:
        for j in i:
            s += j
    return s

t = [[1, 2, 3], [5, 6, 7], [9, 10, 23]]
print(nested_sum(t))