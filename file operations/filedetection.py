import os

file_path = "README.md"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exist ")
else:
    print(f"The location '{file_path}' doesnt exist ")