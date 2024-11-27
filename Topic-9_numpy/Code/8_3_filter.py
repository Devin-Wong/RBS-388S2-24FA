import numpy as np

names = ['Jack', 'Mark', 'Mary', 'Jenny', 'April', 'Jin']
ages = [23, 18, 21, 19, 22, 19]

names_arr, ages_arr = np.array(names), np.array(ages)

names_older_20 = names_arr[ages_arr>20]
print(names_older_20)