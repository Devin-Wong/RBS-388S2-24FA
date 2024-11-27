# --- read a file to obatin a list of numbers ------
import csv

file_path = "project-1.csv" # You may change the path to your own.

def read_file(file_path):
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        spy = []
        for row in csv_reader:
                spy.append(row[1])

    return list(map(float, spy)) 
    
spy = read_file(file_path)
# print(spy)
# ---------------------------------------------------

# A. Let's define a rising day as the day when the closing price is higher than the previous day.
# I: (3 pts) Try to obtain the number of rising days from 1/2/2024 through 6/28/2024. You need to print out the number of rising days.
def func_numrisingdays(l):
    n = 0
    for i in range(1,len(l)):
        if l[i] > l[i - 1]:
            n += 1
    return n

num_risingDays = func_numrisingdays(spy)
print(f"A-I:The number of rising days from 1/2/2024 through 6/28/2024: {num_risingDays}")

# II: (8 pts) How many days did the rise last at most?
def func_riselast(l):
    rising = 0
    max = 0
    for i in range(1, len(l)):
        if l[i] > l[i-1]:
            rising += 1
        else:
            if rising > max:
                max = rising
            rising = 0
    return max

days_riselast = func_riselast(spy)

print(f"A-II: The number of days the rise lasted at most: {days_riselast}")

# B-I. (5 pts) Try to calculate 5-day moving averages.
def func_MA(data, l):
    rst = []
    for i in range(l-1,len(data)):
        start = i - (l-1)
        end = i + 1
        ma = sum(data[start:end]) / l
        rst.append(ma)
    return rst

ma_5 = func_MA(spy, 5)
# print(ma_5)

# B-II. (3 pts) Obtain the number of rising days in the 5-day moving averages.
num_risingDays_ma5 = func_numrisingdays(ma_5)
print(f"B-II: The number of rising days in the 5-day moving averages: {num_risingDays_ma5}")

# III. (8 pts) How many days did the 5-day moving averages rise last at most?
days_riselast_ma5 = func_riselast(ma_5)
print(f"B-III: The days the 5-day moving averages rise lasted at most: {days_riselast_ma5}")

# IV. (5 pts) How many days were the SPY closing prices lower than the 5-day moving averages.
def fun_compare(l1, l2):
    count = 0 
    for i in range(len(l1)):
        if l1[i] < l2[i]:
            count += 1
    return count

num_lower = fun_compare(spy[4:], ma_5)
# num_lower = fun_compare(spy[:-4], ma_5)

print(f"The days the SPY closing prices were lower than the 5-day moving averages: {num_lower}")

