# ----------------------------------
# -- Practical Membership Control --
# ----------------------------------

# List Contains Admins
admins = ["Ahmed", "Sameh","Osama", "Manal","Rahma", "Mahmoud", "Enas"]

# Login
name = input("Please Type Your name").strip().capitalize()

# If Name Is In Admins 
if name in admins :
    
   print(f"Hello {name}, Welcome Back")
   
   option = input("Delete Or Update Your Name").strip().capitalize()
   
   # Update Option
   
   if option == "Update" or option == "U" :
       
       thenewname = input("Your New Name Please ").strip().capitalize()
       
       admins[admins.index("Osama")] = "Elzero"
       
       print("Name Updated!")
       
       print(admins)
       
       # Delete Option
       
   elif option == "Delete" or option == "D" :
       
       admins.remove(name)
    
       print("Name Deleted! ")
       
       print(admins)
      
   # Wrong Option   
       
   else : 
       
       print("Wrong Option!")   
else :
    
    status = input("Not Admin, Add You Y, N ? ").strip().capitalize()
    
    if status == "Yes" or "Y" :
        
        print("You  Have Been Added")
        
        admins.append(name)
        
        print (admins)
        
    else :
        
        print("You Are Not Added")    
      