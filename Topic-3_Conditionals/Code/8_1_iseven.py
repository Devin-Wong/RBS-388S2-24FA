def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False

n = 3
if is_even(n):
    print(f"{n} is an even number.")           
else:
    print(f"{n} is an odd number.")    