import csv

employees = [["Name", "Age", "Job"],
           ["Adam", "30", "Cleaner"],
           ["Bob", "20", "Cook"],
           ["Celine", "43", "Manager"]]

file_path = "employess.csv"

with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)
    for row in employees:
        writer.writerow(row)
    print(f"CSV file {file_path} was created")