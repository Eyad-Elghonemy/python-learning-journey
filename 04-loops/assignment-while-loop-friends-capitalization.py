friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]


capital = 0
small = 0

while capital < len(friends) :
    
    if friends[capital][0].islower() == True :
        
        small += 1
        
    else :
        
        print(friends[capital])
        
    capital += 1 
        
print(f"Friends Printed And Ignored Names Count Is {small}")