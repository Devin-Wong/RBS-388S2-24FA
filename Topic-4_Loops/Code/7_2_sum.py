def main():
    n = get_number()
    s = get_sum(n)
    print(f"sum of 1:{n} is {s}.")

# try to get a positive number
def get_number():
    while True:
        n = int(input('Please input a positive number: '))
        if n>0: 
            break
    return n

# calculate sum of 1 to n
def get_sum(n):
    s = 0
    for i in range(1,n+1):
        s += i
    return s

main()













# def get_number_3():
#     while True:
#         n = int(input('Please input a positive number: '))
#         if n>0: 
#             return n

# def get_number_2():
#     n = int(input('Please input a positive number: '))
#     while n<=0:
#         n = int(input('Please input a positive number: '))
#     return n