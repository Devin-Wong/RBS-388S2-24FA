# def get_quotient(x, y):
#     return x//y

# def get_remainder(x, y):
#     return x%y

def get_quotient_remainder(x, y):
    return x//y, x%y

x, y = 10, 3
quot, rem = get_quotient_remainder(x, y)

print(quot)
print(rem)