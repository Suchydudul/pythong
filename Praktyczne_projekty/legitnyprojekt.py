import sys
import os


EXT_TO_LANG = {
  ".c": "C/C++",
  ".cc": "C/C++",
  ".h": "C/C++",
  ".hpp": "C/C++",
  ".cpp": "C/C++",
  ".ino": "C/C++",
  ".py": "Python",
  ".pyw": "Python",
  ".html": "HTML",
  ".htm": "HTML",
  ".md": "Markdown",
  ".css": "CSS",
  ".js": "JavaScript",
  ".bat": "Batch",
  ".pl": "Perl",
  ".php": "PHP",
  ".sh": "Bash",
}



def get_dir(): #gets the initial dir (root of the tree) from the an argument or via input
    if len (sys.argv) !=2:
        path = input("Please provide a valid path or provide an argument before running the program: (type exit to exit) ")
        if path.lower() == "exit": 
            sys.exit("\x1b[0;31m !!!!usage: legitnyprojekty.py <path>, for names with spaces put the path in quotes!!!! \x1b[39;49m")
            quit()
    else:
        path = sys.argv[1]
    print(f"path: \x1b[0;31m {path}\n \x1b[39;49m")
    return path



def get_stats(path): #Searches the main directory for files and sub directories and searches the files for contents
    extensions = set()
    num_lines = 0
    print(path)
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



def main():
    os.system("")
    path = get_dir()
    get_stats(path)




if __name__ == "__main__":
    main()