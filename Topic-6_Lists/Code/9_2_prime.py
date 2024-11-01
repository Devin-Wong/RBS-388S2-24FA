def prime(n): # n is a non-negative int.
    if n<2:
        return False
    
    sqrt = int(n**0.5)
    for i in range(2,sqrt+1):
        if n%i==0:
            return False
    
    return True

l = [2, 3, 10, 17, 20]

res = list(filter(prime, l))
print(res)