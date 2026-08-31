# ---------------------
# --  Loop  =>  For  --
# --  Neasted  Loop  --
# ---------------------

# peoples = ["osama", "ahmed", "sayed", "ali"]

# skills = ['html', 'css', 'JS']

# for name in peoples : 
    
#    print(f"{name} skills is : ")
    
#    for skill in skills :
        
#        print(f"- {skill}")

peoples = {
    
    "Osama" : {
        "Html" : "70%" ,
        "Css"  : "80%" ,
        "JS"   : "70%"
    }, 
    "Ahmed" : {
        "Html" : "90%" ,
        "Css"  : "80%" ,
        "JS"   : "60%"
    },
    "Sayed" : {
        "Html" : "77%" ,
        "Css"  : "85%" ,
        "JS"   : "50%"
    }
}

# print(peoples["Osama"]['Css'])
# print(peoples["Sayed"]['JS'])

for name in peoples :

  print(f"Skills and progress for {name} is : ")
  
  for skill in peoples[name]:
      
      print(f"{skill.upper()} => {peoples[name][skill]}")