import json
employee = {
    "name": "adam",
    "age": "30",
    "job": "cook"

}

file_path = "output.json"

try: 
    with open (file_path, "w") as file:
        json.dump(employee, file, indent= 4)
        print(f"The json file {file_path} was created")
except FileExistsError:
    print("The file already exist")