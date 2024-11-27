import numpy as np

homework = [81, 83, 89, 98, 70, 71, 72, 91, 80, 61, 50]
project = [90, 92, 85, 82, 84, 86, 83, 79, 70, 81, 60]
exam_1 = [83, 70, 78, 90, 82, 88, 68, 59, 59, 75, 77]
exam_2 = [82, 73, 60, 65, 95, 88, 68, 59, 62, 75, 50]

hw_arr, prjt_arr = np.array(homework), np.array(project)
ex1_arr, ex2_arr = np.array(exam_1), np.array(exam_2)

final = 0.20 * hw_arr + 0.2 * prjt_arr + 0.3 * ex1_arr + 0.3 * ex2_arr

def func_letter(x):
    if x>=90:
        return 'A'
    elif x>=80:
        return 'B'
    elif x>=70:
        return 'C'
    elif x>=60: 
        return 'D'
    else:
        return 'F'

grades = np.array(list(map(func_letter, final)))
print(grades)

a_prec = sum(grades == 'A')/len(grades) 

print(a_prec)
