l = [-2, 0, -1, 10, 1]

# # --- old method -------
# res = []
# for i in range(len(l)):
#     if l[i]>0:
#         res.append(l[i])

res = [i for i in l if i>0]
print(res)        