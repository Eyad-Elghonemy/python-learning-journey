nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for num in nums :
    
    if num == 6 or num == 8 or num == 12 :
        
        continue
    
    else :
        
        print(str(num).zfill(2))
        
else :
    
    print("All Numbers Printed")