l = [2, 3, 10, 17, 20]

# --- list comprehension ---
res = [i for i in l if i % 2 == 0]
print(res)

# # --- method 1: for loop --- 
# res = []
# for i in l:
#     if i % 2 == 0:
#         res.append(i)
# print(res)    
