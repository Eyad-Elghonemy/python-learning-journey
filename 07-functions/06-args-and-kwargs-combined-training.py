# -----------------------------------------------------
# -- Function Packing, Unpacking Arguments Trainings --
# -----------------------------------------------------

mytuple =  ("HTML", "CSS", "JS")


myskills = {
    "GO" : "80%",
    "Python" : "70%",
    "My SQL" : "50%"
}


def show_skills(name, *skills, **skillswithprogress) :
    
    print(f"Hello {name} \nSkills Without Progress Is :")
    
    for skill in skills :
        
        print(f"- {skill}")

    print("Skills With Progress Is : ")
    
    for skill_key, skill_value in skillswithprogress.items() :
        
        print(f"- {skill_key} => {skill_value}")

show_skills('osama', *mytuple, **myskills)

