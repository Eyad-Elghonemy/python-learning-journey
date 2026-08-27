#skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]

#while skills :
    
#    print(skills.pop(0))


my_friends = []

number = 4


while len(my_friends) < 4 :
    
    name = input("write name : ").strip()
    
    if name.isupper() ==  True :
    
      print("Invalid Name")
   

    elif name.islower() == True :
    
      number -=1 
    
      my_friends.append(name)
      
      print(f"Friend {name} Added => 1st Letter Become Capital")
      
      print(f"Names Left in List Is {number}")
    
    
    elif name.istitle() == True :
    
       number -=1 
    
       my_friends.append(name)
      
       print(f"Friend {name} Added => 1st Letter Become Capital")
      
       print(f"Names Left in List Is {number}")
    
    else :
        
        print("Invalid Name")
        

if number == 0 :
    
    print(my_friends)