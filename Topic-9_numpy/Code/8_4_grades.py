import numpy as np

homework = [81, 83, 89, 98, 70, 71, 72, 91, 80, 61, 50]
project = [90, 92, 85, 82, 84, 86, 83, 79, 70, 81, 60]
exam_1 = [83, 70, 78, 90, 82, 88, 68, 59, 59, 75, 77]
exam_2 = [82, 73, 60, 65, 95, 88, 68, 59, 62, 75, 50]

hw_arr, prjt_arr = np.array(homework), np.array(project)
ex1_arr, ex2_arr = np.array(exam_1), np.array(exam_2)

final = 0.20 * hw_arr + 0.2 * prjt_arr + 0.3 * ex1_arr + 0.3 * ex2_arr

a_prec = sum(final>=90)/len(final)
b_prec = sum((final>=80) * 1 * (final<90))/len(final)
c_prec = sum((final>=70) * 1 * (final<80))/len(final)
d_prec = sum((final>=60) * 1 * (final<70))/len(final)
f_prec = sum(final<60)/len(final)

print(final)
print(a_prec, b_prec, c_prec, d_prec, f_prec)