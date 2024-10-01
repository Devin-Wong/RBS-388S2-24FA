l = [20, 30, 15, 25, 45, 50, 20]

s = 0
for i in range(len(l)):
    s += l[i]
    
    if s>100:
        break

    print(l[i])