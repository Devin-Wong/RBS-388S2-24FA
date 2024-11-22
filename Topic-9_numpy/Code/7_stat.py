import numpy as np

data = [-1, 78, -92, 80, -93, 0]
arr = np.array(data)

minimum = arr.min()
maximum = arr.max()
mean = arr.mean()
std = arr.std()

q1 = np.percentile(data, 25)
q2 = np.percentile(data, 50)
q3 = np.percentile(data, 75)

print(minimum, maximum, mean, std)
print(q1, q2, q3)
