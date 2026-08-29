# ----------------------------
# -- Loop => While Training --
# -- Simple Bookmark Manage --
# ----------------------------

# Empty List To Fill Later

myfavwebs = []

# Maximum Allowed Webs 
maximumwebs = 5

while maximumwebs > 0 : 
    
    # Input The New Website
    web = input("Website Name Without https:// ")
    
    # Add The New Website TO The List
    myfavwebs.append(f"https://{web.strip().lower()}")
    
    # Decrese One Number From Allowed Websites
    maximumwebs -= 1  # maximumwebs = maximumwebs + 1
    
    # Print THe Add Message 
    print(f"Website Added, {maximumwebs} Places Left")
    
    # Print The List
    print(myfavwebs)
    
else :
    
    print("Bookmark Is Full , You Can't Add More")
    
# Check If List Is Empty 
if len(myfavwebs) > 0 :
    # Sort The List
    
    myfavwebs.sort()
    
    index = 0
    
    print("Printing THe List Of Your Bookmark")
    
    while index < len(myfavwebs) :
        
        print(myfavwebs[index])
        
        index += 1  # index = index + 1 
        