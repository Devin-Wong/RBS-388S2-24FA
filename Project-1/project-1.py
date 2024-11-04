# --- read a file to obatin a list of numbers ------
import csv
file_path = "project-1.csv"
with open(file_path, mode='r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    print("Header:", header)
    spy = []
    for row in csv_reader:
            print(row)
            spy.append(row[1])

spy = list(map(float, spy))     
# ---------------------------------------------------


