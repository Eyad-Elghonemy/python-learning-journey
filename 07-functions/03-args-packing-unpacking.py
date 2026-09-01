# ---------------------------------------
# -- Function Packing, Unpacking *Args --
# ---------------------------------------

# print(1,2,3,4)

# mylist = [1,2,3,4]

# print(mylist)
# print(*mylist)

def say_hello(*peoples) :  # n1, n2, n3, n4, n5
    
    
    for name in peoples :
        
        print(f"Hello {name}")
        
say_hello('osama', 'ahmed', 'sayed', 'mahmoud', 'alaa')



def show_details(name,*skills) :
    
    print(f"Hello {name} Your Skills Is :")
    
    for skill in skills :
        
        print(skill)
    
show_details("Osama","HTML", "CSS", "JS","Python")
show_details("Ahmed","HTML", "CSS", "JS","Python","PHP","mySQL")