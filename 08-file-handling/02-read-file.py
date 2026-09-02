# ---------------------------------
# -- Files Handling => Read File --
# ---------------------------------

myfile = open(r"C:\Users\eyad0\Documents\python\osama.txt", "r")

# print(myfile)  # File Data Opject

# print(myfile.name) 

# print(myfile.mode)  

# print(myfile.encoding)

# print(myfile.read(5))
# print(myfile.readline())
# print(myfile.readline())

# print(myfile.readlines())
# print(myfile.readlines(50))
# print(type(myfile.readlines()))

for line in myfile:
    
    print(line)

    if line.startswith("07") :
    
      break
  
  
# Close The File

myfile.close()