# -------------------
# -- File Handling -- 
# -------------------
# "a" Append  Open File Appending Values, Create File If Not Exists
# "r" Read    [Default Value] Open File For Read And Give Error If File Is Not Exists
# "w" Write   Open File For Writing, Create File If Not Exists
# "x" Create  Create File, Give Error If File Exists 
# --------------------------------------------------

# import os

# print(os.getcwd())  # Get Current Working Directory

# print(os.path.dirname(os.path.abspath(__file__)))  # Main Current Working Directory

# Change Current Working Directory 

# os.chdir(os.path.dirname(os.path.abspath(__file__)))

# print(os.path.abspath(__file__))  # Absolute Path

# print(os.getcwd())

#file = open("C:\Users\eyad0\Documents\python\osama.txt")

file = open(r"C:\Users\eyad0\Documents\python\nfiles\osama.txt")