num = int(input("write number : " ))

count = 0

if num < 0 or num == 0 : 
    
    print(f"Number {num} Is Not Larger Than 0 ")
    
else :
    
    pass

while num > 1 :
  
    num -=1
    
    if num == 6 :
        
        continue
    
    print(num)
    count += 1
print(f"{count} Numbers Printed Successfully")