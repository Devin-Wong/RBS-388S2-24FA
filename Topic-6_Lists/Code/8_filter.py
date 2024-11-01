l = [-2, 0, -1, 10, 1]

# ---- use filter() -----
# def is_positive(x):
#     return x>0

positive_numbers = filter(lambda x: x>0, l)
positive_numbers = list(positive_numbers)
print(positive_numbers) 


# # --- old method -------
# res = []
# for i in range(len(l)):
#     if l[i]>0:
#         res.append(l[i])

# print(res)        