import numpy as np

l1 = [1, 2, 3]
l2 = [10, 20, 30]

l1_arr, l2_arr = np.array(l1), np.array(l2)

rst = l1_arr * l2_arr
print(rst)


# rst = [l1[i]+l2[i] for i in range(len(l1))]
# # rst = []
# # for i in range(len(l1)):
# #     rst.append(l1[i] + l2[i])

# print(rst)