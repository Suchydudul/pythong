import json
import csv

file_path1 = "output.txt"
file_path2 = "output.json"
file_path3 = "employess.csv"

with open(file_path1, "r") as file:
    print(file.read())

with open(file_path2, "r") as file:
    content = json.load(file)
    print(content["job"])

with open(file_path3, "r") as file:
    content = csv.reader(file)
    for line in content:
        print(line[0])