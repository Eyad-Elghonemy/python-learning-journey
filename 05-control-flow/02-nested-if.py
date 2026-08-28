# ---------------
# -- Nested If --
# ---------------

uname = "osama"
isstudent = "yes"
ucountry =input("what's your country")
cname = "python"
cprice = 100

if ucountry == "egypt" or ucountry == "kuwait" or ucountry == "ksa" :


    if isstudent == "yes" : 
    
       print(f"hello {uname}, because you are from {ucountry} and student")
       print(f"the course \"{cname}\" price is: ${cprice - 90}")
  
    
    else: 
        
       print(f"the course \"{cname}\" price is: ${cprice - 80}")
  
elif ucountry == "bahrain" or ucountry == "qatar" :
    
     print(f"hello {uname}, because you are from {ucountry}")
     print(f"the course \"{cname}\" price is: ${cprice - 60}")
  

  
else :
    print(f"hello {uname}, because you are from {ucountry}")
    print(f"the course \"{cname}\" price is: ${cprice - 30}")