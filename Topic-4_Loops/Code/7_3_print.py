def printEvenValues(x):
    for i in range(len(x)):
        if i%2==0:
            continue

        print(x[i])

x = ['a', 'b', 'c', 'd', 1, 23, 388]
printEvenValues(x)        