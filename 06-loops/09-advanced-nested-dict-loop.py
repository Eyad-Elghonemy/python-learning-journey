# ------------------------------
# -- Advanced Dictionary Loop --
# ------------------------------

myskills = {
    "HTML" : "80%",
    "CSS"  : "90%",
    "JS"   : "70%",
    "PHP"  : "80%"
}

#print(myskills.items())

#for skill in myskills :
    
#    print(f"{skill} => {myskills[skill]}")

#for skill_key , skill_value in myskills.items() :
    
#    print(f"{skill_key} => {skill_value}")

myultimateskills = {
    "HtML" : {
        "Main" : "80%",
        "Pugjs" : "80%"
    },
    "CSS" : {
        "Main" : "90%",
        "Sass" : "70%"
    }
}

for main_key , main_value in myultimateskills.items() : 
    
    print(F"{main_key} progress is : ")
    
    for child_key , child_value in main_value.items() :
        
        print(f"{child_key} => {child_value}")