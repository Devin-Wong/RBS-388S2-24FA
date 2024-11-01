def fun(n):
    if n<=0: 
        print('end')
    else:
        print(n) 
        fun(n-1)

fun(4)