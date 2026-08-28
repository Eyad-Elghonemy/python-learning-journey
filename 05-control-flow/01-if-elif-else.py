# --------------------
# --  Control Flow  --
# -- If, Elif, Else -- 
# -- Make Decisions --
# --------------------

uname = "osama"
ucountry = "kuwait"
cname = "python"
cprice = 100

if ucountry == "egypt" :

    print(f"hello {uname}, because you are from {ucountry}")
    print(f"the course \"{cname}\" price is: ${cprice - 80}")
  
elif ucountry == "ksa" :
    
     print(f"hello {uname}, because you are from {ucountry}")
     print(f"the course \"{cname}\" price is: ${cprice - 60}")
  
elif ucountry == "kuwait" :
    
     print(f"hello {uname}, because you are from {ucountry}")
     print(f"the course \"{cname}\" price is: ${cprice - 50}")
  
else :
    print(f"hello {uname}, because you are from {ucountry}")
    print(f"the course \"{cname}\" price is: ${cprice - 30}")