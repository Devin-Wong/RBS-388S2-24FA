# --- read a file to obatin a list of numbers ------
import csv

file_path = "project-1.csv"

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


