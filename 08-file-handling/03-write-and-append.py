# -----------------------------------------------
# -- File Handling => write And Append In File --
# -----------------------------------------------

# myfile = open(r"C:\Users\eyad0\Documents\python\osama.txt", "w")

# myfile.write("Hello\n")
# myfile.write("Third Line")

# myfile = open(r"C:\Users\eyad0\Documents\python\fun.txt", "w")

# myfile.write("Elzero Web School\n"*1000)

# mylist = ["osama\n", "ahmed\n", "sayed\n"]

# myfile = open(r"C:\Users\eyad0\Documents\python\osama.txt", "w")
# myfile.writelines(mylist)

myfile = open(r"C:\Users\eyad0\Documents\python\osama.txt", "a")

myfile.write("Tessting Position\n\n\n")
myfile.write("osama")
myfile.write("Elzero")