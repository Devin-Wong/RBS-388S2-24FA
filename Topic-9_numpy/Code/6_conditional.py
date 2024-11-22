import numpy as np

data = [-1, 78, -92, 80, -93, 0]
arr = np.array(data)

rst = arr[arr<0]

print(rst)


