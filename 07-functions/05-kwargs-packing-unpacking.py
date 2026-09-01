# ----------------------------------------------------
# -- Function Packing, Unpacking Arguments **KWArgs --
# ----------------------------------------------------

# def show_skills(*skills) :
    
#     print(type(skills))
    
#     for skill in skills :
        
#         print(f"{skill}")
        
# show_skills('HTML', 'CSS', 'JS')


myskills = {
    "HTML" : "80%",
    "CSS" : "70%",
    "JS" : "50%",
    "python" : '50%',
    "Go" : "40%"
}


def show_skills(**skills) :
    
    print(type(skills))
    
    for skill, value in skills.items() :
        
        print(f"{skill} => {value}")
        
show_skills(**myskills)