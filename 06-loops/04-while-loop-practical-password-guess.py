# ----------------------------
# -- Loop => While Training --
# -- Simple password Gusses --
# ----------------------------

tries = 4

mainpassword = input("Enter The New Password :")

inputpassword = input("Write Your Password : ")

while inputpassword != mainpassword :
    
    tries -=1  
    
    print(f"Wrong Password, { 'last' if tries == 0 else tries } Chances Left")
    
    inputpassword = input("Write Your Password: ")
    
    if tries == 0 : 
        
        print("All Tries Is Finished")
        
        break
        
        # print("Will Not Print")
        
          
else :

    print("Correct Password!")
    
