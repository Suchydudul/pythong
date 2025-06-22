import sys 
import os
os.system("")
if len (sys.argv) !=2:
    sys.exit("\x1b[0;31m !!!!usage: listowanie.py <path>, for names with spaces put the path in quotes!!!! \x1b[39;49m")
path = sys.argv[1]
print(f"path: \x1b[0;31m {path}\n \x1b[39;49m")




extensions = set()
num_lines = 0

for(root, dirs, files) in os.walk(path):
    print(f"root: {root}\n")
    if dirs !=[]:
        print(f"dirs: {dirs}\n")
    print(f"files: {files}\n")

    for x in range(len(files)):
        name, extension = os.path.splitext(files[x])
        print(f" {name}, {extension}")
        if extension == ".py":
            f = open(root+"\\"+ files[x])
            lines = f.readlines()
            for row in lines:
                row = row.strip()
                if row != ""  and not row.startswith("#") :
                    #print(row)
                    num_lines +=1
            f.close
        extensions.add(extension)
    print("\x1b[0;32m-----------------\x1b[39;49m\n")
print(f"The extensions are: {extensions}")
print(f"Total number of lines in .py files: {num_lines}")