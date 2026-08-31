# -----------------
# -- loop => for --
# --  Trainings  --
# -----------------

# Range

myrange = range(1, 101)

for number in myrange : 
    
    print (number)
    
# Dictionary 

myskills = {
    "Html" : "98%", 
    "css" : "88%", 
    "PHP" : "70%", 
    "JS" : "80%", 
    "PYTHON" : "90%", 
    "My SQL" : "91%",    
}

print(myskills['JS'])
print(myskills.get("PYTHON"))

for skill in myskills :
    
   # print(skill)
   
   print(f"my progress in lang {skill} is : {myskills[skill]}")