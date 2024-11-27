l = [-9, 0, -9, 8, 21, -2, 1]

# --- use numpy ---
import numpy as np
l_arr = np.array(l)

n = sum(l_arr>0)
print(n)





# # --- tridictional method ---
# count = 0
# for i in l:
#     if i>0:
#         count += 1
# print(count)        